import os, tempfile
import streamlit as st
from langchain_community.llms import Cohere
from langchain_core.messages import HumanMessage
from langchain.vectorstores.chroma import Chroma
from langchain_community.embeddings import CohereEmbeddings
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import PyPDFLoader

# Streamlit app
st.subheader('Summarize Document')

# Get Cohere API key and source document input
with st.sidebar:
    os.environ["COHERE_API_KEY"] = st.text_input("Cohere API key", value="", type="password")
    st.caption("*If you don't have an Cohere API key, get it [here](https://dashboard.cohere.com/api-keys).*")
source_doc = st.file_uploader("Source Document", label_visibility="collapsed", type="pdf")

# If the 'Summarize' button is clicked
if st.button("Summarize"):
    # Validate inputs
    if not os.environ["COHERE_API_KEY"].strip() or not source_doc:
        st.error(f"Please provide the missing fields.")
    else:
        try:
            with st.spinner('Please wait...'):
              # Save uploaded file temporarily to disk, load and split the file into pages, delete temp file
              with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
                  tmp_file.write(source_doc.read())
              loader = PyPDFLoader(tmp_file.name)
              pages = loader.load_and_split()
              os.remove(tmp_file.name)

              # Create embeddings for the pages and insert into Chroma database
              embeddings = CohereEmbeddings(model="small")
              vectordb = Chroma.from_documents(pages, embeddings)

              # Initialize the Cohere module, load and run the summarize chain
              model = Cohere(model="command", temperature=0.75)
              chain = load_summarize_chain(model, chain_type="stuff")
              search = vectordb.similarity_search(" ")
              summary = chain.run(input_documents=search, question="Write a summary within 200 words and use bulet points.")

              st.success(summary)
        except Exception as e:
            st.exception(f"An error occurred: {e}")