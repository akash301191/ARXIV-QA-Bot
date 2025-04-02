import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.arxiv import ArxivTools

def create_arxiv_agent(api_key: str) -> Agent:
    """
    Initialize the arXiv agent with OpenAI GPT-4o and ArxivTools.
    """
    return Agent(
        model=OpenAIChat(
            id="gpt-4o",
            max_tokens=1024,
            temperature=0.9,
            api_key=api_key
        ),
        tools=[ArxivTools()]
    )

def ask_arxiv_question(agent: Agent) -> None:
    """
    Prompts the user for an arXiv search query, runs the agent, displays the answer,
    and stores the conversation in session state.
    """
    query = st.text_input("Enter the ArXiv search query: ", type="default")
    if query:
        augmented_query = f"""
        {query}

        Please provide your answer with appropriate arXiv references embedded in the text. At the end, include a 'References' section listing the corresponding arXiv links for each reference.
        """
        
        response = agent.run(augmented_query, stream=False)
        st.write(response.content)
        # Initialize transcript if not present
        if "transcript" not in st.session_state:
            st.session_state.transcript = ""
        # Append the query and response to the transcript
        st.session_state.transcript += f"Query: {query}\nResponse: {response.content}\n\n"

def download_transcript() -> None:
    """
    Provides a download button for the conversation transcript.
    """
    transcript = st.session_state.get("transcript", "")
    if transcript:
        st.download_button(
            label="Download Conversation Transcript",
            data=transcript,
            file_name="arxiv-qa-transcript.txt",
            mime="text/plain"
        )

def main() -> None:
    """
    Main function to run the Streamlit app.
    """
    st.set_page_config(page_title="ArXiv QA Bot")

    # Optional: Inject custom CSS for styling (if desired)
    st.markdown(
        """
        <style>
        .block-container {
            padding-left: 0rem !important;
            padding-right: 0rem !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 style='font-size: 2.5rem;'>🔎 ArXiv QA Bot</h1>", unsafe_allow_html=True)
    st.markdown(
        "Welcome to ArXiv QA Bot — a user-friendly tool that lets you search and chat with research papers from arXiv."
    )
    st.markdown("<br>", unsafe_allow_html=True)

    # Get OpenAI API key from user
    openai_api_key = st.text_input(
        "OpenAI API Key",
        type="password",
        help="Don't have an API key? Get one [here](https://platform.openai.com/account/api-keys)."
    )
    if not openai_api_key:
        return

    # Initialize the agent
    agent = create_arxiv_agent(openai_api_key)

    st.markdown("<br>", unsafe_allow_html=True)
    # Process user query and display response
    ask_arxiv_question(agent)
    # Provide option to download the transcript
    download_transcript()

if __name__ == "__main__":
    main()
