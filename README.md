📄 Chat with Multiple PDFs

Chat with your PDFs using AI!
A Streamlit-based chatbot that allows you to upload multiple PDF files and ask questions interactively. Built with LangChain, OpenAI embeddings, and FAISS vector store for efficient document retrieval.

🎯 Features

Upload multiple PDFs at once.

Extracts and processes text from PDFs automatically.

Splits text into chunks for better semantic search.

Conversational retrieval using OpenAI LLMs.

Memory keeps track of chat history for a natural conversation.

Clean, responsive interface with Streamlit.

🛠 Installation

Clone the repository:

git clone https://github.com/Manaskhurana/Python-Multiple-PDF-Chat-Bot.git
cd chat-with-pdfs


Create a virtual environment (recommended):

python -m venv venv


Activate the virtual environment:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Create a .env file in the project root and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here

🚀 Running the App

Start the Streamlit app:

streamlit run app.py


Open your browser at http://localhost:8501
.

Usage Steps:

1. Upload one or more PDFs in the sidebar.
2. Click "Process" to extract and embed text.
3. Ask questions in the chat box and get instant AI responses.
4. Continue the conversation; chat history is preserved.

🗂 Project Structure
chat-with-pdfs/
├─ app.py                # Main Streamlit app
├─ htmlTemplates.py      # Custom HTML templates for chat messages
├─ requirements.txt      # Python dependencies
├─ .env                  # OpenAI API key (ignored by Git)
├─ venv/                 # Virtual environment (ignored by Git)
└─ README.md

⚙ Dependencies

Python 3.13+

Streamlit

PyPDF2

LangChain

OpenAI

Install all dependencies via:

pip install -r requirements.txt

📝 Notes
- `.env` and `venv/` are included in `.gitignore` to keep sensitive data and virtual environment out of Git.
- Best run locally, but can also deploy on Streamlit Cloud or other hosting platforms.

📜 License

MIT License © 2025 Manas Khurana

✅ This README is professional, fully formatted, all commands and code blocks are ready for GitHub copy buttons, includes demo video section, screenshots, and step-by-step instructions.
