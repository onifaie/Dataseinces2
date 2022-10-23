import streamlit as st
import pandas as  pd
import numpy as np 



def teacher():
          
    
  df=pd.read_csv("Data\obeid3.txt",encoding="utf-8",nrows=300000)
  st.write(df)
  df2 = df.groupby(['EdarhName'])['kindjop'].value_counts()
  st.write(df2)
  df3=df.pivot_table(df2,['EdarhName'],'section').value_counts()
  st.write(df3)
  table = pd.pivot_table(df2, ['EdarhName'], ['section'])
                        