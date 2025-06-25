# Automated Metadata Generation

This project aimed at building an intelligent system for **automatically extracting semantic metadata** from documents like PDF, DOCX, and TXT. The system leverages Large Language Models (LLMs) and document processing techniques to enhance **discoverability**, **classification**, and **analysis** of unstructured data.

---

## Objective

To develop an automated system that extracts **scalable**, **consistent**, and **semantically rich metadata** from uploaded documents. This improves how documents are indexed, searched, and analyzed.

---

## Key Areas of Focus

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

### Semantic Content Identification
Uses **token-based splitting** and **LLM extractors** to identify the most meaningful sections of the document for metadata generation.

### Structured Metadata Creation
Generates structured metadata in dictionary/JSON format that can be further consumed, stored, or used for classification and analytics.

### User Interface Development
A clean and interactive **Streamlit web interface** allows:
- Document upload
- Live viewing of extracted metadata

### System Deployment
The system is ready for deployment on platforms like:
- **Streamlit Cloud**
- **Hugging Face Spaces**
- **Localhost**

---

## Features

This Automated Metadata Generator provides a user-friendly and interactive experience with several key features:

* **Intelligent Metadata Extraction:** Automatically extracts core semantic metadata including:
    * Document Title
    * Concise Summary
    * Relevant Keywords
    * Contextual Questions the document excerpt can answer
* **Multi-Format Document Support:** Seamlessly processes documents in various common file formats:
    * **PDF**
    * **DOCX**
    * **TXT**
* **Live Metadata Display:** After uploading a file and initiating the process, the extracted metadata is displayed live on the webpage, providing immediate feedback.
* **Interactive Controls:**
    * **"Browse files" button:** Allows easy selection and upload of documents.
    * **"Running" / "Stop" buttons:** Provides control over the metadata generation process, allowing users to rerun or halt operations as needed.
* **Responsive Layout Options:** Adjust the display mode of the application to suit your viewing preference:
    * **Wide Mode:** Expands the application to occupy the entire width of your screen.
    * **Standard Mode:** Default layout for a more compact view.
* **Customizable Theme:** Personalize your experience with built-in theme options:
    * **Light Mode:** A brighter interface for day-time use.
    * **Dark Mode:** A darker interface for reduced eye strain in low-light conditions.
    * **Custom Theme Editor:** Allows users to fine-tune primary, background, and text colors, along with font families, for a completely personalized visual style.

## Technologies & Tools Used

| Category          | Tools & Libraries                          |
|-------------------|--------------------------------------------|
| LLM Inference     | Ollama + TinyLLaMA                         |
| Document Parsing  | LlamaIndex, SimpleDirectoryReader          |
| Metadata Extraction | TitleExtractor, SummaryExtractor, etc.     |
| UI Framework      | Streamlit                                  |
| File Handling     | Python `tempfile`, `os`                    |
| Async Handling    | nest_asyncjo                               |

This project uses [Ollama](https://ollama.com) to run local Large Language Models (LLMs) for metadata extraction.

Specifically, it uses:

-   **Model**: `tinyllama`
-   **Reason**: Lightweight, fast, and suitable for local experimentation without needing a GPU and open source.
-   **How it's used**: Passed into `llama-index`'s extractor modules for title, summary, keywords, and Q&A generation.

## Installing Ollama and LLM Model
To use LLM-based extractors, this project depends on Ollama — a local LLM runner that lets you run open-source models like TinyLLaMA, Mistral, and more.

**Step-by-Step Installation (for Windows/Mac/Linux)**
1.  Download and install Ollama from the official site:
    [https://ollama.com/download](https://ollama.com/download)
2.  Start the Ollama service (it usually runs automatically after install).
3.  Pull the `tinyllama` model used in this project:

    ```bash
    ollama pull tinyllama
    ```

---

## How to Run the Project

### Step 1: Clone the Repo

```bash
git clone [https://github.com/Pavankumar065/auto-metadata-generator.git](https://github.com/Pavankumar065/auto-metadata-generator.git)
cd auto-metadata-generator
```
---

### Step 2: Install Requirements
```bash
pip install -r requirements.txt
```
---

### Step 3: Run the Streamlit App
```bash
streamlit run streamlit_app.py
```
---

## How to Access the Website

You can access the Automated Metadata Generator either by running it locally on your machine or by visiting its publicly deployed version.

**Using the Local Application:**

After opening the URL in your browser:

1.  **Upload Document:** Click the **"Browse files"** button (or drag and drop a file) to select a PDF, DOCX, or TXT document from your computer.
2.  **Generate Metadata:** Once a file is selected, the system will automatically begin **"Processing for metadata extraction..."** and then display **"Extracting metadata..."**.
3.  **View Live Results:** After successful extraction, you will see a green **"Metadata extracted successfully!"** message, and the extracted Document Title, Summary, Keywords, and Questions will appear live on the page.
4.  **Control Generation:**
    * If the system is running, a **"Running"** indicator will be visible. You can click the **"Stop"** button (usually next to "Running" at the top right) to halt the process.
    * To restart the extraction for the same or a new file, you can often click a **"Rerun"** button (also usually at the top right, under the "Deploy" dropdown).
5.  **Adjust Layout:** To change the display size, click the "Settings" icon (often a gear or three dots) usually located at the top right. From there, you can enable **"Wide mode"** to make the app occupy the entire screen width.
6.  **Change Theme:** Within the "Settings" menu, you'll find options to "Choose app theme". You can select **"Light"**, **"Dark"**, or **"Use system setting"**. Additionally, you can **"Edit active theme"** to customize colors (Primary, Background, Text, Secondary Background) and Font Family.

### 2. Deployed Application Link:

If the project is deployed to a cloud platform (like Streamlit Cloud or Hugging Face Spaces), you can access it directly via its public URL. The usage steps will be identical to the "Local Access" section above.


##**Demo Video:**

For a visual demonstration of the project's features and functionality, watch the demo video on YouTube:

▶️ **https://youtu.be/lZhl7Jj_yG0?si=cjFVacUaVZPjHoUl** 


