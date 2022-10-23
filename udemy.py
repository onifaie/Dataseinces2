import datetime
from email.utils import collapse_rfc2231_value
from functools import cache
from tkinter.font import names
import streamlit as st 
import numpy as np 
import pandas as pd 
import plotly.express as px
from PIL import Image
import  matplotlib.pyplot as plt 
# import random
import random
from gb import get_Tabls


from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

    

def get_udemy():
    title=st.title("Udemy Analysis")
    # st.set_page_config(page_title="Udemy Analysis", layout="wide")


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
    r=data.groupby(by='subject')[['price','subject','level','content_duration']].sum()
    st.bar_chart(r)
    st.markdown('''_ _ _ ''')
    
    
    m=(pd.DataFrame(data))
    # number = st.number_input('Insert a number')
    t=st.slider('chooes to show Data ',1,100)
    xx=pd.DataFrame(data)
    xx['Randon']=np.random.randint(0,100, size=len(xx))
    xx['total']=(xx['price']/2).astype(int)
    st.subheader('this show fileds and new one name of Total and show it ')
    st.write(m.loc[m.subject=='Business Finance',['price','content_duration','course_title','level','subject','total','Randon']])
    st.subheader('this Dara Frame if price == 50 and content_duration <100')
    st.write(m.query('price == 50 and content_duration < 50'))
<<<<<<< HEAD
    # dd=(data.groupby(by='subject').sum()).to_dict()
    # st.table(dd)
    # st.plotly_chart(dd,x='subject',y='price')
    # plt.plot(m,x='subject',y='price')
    a=xx.groupby(by='subject')[['price',"content_duration",'total']].max()
    z=plt.plot(a)
    
    st.markdown('''_ _ _
                
                *    a=xx.groupby(by='subject')[['price',"content_duration",'total']].max() \n
                *     st.bar_chart(a)


                ''')
    st.bar_chart(a)
    # return title 

























    st.code('''
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
# import random
import random



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
    st.line_chart(data[['subject','price']].head(10))
    
    
    m=(pd.DataFrame(data))
    # number = st.number_input('Insert a number')
    t=st.slider('chooes to show Data ',1,100)
    xx=pd.DataFrame(data)
    xx['Randon']=np.random.randint(0,100, size=len(xx))
    xx['total']=(xx['price']/2).astype(int)
    st.subheader('this show fileds and new one name of Total and show it ')
    st.write(m.loc[m.subject=='Business Finance',['price','content_duration','course_title','level','subject','total','Randon']])
    st.subheader('this Dara Frame if price == 50 and content_duration <100')
    st.write(m.query('price == 50 and content_duration < 100 '))
    # dd=(data.groupby(by='subject').sum()).to_dict()
    # st.table(dd)
    # st.plotly_ch
            
            '''          
            )
    
    st.write(get_Tabls(m))
    y=m.groupby(by=['subject']).sum()
    p=(y[['price','total','is_paid']])
    zz=plt.plot(p)
    st.write(p)

   
=======
    # dd=(data.groupby(by='subject').sum()).to_dict()
    # st.table(dd)
    # st.plotly_chart(dd,x='subject',y='price')
    # plt.plot(m,x='subject',y='price')
    a=xx.groupby(by='subject')[['price',"content_duration",'total']].max()
    z=plt.plot(a)
    
    st.markdown('''_ _ _
                
                *    a=xx.groupby(by='subject')[['price',"content_duration",'total']].max() \n
                *     st.bar_chart(a)


                ''')
    st.bar_chart(a)
    # return title 

























    st.code('''
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
# import random
import random



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
    st.line_chart(data[['subject','price']].head(10))
    
    
    m=(pd.DataFrame(data))
    # number = st.number_input('Insert a number')
    t=st.slider('chooes to show Data ',1,100)
    xx=pd.DataFrame(data)
    xx['Randon']=np.random.randint(0,100, size=len(xx))
    xx['total']=(xx['price']/2).astype(int)
    st.subheader('this show fileds and new one name of Total and show it ')
    st.write(m.loc[m.subject=='Business Finance',['price','content_duration','course_title','level','subject','total','Randon']])
    st.subheader('this Dara Frame if price == 50 and content_duration <100')
    st.write(m.query('price == 50 and content_duration < 100 '))
    # dd=(data.groupby(by='subject').sum()).to_dict()
    # st.table(dd)
    # st.plotly_ch
            
            '''          
            )
    
    st.write(get_Tabls(m))
>>>>>>> 9664e2dda39284a84ea46c40c61743381d51a56e
