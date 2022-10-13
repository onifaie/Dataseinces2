import streamlit as st


def project():
    
    st.markdown('''
                     
                     this home page 
                     ''')
    st.title("this my home page to show Projects ")
    list=['1','2','3']
    
    with st.sidebar:
        st.selectbox('this all City plese chooes ',
                    list)             