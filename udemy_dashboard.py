# importing libraries
import streamlit as st
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px
       
                          
st.set_page_config(layout='centered')
st.title('Udemy Courses EDA')
st.text('Developed By: @MuhamedMedhat')


 # importing data
df = pd.read_csv('udemy courses.csv')  
st.dataframe(df)
st.markdown('---')
col1 , col2,col3,col4= st.columns(4)

# How many courses in each subject?
st.subheader('How many courses in each subject?')
fig = px.bar(data_frame=df , x=df['subject'])
st.plotly_chart(fig)
st.markdown('---')


# What is the average price for each subject?
st.subheader('What is the average price for each subject?')
dic = dict(df.groupby('subject').mean()['price'].round())
fig = px.bar(data_frame=df,x=dic.keys(),y=dic.values())
fig.update_xaxes(title='subject')
fig.update_yaxes(title='avarege price')
st.plotly_chart(fig)       


# how many courses for each subject regarding : (paid & unpaid | level) ?
st.subheader('how many courses for each subject regarding : (paid & unpaid | level) ?')    
option = st.selectbox('Select an option',['is_paid','level'])
fig = px.bar(data_frame=df,x=df['subject'],color=option)
st.plotly_chart(fig)


# Number of Subscribers per Subject
st.subheader("Number of Subscribers per Subject")
option = st.selectbox("Select an option to split visuals",['is_paid','level'])
fig = px.bar(data_frame=df, x=df['subject'], color=option)
st.plotly_chart(fig)


# Number of subscribers per year
st.subheader("Number of Subscribers per Year")
fig = px.pie(names = df.groupby('year')['num_subscribers'].sum().index,
            values = df.groupby('year')['num_subscribers'].sum().values)
st.plotly_chart(fig)


# Number of courses per Level
st.subheader("Number of Courses per Level")
fig = px.bar(data_frame = df, x = 'level', color='subject')
st.plotly_chart(fig)


# correlation
st.subheader("Correlation")
fig = px.imshow(df.corr(),text_auto =True)
st.plotly_chart(fig)
