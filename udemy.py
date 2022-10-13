import streamlit as st
import  pandas as pd 


def get_udemy():
    df=pd.read_csv("Data/udemy_courses.csv")
    
    st.write(df)
    
    st.markdown('''
                     
                     this home page 
                     ''')
    st.title("this my home page to show Data ")
    list=['1','2','3']
    
    st.selectbox('please select to show data ',list)
    