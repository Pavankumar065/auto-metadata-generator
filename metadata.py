import nest_asyncio
import streamlit as st
from llama_index.core.schema import MetadataMode
from llama_index.llms.ollama import Ollama
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core import SimpleDirectoryReader
from llama_index.core.extractors import (
    SummaryExtractor,
    QuestionsAnsweredExtractor,
    TitleExtractor,
    KeywordExtractor,
)

import os
import tempfile
import asyncio

nest_asyncio.apply()

# Load LLM
llm = Ollama(model="tinyllama")

# Define extractors and transformations
text_splitter = TokenTextSplitter(separator=" ")

extractors = [
    TitleExtractor(nodes=5, llm=llm),
    QuestionsAnsweredExtractor(questions=3, llm=llm),
    SummaryExtractor(summaries=["prev", "self"], llm=llm),
    KeywordExtractor(keywords=10, llm=llm),
]

transformations = [text_splitter] + extractors

# Streamlit App UI
st.set_page_config(page_title="Metadata Extractor", layout="wide")
st.title("📄 Automated Metadata Generator")
st.markdown("Upload a document (PDF, DOCX, or TXT) to extract rich metadata.")

uploaded_file = st.file_uploader("Upload your document", type=["pdf", "docx", "txt"])

if uploaded_file:
    # Save uploaded file to temp directory
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp_file:
        tmp_file.write(uploaded_file.getbuffer())
        tmp_file_path = tmp_file.name

    st.info("📤 File uploaded. Processing for metadata extraction...")

    # Read file and extract specific sections
    docs = SimpleDirectoryReader(input_files=[tmp_file_path]).load_data()
    front_pages = docs[0:3]
    last_pages = docs[-3:] if len(docs) > 6 else docs
    selected_docs = front_pages + last_pages

    # Run the ingestion pipeline
    pipeline = IngestionPipeline(transformations=transformations)

    async def extract_metadata():
        return await pipeline.arun(documents=selected_docs)

    with st.spinner("⏳ Extracting metadata..."):
        nodes = asyncio.run(extract_metadata())

    # Show metadata of first result
    if nodes:
        st.success("✅ Metadata extracted successfully!")
        for i, node in enumerate(nodes):
            st.subheader(f"📄 Section {i+1}")
            st.json(node.metadata)
    else:
        st.error("❌ No metadata could be extracted.")

    # Clean up temp file
    os.remove(tmp_file_path)
