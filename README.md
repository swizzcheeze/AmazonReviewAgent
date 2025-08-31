# AI-Powered Review Assistant (Agent Pipeline Edition)

An advanced, command-line tool that leverages a dual-agent AI pipeline to generate high-quality, context-aware product reviews. This assistant allows users to connect to multiple Large Language Model (LLM) providers, including Google's Gemini, Ollama, and LM Studio, to create nuanced and human-like reviews.

---

## Project Overview

This repository contains the full source code and documentation for the AI Review Assistant. For a detailed breakdown of the product vision, technical architecture, and future roadmap, please see the official project documents:

* [**Product Requirements Document (PRD)**](https://www.google.com/search?q=Product_Requirements_Document.md "null")
* [**System Flowchart & Legend**](https://www.google.com/search?q=System_Flowchart.md "null")

---

## Key Features

* **Dual-Agent Pipeline:** Utilizes a "Writer" agent to generate an initial draft and a separate "Editor" agent to refine, humanize, and improve the final output.
* **Multi-Provider Support:** Easily configure the application to use different LLMs for the writer and editor roles. Supports cloud-based models (Gemini) and locally-hosted models (Ollama, LM Studio).
* **Context-Aware Generation:** Can scrape a product's URL to gather real-time product information and analyze past reviews to generate new reviews that are consistent in tone and style.
* **Simple CLI Interface:** A straightforward menu-driven interface for writing reviews, listing past reviews, and managing settings.
* **Configurable & Extensible:** All settings, including API keys and model endpoints, are managed in a simple `config.json` file.

---

## How It Works

The application operates on a sophisticated, agent-based pipeline architecture, from user input to final review generation. The core of the system is the AI pipeline, which processes user notes and external data through a sequence of specialized agents. For a detailed explanation, please see the PRD.

### Application Flowchart

The following diagram illustrates the complete workflow of the application.

---

## Setup and Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/ai-review-assistant.git](https://github.com/your-username/ai-review-assistant.git)
    cd ai-review-assistant
    ```
2.  **Create a Python Environment:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install Dependencies:**
    You will need to install the required Python libraries. Create a `requirements.txt` file with the following content:
    ```text
    google-generativeai
    ```
    Then, install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: This project assumes you have a separate `fetcher.py` script for URL scraping, which may have its own dependencies like `BeautifulSoup` or `requests`.)*

4.  **Configure the Application:**
    When you first run the application, a `config.json` file will be created automatically. Open this file and edit it to select your desired LLM providers and add your API keys.

---

## Usage

1.  **Run the Application:**
    From the root directory, run the main script:
    ```bash
    python main.py
    ```
2.  **Use the Menu:**
    * **1. Write a new review:** Provide a product name, rating, and notes to generate a review using the standard pipeline.
    * **2. Write a new review with product context:** Provide a product URL in addition to your notes to generate a more detailed and context-aware review.
    * **3. List past reviews:** View a list of all reviews you have saved in the `reviews/` directory.
    * **4. Settings:** Configure which LLM provider to use for the "Writer" and "Editor" agents and enter your Gemini API key.
    * **5. Exit:** Close the application.

---

## Configuration

The `config.json` file is the control center for the AI pipeline.

```json
{
  "pipeline": {
    "writer_provider": "gemini",
    "editor_provider": "lmstudio"
  },
  "providers": {
    "gemini": {
      "api_key": "YOUR_API_KEY_HERE"
    },
    "ollama": {
      "endpoint": "http://localhost:11434/api/generate"
    },
    "lmstudio": {
      "endpoint": "http://localhost:1234/v1/chat/completions"
    }
  }
}
```
* **`writer_provider` / `editor_provider`:** Can be set to `"gemini"`, `"ollama"`, or `"lmstudio"`.
* **`api_key`:** If using Gemini, you must replace `"YOUR_API_KEY_HERE"` with your actual Google AI Studio API key.
* **`endpoint`:** Ensure the endpoints for Ollama or LM Studio match your local server configuration.

---

## Future Roadmap

Based on the Product Requirements Document, planned future enhancements include:

* **Internalize Web Scraping:** Integrate the `fetcher.py` logic directly into the application.
* **"Fact-Checker" Agent:** Add a third agent to the pipeline to verify the generated review against the scraped product data.
* **Tone & Sentiment Control:** Allow users to specify the desired tone (e.g., enthusiastic, critical) of the review.
* **Batch Generation:** Enable review generation for a list of products from a CSV file.
* **GUI/Web Interface:** Develop a graphical or web-based user interface for broader accessibility.

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.
