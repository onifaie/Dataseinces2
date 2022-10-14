

from pypdf2 import pdffileManager

import fitz

import streamlit as st
import os



def Readpdf():
    listpdf=[]

    uploaded_pdf = st.file_uploader("Load pdf: ", type=['pdf'])
    uploaded_pdf1 = st.file_uploader("Load pdf: ", type=['pdf'])
    uploaded_pdf2 = st.file_uploader("Load pdf: ", type=['pdf'])

    if uploaded_pdf is not None:
        with fitz.open(stream=uploaded_pdf.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            a=st.write(text) 
            # doc.close()
            fileReader = PyPDF2.PdfFileReader(a)

            
            
# def margen():
#     pdf=pdffileManager()
#     for file in os.listdir():
#         if file.endswith(".Pdf"):
#             pdf.append(file)
#     pdf.write("merge,pdf")
#     pdf.close()
#     st.write(" merge is Comblite ....Done ")
