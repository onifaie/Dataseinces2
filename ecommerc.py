from cProfile import label
import datetime
from email.utils import collapse_rfc2231_value
from functools import cache
from sqlite3 import Row
from tkinter.font import names
import streamlit as st 
import numpy as np 
import pandas as pd 
import plotly.express as px
from PIL import Image
import  matplotlib.pyplot as plt 

from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

from gb import get_Tabls


# @st.cache
def get_ecommerc():
    st.subheader(' Ecommerc Project many skills can you find here ')
    with st.expander("Information About Project"):
        st.write("""
           this page tell you how Scrap Udemy website 
           * about 5000 Courses Scraping 
           * look up by Subject or Price or any filed 
        
           * make chart depand what's you selection 
           * Recommanded about what's the best Course and NLP Students 
           
        """)
        st.image("https://www.usnews.com/dims4/USNEWS/305c384/2147483647/thumbnail/970x647/quality/85/?url=http%3A%2F%2Fmedia.beam.usnews.com%2F38%2Fe6%2F58c88e3c4d2e9dd1a7055521da7f%2F201016-udemy-stock.png",width=150)
        
 
    #Quantity , UnitPrice 
        
    # this section about Tabs 
 

    data=pd.read_csv('Data/data-2.csv',nrows=50)#, index_col=0)
    # data['total']=data[('UnitPrice' )*('Quantity')]
    # st.text(data.shape())
    # st.map(data['Country'])
    
    st.write(data.shape)
    # st.write(data.dtypes)
#Country
    st.markdown('''_ _ _ ''')
    # st.write(AgGrid(data))
    col1 , col2 =st.columns(2)
    col1.markdown('this Table Avtivatiy with users can be doing   \n* fillter \n * sorting \n * selection \n * Loook up \n * Freeze Colum by name ')
    col2.markdown('you can do with this Table is  \n* fillter \n * sorting \n * selection \n * Loook up \n * Freeze Colum by name ')
    st.markdown(' ### whats the skills we will applying \n * how explore Data \n* how clean Data \n* make gruop by  countery \n * make new colum  \n* make Total colum \n* make provit_Table  ')
    

    get_Tabls(data)
    # gb = GridOptionsBuilder.from_dataframe(data)
    # gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    # gb.configure_side_bar() #Add a sidebar
    # gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    # gridOptions = gb.build()

    # grid_response = AgGrid(
    #     data,
    #     gridOptions=gridOptions,
    #     data_return_mode='AS_INPUT', 
    #     update_mode='MODEL_CHANGED', 
    #     fit_columns_on_grid_load=False,
    #     # theme='blue', #Add theme color to the table
    #     enable_enterprise_modules=True,
    #     height=500, 
    #     width='100%',
    #     reload_data=True
    # )

    # st.write(data = grid_response['data'].head(4))
    # selected = grid_response['selected_rows'] 
    # st.write(df=pd.DataFrame(selected)) #Pass the selected rows to a new dataframe df
    # st.markdown("""- - - - """)
    # # st.line_chart(data[['InvoiceNo']].head(10))
    st.markdown('''_ _ _ ''')
    
    
    # this Start charting Pie this values and how you can showing on page 
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs','contery'
    sizes = [15, 30, 45, 10,88]
    explode = (0, 0.1, 0, 0,0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=49)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)