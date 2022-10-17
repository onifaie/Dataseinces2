import  pyttsx3
from PyPDF2 import PdfFileWriter, PdfFileReader
import  PyPDF2 
import fitz

import streamlit as st
import os



def Readpdf():
    audio_file = open('Data/sample4.wav', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/ogg')
    

    uploaded_pdf = st.file_uploader("Load pdf: ", type=['pdf'])
    pdfReader=PyPDF2.PdfFileReader(uploaded_pdf)
    pages=pdfReader.numPages
    speaker=pyttsx3.init()
    for num in range(0,pages):
        page=pdfReader.getPage(1)
        text=page.extractText()
        speaker.say(text)
        speaker.runAndWait()
        st.write(text)
        # st.audio.stop(text)
        
 
    
    
def readSound(self,text):
    speaker=pyttsx3.init()
    speaker.stop(text)
    





    # if uploaded_pdf is not None:
    #     with fitz.open(stream=uploaded_pdf.read(), filetype="pdf") as doc:
    #         text = ""

    #         for page in doc:
    #             text += page.get_text()
    #         t=st.write(text) 
    #         text=PyPDF2.PdfFileReader(uploaded_pdf)

    #         speaker=pyttsx3.init()
    #         from_page = pdfReader.getPage(0)
    #         speaker.say(from_page)
    #         speaker.runAndWait()
            # doc.colse()

            
            # doc.close()
        # text = from_page.extractText()

        # speak = pyttsx3.init()
        # speak.say(text)
        # speak.runAndWait()

            
            
# def margen():
#     pdf=pdffileManager()
#     for file in os.listdir():
#         if file.endswith(".Pdf"):
#             pdf.append(file)
#     pdf.write("merge,pdf")
#     pdf.close()
#     st.write(" merge is Comblite ....Done ")
