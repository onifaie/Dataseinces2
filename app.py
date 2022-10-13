import streamlit as st
from multiapp import MultiApp
from apps import home, data ,model# import your app modules here

app = MultiApp()


col1, col2, col3 = st.columns(3)


app.add_app("web scrapting Noon ", home.app)
app.add_app("web scraping For NBA Football", data.app)
app.add_app("web scraping Jobs ", model.app)
app.run()


