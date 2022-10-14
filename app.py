# from . import home, model
# from . import data
from email.policy import default
import streamlit as st
# from pages import data# import your app modules here
from streamlit_option_menu import option_menu
from home import go 
from projects import project
from udemy import get_udemy
from test import call_test
from ecommerc import get_ecommerc

from pdffile import  Readpdf
# from PIL import Image
import base64

with st.sidebar:
    st.sidebar.image("Data/mypace.jpg", use_column_width=True,width=150 )


    st.sidebar.info('''
                    

                    * Email (onifsie@gmail.com)
                    * Server online activation 
                    * your working online Now ....
                    * [my website ](https://obeid.pro)
                    ''')

    selected=option_menu(
        
            menu_title="all_projects",
            options=["Home","ecommerce","web_Scrap","Data Analysis","Sentiment","NLP ","Open Cv ","Quran","Udemy","Schools_Deep","Tweeter","tiktok","Read PDF","test"],
            icons=["house","bank2","person-check-fill","book","house","mouse","phone","folder-symlink-fill","list-task","megaphone-fill","twitter","tiktok","file-earmark-pdf-fill"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
            styles={
        "container": {"padding": "0!important", "background-color": "#FCFAFA"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }

    )   
    
if selected=="Read PDF" :
     Readpdf() 
if selected=='web_Scrap':
        project()
   
       
if selected=="Home":
    go()

if selected=='Udemy':
    get_udemy()
if selected=='test':
    call_test()

if selected=='ecommerce':
    get_ecommerc()
    

            

st.sidebar.title("about me ")
st.sidebar.info('''
                
                   """## Obeid Al_otibi

This an open source project and you are very welcome to **contribute** your awesome
comments, questions, resources and apps as
[issues](https://github.com/MarcSkovMadsen/awesome-streamlit/issues) or
[pull requests](https://github.com/MarcSkovMadsen/awesome-streamlit/pulls)
to the [source code](https://github.com/MarcSkovMadsen/awesome-streamlit).

For more details see the [my website Personal ](https://obeid.pro) To Read More about me .

## The Developer

This project is developed by Marc Skov Madsen. You can learn more about me at
[this all my project In ML and Data Scenic ](https://obeid.pro).

                ''')
    
# selected=option_menu(
        
#      menu_title="all_projects",
#     options=["home","project","about us ","ML Projects "],
#     icons=["home","book","house"],
#     menu_icon="cast",
#     default_index=0,
#     orientation="horizontal"
            
#     )          




