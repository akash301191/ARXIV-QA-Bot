# ArXiv QA Bot

ArXiv QA Bot is a user-friendly Streamlit application that allows you to search and interact with research papers from arXiv. Powered by the [Agno](https://github.com/agno-agi/agno) framework and OpenAI's GPT-4o model, this tool enables you to explore the wealth of knowledge contained within arXiv papers through intuitive text-based interactions.

## Folder Structure

```
ArXiv-QA-Bot/
├── arxiv-qa-bot.py
├── README.md
└── requirements.txt
```

- **arxiv-qa-bot.py**: The main Streamlit application.
- **requirements.txt**: A list of all required Python packages.
- **README.md**: This documentation file.

## Features

- **ArXiv Search:** Easily query arXiv research papers using natural language.
- **Conversational Q&A:** Receive responses that include embedded arXiv references and a final "References" section with clickable links.
- **Transcript Download:** Save your conversation as a text file for later review.
- **Streamlined Interface:** A clean, interactive interface built with Streamlit.

## Prerequisites

- Python 3.11 or higher
- An OpenAI API key (get yours [here](https://platform.openai.com/account/api-keys))

## Installation

1. **Clone the repository** (or download it):
   ```bash
   git clone https://github.com/yourusername/arxiv-qa-bot.git
   cd arxiv-qa-bot
   ```

2. **(Optional) Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate        # On macOS/Linux
   # or
   venv\Scripts\activate           # On Windows
   ```

3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Streamlit app**:
   ```bash
   streamlit run arxiv-qa-bot.py
   ```
2. **Open your browser** to the local URL shown in the terminal (usually `http://localhost:8501`).
3. **Interact with the app**:
   - Enter your OpenAI API key when prompted.
   - Enter your arXiv search query.
   - The agent will return a response with embedded arXiv references and a final "References" section.
   - Download the transcript of your conversation if needed.

## Code Overview

- **`create_arxiv_agent`**: Initializes the ArXiv agent using OpenAI GPT-4o and ArxivTools.
- **`ask_arxiv_question`**: Handles user input by prompting for an arXiv search query, augmenting the query with instructions for references, processing the query via the agent, and displaying the response. It also appends the interaction to a transcript stored in Streamlit's session state.
- **`download_transcript`**: Provides a download button to save the entire Q&A session as a text file.
- **`main`**: Orchestrates the Streamlit app layout, captures the OpenAI API key, initializes the agent, and integrates all functionality.

## Contributions

Contributions are welcome! Feel free to fork the repository, make improvements, and open a pull request. Please ensure your changes follow the existing style and include any necessary documentation or tests.
