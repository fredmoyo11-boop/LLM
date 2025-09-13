# LLM Writing Assistant
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/fredmoyo11-boop/LLM)

This repository contains "WritePro," an LLM-based writing assistant designed to help users improve their written reports and essays. The application uses a local large language model (via Ollama) to suggest improvements. It features a FastAPI backend and an interactive Streamlit frontend.

The primary project code is located within the `project-two/` directory.

## Features

*   **Proofreading**: Detects and corrects grammar and spelling mistakes in your text.
*   **Rephrasing**: Suggests alternative phrasings for your sentences in various styles, including formal, casual, concise, and creative.
*   **Difference Viewer**: Clearly displays the changes between the original and the revised text, showing what has been added or removed.
*   **Intuitive Interface**: A clean and modern user interface built with Streamlit for a seamless user experience.

## Technology Stack

*   **Backend**: FastAPI
*   **Frontend**: Streamlit
*   **Local LLM**: Ollama
*   **Dependencies**: Uvicorn, Requests, Pydantic

## Getting Started

Follow these instructions to set up and run the project locally.

### 1. Prerequisites

*   Python 3.8+
*   An Ollama instance running a model like `deepseek-r1:70b`. The example file `project-two/examples/ollama_message.py` can be used to test your connection.

### 2. Installation

First, clone the repository to your local machine:
```bash
git clone https://github.com/fredmoyo11-boop/llm.git
cd llm/project-two
```

Next, create and activate a virtual environment:

On macOS/Linux:
```bash
python3 -m venv .pyenv
source .pyenv/bin/activate
```

On Windows:
```bash
python -m venv .pyenv
.pyenv\Scripts\activate
```

Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 3. Running the Application

You will need to run the backend and frontend in two separate terminal windows.

**Terminal 1: Start the Backend**

Navigate to the `project-two` directory and run the FastAPI backend:
```bash
python backend/backend.py
```
The backend will be available at `http://127.0.0.1:8000`.

**Terminal 2: Start the Frontend**

In a new terminal (with the virtual environment activated), navigate to the `project-two` directory and run the Streamlit frontend:
```bash
streamlit run frontend/myFrontend.py
```
The WritePro application will open in your web browser.

## Project Structure

```
└── project-two/
    ├── README.md               # Original project assignment details
    ├── requirements.txt        # Python dependencies
    ├── backend/
    │   └── backend.py          # FastAPI application
    ├── frontend/
    │   ├── frontend.py         # Original Streamlit frontend
    │   └── myFrontend.py       # Enhanced "WritePro" Streamlit frontend
    ├── examples/
    │   └── ollama_message.py   # Script to test Ollama connection
    └── Wireframe/
        ├── Wireframe.fig       # Figma wireframe file
        └── features.md         # Markdown describing selected UI features
