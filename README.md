# Enhanced Q&A Chatbot

A Streamlit-based chatbot application that leverages LangChain and Groq's powerful language models to provide accurate answers to user questions.

## Overview

This project is a question-answering chatbot built with Streamlit and LangChain. It uses Groq's language models to generate responses to user queries. The application features a user-friendly interface with customizable settings for model selection, temperature, and token limits.

## Features

- **Multiple Model Support**: Choose from various Groq models including Gemma and Llama variants
- **Customizable Parameters**: Adjust temperature and max tokens to control response generation
- **User-Friendly Interface**: Clean Streamlit UI with sidebar for settings
- **LangSmith Integration**: Built-in tracking for monitoring and improving model performance

## Project Structure

- `app.py` - Main application file containing the Streamlit interface and LangChain implementation
- `requirements.txt` - List of required Python packages

## Prerequisites

- Python 3.8+
- Groq API key
- LangChain API key (for LangSmith tracking)

## Installation

1. Clone the repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root with your API keys:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   LANGCHAIN_API_KEY=your_langchain_api_key_here
   ```

## Usage

1. Start the application:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)
3. Enter your Groq API key in the sidebar
4. Select a model from the dropdown menu
5. Adjust temperature and max tokens settings as needed
6. Type your question in the input field
7. Click "Generate Response" to get an answer

## Available Models

The application supports the following Groq models:
- gemma2-9b-it
- llama3-70b-8192
- llama3-8b-8192
- llama-3.1-8b-instant
- llama-3.3-70b-versatile

## Customization

### Temperature

The temperature parameter controls the randomness of the model's output. Higher values (closer to 1.0) make the output more random, while lower values (closer to 0.0) make it more deterministic and focused.

### Max Tokens

This setting limits the length of the generated response. Adjust based on how detailed you want the answers to be.

## LangSmith Tracking

The application includes LangSmith integration for tracking and analyzing model performance. This helps in monitoring usage patterns and improving the chatbot over time.

## Dependencies

Major dependencies include:
- Streamlit: For the web interface
- LangChain: For building the language model chain
- Groq API: For accessing the language models
- python-dotenv: For environment variable management

## License

[MIT License](LICENSE)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- [LangChain](https://www.langchain.com/) for the powerful LLM framework
- [Groq](https://groq.com/) for the fast inference platform
- [Streamlit](https://streamlit.io/) for the easy-to-use web application framework
