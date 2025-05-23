import pandas as pd
import altair as alt
import plotly.express as px
import streamlit as st 

st.title("📊 Accident Dashboard - Home Page")

if 'df_titanic' not in st.session_state:
    st.session_state['df_titanic'] = pd.read_csv("./dataset/titanic3.csv",low_memory=False, on_bad_lines='skip') 

df_titanics3 = st.session_state['df_titanic']

st.header("✅ 1. Data Overview")

total_passengers = len(df_titanics3)
st.subheader(f"Show total number of passengers: {total_passengers}")

if 'survived' in df_titanics3.columns:
    survivors = df_titanics3['survived'].sum()
    survival_rate = (survivors / total_passengers) * 100
    st.subheader(f"Survivors percentage: {survival_rate:.2f}%")
    st.subheader(f"Deceased percentage: {100 - survival_rate:.2f}%")
else:   
    st.error("The 'survived' column was not found in the CSV file. Please check the input file.")

st.header("Missing Data")
missing_data = df_titanics3.isnull().sum()  # Show the amount of missing data
missing_percentage = (missing_data / total_passengers) * 100  # Calculate the percentage of missing data
missing_data_df = pd.DataFrame({
    "Column": missing_data.index,
    "Missing Data": missing_data.values,
    "Percentage (%)": missing_percentage.values
})
st.dataframe(missing_data_df)

# ✅ 3. Interactive Filters (in the sidebar)
st.sidebar.header("✅ 3. Interactive Filters (in the sidebar)")

sex_options = df_titanics3['sex'].dropna().unique().tolist()
sex_selected = st.sidebar.multiselect("Sex", options=sex_options, default=sex_options)

class_options = df_titanics3['pclass'].dropna().unique().tolist()
class_options_mapped = {1: '1st Class', 2: '2nd Class', 3: '3rd Class'}
class_labels_reverse = {v: k for k, v in class_options_mapped.items()}
class_selected = st.sidebar.multiselect("Class", options=[class_options_mapped[c] for c in class_options], default=[class_options_mapped[c] for c in class_options])

status_options = {'Survivors': 1, 'Non-Survivors': 0}
status_selected = st.sidebar.multiselect("Status", options=list(status_options.keys()), default=list(status_options.keys()))

df_titanics3 = df_titanics3[
    (df_titanics3['sex'].isin(sex_selected)) &
    (df_titanics3['pclass'].isin([class_labels_reverse[c] for c in class_selected])) &
    (df_titanics3['survived'].isin([status_options[s] for s in status_selected]))
]

st.header("✅ 2. Required Visual Analyses")

# Bar chart showing survival rate by sex.
if 'sex' in df_titanics3.columns and 'survived' in df_titanics3.columns:
    survival_rate_sex = df_titanics3.groupby('sex')['survived'].mean() * 100
    survival_rate_sex_df = survival_rate_sex.reset_index()  # Convert to DataFrame
    fig_sex = px.bar(
        survival_rate_sex_df,
        x='sex', 
        y='survived',  
        labels={'sex': 'Sex', 'survived': 'Survival Rate (%)'},
        title="Survival Rate by Sex"
    )
    st.plotly_chart(fig_sex)
else:
    st.error("The columns 'sex' and/or 'survived' were not found in the CSV file.")

# Bar chart: Age vs Survival.
if 'age' in df_titanics3.columns and 'survived' in df_titanics3.columns:
    # Replace commas with dots and convert to numeric
    df_titanics3['age'] = df_titanics3['age'].astype(str).str.replace(',', '.')
    df_titanics3['age'] = pd.to_numeric(df_titanics3['age'], errors='coerce')

    bins = [0, 9, 15, 20, 30, 45, 60, 100]
    labels = ['0-9', '10-15', '16-20', '21-30', '31-45', '46-60', '61-100']
    df_titanics3['Age Group'] = pd.cut(df_titanics3['age'], bins=bins, labels=labels, right=False)

    df_grouped = df_titanics3.groupby(['Age Group', 'survived']).size().reset_index(name='count')

    df_grouped['Status'] = df_grouped['survived'].map({0: 'Did Not Survive', 1: 'Survived'})  # Map 0/1 to text

    fig_bar = px.bar(
        df_grouped,
        x='Age Group',
        y='count',
        color='Status',
        barmode='group',
        labels={'count': 'Number of People', 'Age Group': 'Age Group'},
        title="Survival Distribution by Age Group"
    )

    st.plotly_chart(fig_bar)

# Bar chart: Survival by Ticket Class (Pclass)
if 'pclass' in df_titanics3.columns and 'survived' in df_titanics3.columns:
    survival_rate_class = df_titanics3.groupby('pclass')['survived'].mean() * 100
    fig_class = px.bar(
        survival_rate_class,
        x=survival_rate_class.index,
        y=survival_rate_class.values,
        labels={'x': 'Ticket Class', 'y': 'Survival Rate (%)'},
        title="Survival Rate by Ticket Class"
    )
    st.plotly_chart(fig_class)
else:
    st.error("The columns 'pclass' and/or 'survived' were not found in the CSV file.")

# Bar chart: Number of survivors by ticket class (Pclass).
if 'pclass' in df_titanics3.columns and 'survived' in df_titanics3.columns:
    df_survivors = df_titanics3[df_titanics3['survived'] == 1]

    survivors_by_class = df_survivors['pclass'].value_counts().sort_index().reset_index()
    survivors_by_class.columns = ['Class', 'Quantity']

    class_labels = {1: 'VIP', 2: 'Middle Class', 3: 'Commoner'}
    survivors_by_class['Class'] = survivors_by_class['Class'].map(class_labels)

    fig_survivors_class = px.bar(
        survivors_by_class,
        x='Class',
        y='Quantity',
        labels={'Class': 'Ticket Class', 'Quantity': 'Number of Survivors'},
        title='Number of Survivors by Class'
    )

    st.plotly_chart(fig_survivors_class)
    
# Bar chart combining two variables (e.g., sex + class).
if 'sex' in df_titanics3.columns and 'pclass' in df_titanics3.columns and 'survived' in df_titanics3.columns:
    df_survivors = df_titanics3[df_titanics3['survived'] == 1]
    survivors_sex_class = df_survivors.groupby(['sex', 'pclass']).size().reset_index(name='Quantity')

    class_labels = {1: 'VIP', 2: 'Middle Class', 3: 'Commoner'}
    survivors_sex_class['Class'] = survivors_sex_class['pclass'].map(class_labels)

    fig_sex_class_qty = px.bar(
        survivors_sex_class,
        x='Class',
        y='Quantity',
        color='sex',
        barmode='group',
        labels={'Class': 'Ticket Class', 'Quantity': 'Number of Survivors', 'sex': 'Sex'},
        title='Number of Survivors by Sex and Class'
    )

    st.plotly_chart(fig_sex_class_qty)
else:
    st.error("The columns 'sex', 'pclass' and/or 'survived' were not found in the CSV file.")