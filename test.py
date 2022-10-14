import datetime
from email.utils import collapse_rfc2231_value
from functools import cache
from tkinter.font import names
import streamlit as st 
import numpy as np 
import pandas as pd 
# import plotly.express as px
from PIL import Image




from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode


def call_test():

    data=pd.read_csv('Data/udemy_courses.csv')#, index_col=0)


    # st.write(AgGrid(data))
    col1 , col2 =st.columns(2)
    col1.markdown('### this Table Avtivatiy with users  \n* fillter \n * sorting \n * selection \n * Loook up \n * Freeze Colum by name ')
    col2.markdown(' ### you can do with this Table is  \n* fillter \n * sorting \n * selection \n * Loook up \n * Freeze Colum by name ')

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
        height=350, 
        width='100%',
        reload_data=True
    )

    st.write(data = grid_response['data'])
    selected = grid_response['selected_rows'] 
    st.write(df=pd.DataFrame(selected)) #Pass the selected rows to a new dataframe df
    st.markdown("""- - - - """)
    st.line_chart(data[['subject','price']].head(10))

