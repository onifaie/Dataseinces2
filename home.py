from enum import auto
from turtle import width
import streamlit as st
import pandas as pd
import datetime
def go():
   st.image("Data/2.jpg",width=400)

   cm1,cm2=st.columns(2)
   with cm1:
      st.text('this some advaices for any one want to learn some thinks new')
      audio_file = open('Data/sample4.wav', 'rb')
      audio_bytes = audio_file.read()

      st.audio(audio_bytes, format='audio/ogg')
   with cm2:
      st.text('this the better song for me ')
      audio_file = open('Data/sample4.wav', 'rb')
      audio_bytes = audio_file.read()

      st.audio(audio_bytes, format='audio/ogg')
   
   
      st.title(datetime.date.today())   

   with st.expander("Information about me >>>"):
        st.write("""
           this page tell you how Scrap Udemy website 
           * Developer website [ Django - Python - Java Script]
           * master Of AI  & ML  with Data Analysis   
        
           * work with yolo library  to detection  many thinks   
           * work with NLP System and healthy System  
           
        """)
        st.image("Data/mypace.jpg",width=100)
        
 
        col1, col2, col3 = st.columns(3)
        col1.metric("website  ", "94%", "30 Win")
        col2.metric("Data Since  ", "88%", "8%")
        col3.metric("AI & ML & NLP ", "93%", "20%")
        
        st.markdown("_ _ _ ")
        colm1,colm2=st.columns(2)
        colm1.image("https://static.streamlit.io/examples/dice.jpg",width=100)
        colm2.markdown('''
                       
                       * Email is (onifaie@gmail.com) 
                       * Mobile No is ( +966531935087 what's up ) 
                       ''')
                
                
            
            
    
   with st.expander("Summary about all Projects "):
        c1,c2,c3,c4=st.columns(4)
        # c1.st.image("https://www.cloudways.com/blog/wp-content/uploads/Ecommerce-Shopping-Infographics.png",width=100)

        st.markdown("""
           this page tell you how Scrap Udemy website 
           * Developer website [ Django - Python - Java Script]
           * master Of AI  & ML  with Data Analysis   
        
           * work with yolo library  to detection  many thinks   
           * work with NLP System and healthy System  
           
        """)
        
 
        col1, col2, col3 = st.columns(3)
        col1.metric("website  ", "94%", "30 Win")
        col2.metric("Data Since  ", "88%", "8%")
        col3.metric("AI & ML & NLP ", "93%", "20%")
        
        st.markdown("_ _ _ ")
        colm1,colm2=st.columns(2)
        colm1.image("https://static.streamlit.io/examples/dice.jpg",width=100)
        colm2.markdown('''
                       
                       * Email is (onifaie@gmail.com) 
                       * Mobile No is ( +966531935087 what's up ) 
                       ''')
                
                
            
            
        