# Financial Agent

This project contains a financial agent that uses the Groq model to perform various tasks related to finance and web search. The agent can summarize analyst recommendations, share the latest news for specific stocks, and display financial data using tables.

## Features

- **Web Search Agent**: Searches the web for information using the DuckDuckGo tool.
- **Finance AI Agent**: Retrieves financial data such as stock prices, analyst recommendations, stock fundamentals, and company news using the YFinanceTools.
- **Multi-Agent**: Combines the capabilities of the Web Search Agent and Finance AI Agent to perform complex tasks.

## Setup

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/arshia1234567/Financial-Agent.git
    cd agenticAI
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:
        ```sh
        venv\Scripts\activate
        ```

    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

5. Create a [.env](http://_vscodecontentref_/0) file in the root directory and add your API keys:
    ```properties
    GROQ_API_KEY="your_groq_api_key"
    PHI_API_KEY="your_phi_api_key"
    ```

## Usage

1. Run the [financial_agent.py](http://_vscodecontentref_/1) script:
    ```sh
    python financial_agent.py
    ```

2. The agent will summarize analyst recommendations and share the latest news for NVDIA.

 
