import datetime
from email.utils import collapse_rfc2231_value
from functools import cache
from tkinter.font import names
import streamlit as st 
import numpy as np 
import pandas as pd 
import plotly.express as px
from PIL import Image
from matplotlib import pyplot 



from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode



def get_udemy():
    st.subheader(f'Udemy # Pandas Analysis and ML & NLP Projects ')
    with st.expander("Information About Project"):
        st.write("""
           this page tell you how Scrap Udemy website 
           * about 5000 Courses Scraping 
           * look up by Subject or Price or any filed 
        
           * make chart depand what's you selection 
           * Recommanded about what's the best Course and NLP Students 
           
        """)
        st.image("https://www.usnews.com/dims4/USNEWS/305c384/2147483647/thumbnail/970x647/quality/85/?url=http%3A%2F%2Fmedia.beam.usnews.com%2F38%2Fe6%2F58c88e3c4d2e9dd1a7055521da7f%2F201016-udemy-stock.png",width=150)
        
 

        
    # this section about Tabs 
 

    data=pd.read_csv('Data/udemy_courses.csv')#, index_col=0)

    st.markdown('''_ _ _ ''')
    # st.write(AgGrid(data))
    col1 , col2 =st.columns(2)
    col1.markdown('this Table Avtivatiy with users  \n* fillter \n * sorting \n * selection \n * Loook up \n * Freeze Colum by name ')
    col2.markdown('you can do with this Table is  \n* fillter \n * sorting \n * selection \n * Loook up \n * Freeze Colum by name ')

    gb = GridOptionsBuilder.from_dataframe(data)
    gb.configure_pagination(paginationAutoPageSize=True) #Add pagination
    gb.configure_side_bar() #Add a sidebar
    gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren="Group checkbox select children") #Enable multi-row selection
    gridOptions = gb.build()

    grid_response = AgGrid(
        data,
        gridOptions=gridOptions,
        data_return_mode='AS_INPUT', 
        update_mode='MODEL_CHANGED', 
        fit_columns_on_grid_load=False,
        # theme='blue', #Add theme color to the table
        enable_enterprise_modules=True,
        height=500, 
        width='100%',
        reload_data=True
    )

    st.write(data = grid_response['data'])
    selected = grid_response['selected_rows'] 
    st.write(df=pd.DataFrame(selected)) #Pass the selected rows to a new dataframe df
    st.markdown("""- - - - """)
    st.line_chart(data[['subject','price']].head(10))
    st.markdown('''_ _ _ ''')
    
    
    m=(pd.DataFrame(data))
    # number = st.number_input('Insert a number')
    t=st.slider('chooes to show Data ',1,100)

    st.write(m.loc[[0,t]])
    
    # dd=(data.groupby(by='subject').sum()).to_dict()
    # st.table(dd)
    # st.plotly_chart(dd,x='subject',y='price')

  