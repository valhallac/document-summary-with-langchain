 **# Document Summarization with Langchain, Chroma, Cohere, and Streamlit**

This project provides a Python-based web application that efficiently summarizes documents using Langchain, Chroma, and Cohere's language models. It offers a user-friendly interface for browsing and summarizing documents with ease.

**Key Features:**

- Seamless integration of Langchain, Chroma, and Cohere for text extraction, embeddings, and summarization.
- Streamlined document selection and summary generation within a web app.
- Convenient Cohere API key input directly within the web browser for enhanced security.

<img width="1460" alt="image" src="https://github.com/valhallac/document-summary-langchain-chroma-cohere/assets/16238095/1f1960a8-15a9-4286-9373-9631518004be">


**Inspiration:**

- Inspired by the Langchain examples repository: [https://github.com/alphasecio/langchain-examples/blob/main/chroma-summary/langchain_doc_summarizer.ipynb](https://github.com/alphasecio/langchain-examples/blob/main/chroma-summary/langchain_doc_summarizer.ipynb)

**Installation and Setup:**

1. **Install Dependencies:**
   ```bash
   pip install -r document-summary-requirements.txt
   ```

2. **Obtain Cohere API Key:**
   - Create a Cohere account at [https://coherehealth.com/](https://coherehealth.com/)
   - Generate an API key from your account settings.

**Running the Web App:**

1. Navigate to the project directory.
2. Launch the web app using Streamlit:
   ```bash
   streamlit run document-summary.py
   ```

**Using the Web App:**

1. Upon launch, enter your Cohere API key in webpage.
2. Click the "Browse" button to select a document for summarization.
3. Click the "Summarize" button to initiate the summarization process.
4. The generated summary will be displayed in the app's output area.

**Contributing:**

Contributions are welcome to this project! Feel free to fork the repository and submit pull requests with improvements or bug fixes.

**Additional Notes:**

- The quality of summaries may depend on document quality and the accuracy of Langchain's text extraction.
- Consider the usage limits and potential costs associated with external LLM APIs (Cohere).
