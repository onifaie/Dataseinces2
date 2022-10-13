from turtle import width
import streamlit as st
import pandas as pd
import datetime
def go():
    st.title(datetime.date.today())   

    with st.expander("Information About Project"):
        st.write("""
           this page tell you how Scrap Udemy website 
           * about 5000 Courses Scraping 
           * look up by Subject or Price or any filed 
        
           * make chart depand what's you selection 
           * Recommanded about what's the best Course and NLP Students 
           
        """)
        st.image("https://www.usnews.com/dims4/USNEWS/305c384/2147483647/thumbnail/970x647/quality/85/?url=http%3A%2F%2Fmedia.beam.usnews.com%2F38%2Fe6%2F58c88e3c4d2e9dd1a7055521da7f%2F201016-udemy-stock.png",width=150)
        
 
        col1, col2, col3 = st.columns(3)
        col1.metric("Total", "70 °F", "1.2 °F")
        col2.metric("Wind", "9 mph", "-8%")
        col3.metric("Humidity", "86%", "4%")
        
        st.markdown("_ _ _ ")
        colm1,colm2=st.columns(2)
        colm1.image("https://static.streamlit.io/examples/dice.jpg",width=100)
        colm2.markdown('''
                       
                       * this how you can send Email by Streamlit app 
                       * many funcation call from inside application 
                       ''')
                
                
            
            
        