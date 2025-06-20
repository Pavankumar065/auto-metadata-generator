#  Automated Metadata Generation

This project aimed at building an intelligent system for **automatically extracting semantic metadata** from documents like PDF, DOCX, and TXT. The system leverages Large Language Models (LLMs) and document processing techniques to enhance **discoverability**, **classification**, and **analysis** of unstructured data.

---

##  Objective

To develop an automated system that extracts **scalable**, **consistent**, and **semantically rich metadata** from uploaded documents. This improves how documents are indexed, searched, and analyzed.

---

##  Key Areas of Focus

### Automating Metadata Generation
The system automatically extracts relevant metadata such as:
- Document Title
- Summary
- Keywords
- Questions the excerpt can answer

### Content Extraction
Supports multiple file formats:
- **PDF**
- **DOCX**
- **TXT**



###  Semantic Content Identification
Uses **token-based splitting** and **LLM extractors** to identify the most meaningful sections of the document for metadata generation.

###  Structured Metadata Creation
Generates structured metadata in dictionary/JSON format that can be further consumed, stored, or used for classification and analytics.

### User Interface Development
A clean and interactive **Streamlit web interface** allows:
- Document upload
- Live viewing of extracted metadata

###  System Deployment
The system is ready for deployment on platforms like:
- **Streamlit Cloud**
- **Hugging Face Spaces**
- **Localhost**




---

## Technologies & Tools Used

| Category        | Tools & Libraries                 |
|----------------|------------------------------------|
| LLM Inference   | Ollama + TinyLLaMA                |
| Document Parsing| LlamaIndex, SimpleDirectoryReader |
| Metadata Extraction | TitleExtractor, SummaryExtractor, etc. |
| UI Framework   | Streamlit                         |
| File Handling  | Python `tempfile`, `os`           |
| Async Handling | nest_asyncio                      |


This project uses [Ollama](https://ollama.com) to run local Large Language Models (LLMs) for metadata extraction.

Specifically, it uses:

- **Model**: `tinyllama`
- **Reason**: Lightweight, fast, and suitable for local experimentation without needing a GPU and open source.
- **How it's used**: Passed into `llama-index`'s extractor modules for title, summary, keywords, and Q&A generation.


## Installing Ollama and LLM Model
To use LLM-based extractors, this project depends on Ollama — a local LLM runner that lets you run open-source models like TinyLLaMA, Mistral, and more.

Step-by-Step Installation (for Windows/Mac/Linux)
Download and install Ollama from the official site:
 https://ollama.com/download

Start the Ollama service (it usually runs automatically after install).

Pull the tinyllama model used in this project:

ollama pull tinyllama


---

##  How to Run the Project

### Step 1: Clone the Repo

```bash
git clone https://github.com/Pavankumar065/auto-metadata-generator.git
cd auto-metadata-generator
```
---

### Step 2: Install Requirements
```
pip install -r requirements.txt
```
---

### Step 3: Run the Streamlit App
```
streamlit run streamlit_app.py
```
---




