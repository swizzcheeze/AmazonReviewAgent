
# Product Requirements Document: AI-Powered Review Agent

**Author:** Gemini
**Version:** 1.0
**Date:** 2025-08-30

---

## 1. Product Vision & Market Opportunity

### 1.1. Product Vision

To create a powerful, flexible, and efficient tool that automates the generation of high-quality, context-aware, and authentic-sounding product reviews. The "AI-Powered Review Agent" will empower users to produce compelling review content at scale, leveraging a sophisticated, multi-provider AI pipeline that supports both cloud-based and local large language models (LLMs).

### 1.2. Market Opportunity

The target market consists of:

*   **E-commerce Sellers & Brands:** Businesses that need to populate their product pages with initial reviews or generate marketing copy based on product features.
*   **Affiliate Marketers & Bloggers:** Content creators who write product review articles and need to generate descriptive text quickly.
*   **Product Managers & Marketers:** Teams that want to synthesize product information and existing feedback into user-friendly summaries or new review content.

The key market differentiator is the **hybrid AI approach**. By supporting both powerful cloud APIs (like Gemini) and private, cost-effective local models (via Ollama and LM Studio), the tool caters to a wide range of users, from those who need the highest quality generation to those who prioritize privacy, security, and cost control.

---

## 2. Technical Architecture

The system is designed as a modular, command-line Python application with a clear separation of concerns.

### 2.1. High-Level Architecture

The application follows an **agent-based pipeline architecture**. A central `main.py` script orchestrates a sequence of specialized agents to achieve the final output.

1.  **User Input (CLI):** The user initiates a task through a menu in `main.py`.
2.  **Configuration (`config.json`):** All operations are guided by a central configuration file that defines which AI provider to use for each step of the pipeline and stores necessary API keys and endpoints.
3.  **Context Gathering (`product_agent.py`):** For context-aware tasks, this agent is invoked to fetch external data. It scrapes product information from a URL (via an external `fetcher.py` script) and scans the local `reviews/` directory for historical context.
4.  **AI Pipeline (`llm_integration.py`):** This is the core of the system.
    *   **Writer Agent:** The first LLM call generates a draft review based on the initial prompt and any context provided by the `product_agent`.
    *   **Editor Agent:** The draft is passed to a second LLM, which is prompted to "humanize," edit, and refine the text to improve its natural language and engagement.
5.  **Output Management (`review_manager.py`):** The final, edited review content is saved to a sanitized `.txt` file in the `reviews/` directory for persistence and later use.

### 2.2. Key Components

*   **`main.py`:** The user-facing CLI and application orchestrator.
*   **`llm_integration.py`:** Manages all interactions with the various LLM providers. It abstracts the specific API calls for Gemini, Ollama, and LM Studio into a generic `get_llm_response` function.
*   **`product_agent.py`:** Responsible for fetching and consolidating all contextual information (product data, past reviews) to enrich the AI prompts.
*   **`review_manager.py`:** Handles all file system operations, primarily the saving and listing of generated reviews.
*   **`config.json`:** A critical file that makes the system flexible, allowing users to easily swap out AI providers without changing the code.
*   **`fetcher.py` (External Dependency):** An assumed external script responsible for web scraping product data from a URL. This is a potential point of failure and a key dependency.

---

## 3. Core Features & User Journey

### 3.1. Core Features

*   **Multi-Provider AI Pipeline:** Supports Gemini (cloud), Ollama (local), and LM Studio (local) for review generation.
*   **Configurable Agent Roles:** Users can assign different AI providers to the "Writer" and "Editor" roles in the pipeline.
*   **Standard Review Generation:** Create a review based on a product name, star rating, and key points.
*   **Context-Aware Review Generation:** Create a review by providing a product URL, which automatically scrapes product info and references past reviews for richer context.
*   **Local Storage:** All generated reviews are saved with a timestamp and sanitized product name for easy access.
*   **CLI-Based Management:** All features are accessible through an interactive command-line interface.
*   **Settings Management:** Users can easily view and update their AI provider settings and API keys.

### 3.2. User Journey

1.  **Launch:** The user runs `python main.py` from their terminal.
2.  **Menu Selection:** The user is presented with a menu: "Write a new review," "Write with product context," "List past reviews," "Settings," or "Exit."
3.  **Configuration (First-time user):** The user selects "Settings" to choose their desired AI providers for the Writer and Editor agents and enters their Gemini API key if applicable.
4.  **Review Generation:**
    *   The user selects one of the "Write" options.
    *   They are prompted to enter product details (name, rating, notes, and URL if applicable).
    *   The application shows status updates as it calls the Writer and Editor agents.
5.  **Output:**
    *   The final, polished review is printed directly to the console for immediate use.
    *   A message confirms that the review has been saved to a file in the `reviews/` directory.
6.  **Review History:** The user can select "List past reviews" to see all the files they have generated.

---

## 4. Competitive Analysis

| Competitor | Strengths | Weaknesses | Our Advantage |
| :--- | :--- | :--- | :--- |
| **General AI Chatbots (ChatGPT, Gemini UI)** | High-quality output, versatile, easy to use. | Not specialized for reviews, requires manual prompt engineering, potential privacy concerns with sensitive product data. | **Specialized Workflow:** Our Writer->Editor pipeline is optimized for the review format. **Privacy & Cost:** Local LLM support via Ollama/LM Studio addresses privacy and reduces API costs. |
| **Automated Content Spinners** | Fast, cheap, high volume. | Very low quality, often unreadable, easily detected as spam, produces poor SEO results. | **Quality & Authenticity:** We leverage advanced LLMs to produce content that is designed to be natural and engaging, not just spun. |
| **Dedicated AI Writing Tools (Jasper, Copy.ai)** | High-quality, many templates, good UI. | Subscription-based (expensive), primarily cloud-based, may lack deep customization. | **Flexibility & Control:** Our open, code-first approach allows for deep customization. The ability to use local models provides an unparalleled level of control and cost-effectiveness. |

---

## 5. Implementation Roadmap

### Phase 1: Current State (v1.0)

*   Fully functional CLI application.
*   Writer->Editor pipeline with configurable Gemini, Ollama, and LM Studio providers.
*   Context-gathering from product URLs and past reviews.
*   Local file-based storage of reviews.

### Phase 2: Enhancements (v1.5)

*   **Internalize `fetcher.py`:** Integrate the web scraping logic directly into the `product_agent.py` using libraries like `BeautifulSoup` and `requests` to remove the external script dependency.
*   **Add a "Fact-Checker" Agent:** Introduce a third step in the pipeline where an LLM is prompted to verify that the generated review content aligns with the scraped product information.
*   **Sentiment & Tone Control:** Allow the user to specify a desired tone (e.g., "enthusiastic," "critical," "neutral") or sentiment as part of the initial prompt.
*   **Batch Generation:** Create a feature to read a list of products (e.g., from a CSV file) and generate reviews for all of them in a single run.

### Phase 3: Expansion (v2.0)

*   **GUI/Web Interface:** Build a graphical user interface using a framework like Tkinter, or a simple web UI with Flask/FastAPI, to make the tool more accessible to non-technical users.
*   **Direct Integration (Cautionary):** Explore (with strong warnings about Terms of Service) the possibility of using browser automation tools like Selenium to post the generated review directly to a website.
*   **Performance Analytics:** Track metrics like generation time and token usage for each provider to help users optimize their setup.
*   **Advanced Context Management:** Instead of just reading all past reviews, use vector embeddings to find the most semantically similar past reviews to use as context.

---

## 6. Success Metrics

### 6.1. Technical Metrics

*   **Generation Speed:** Average time from prompt input to final review output, measured per provider.
*   **API Success Rate:** Percentage of successful LLM API calls vs. errors.
*   **Provider Adoption:** Track which providers are most commonly used for the Writer and Editor roles.

### 6.2. User & Business Metrics

*   **Reviews Generated:** Total number of reviews created over time.
*   **Feature Usage:** Frequency of use for "Standard Review" vs. "Context-Aware Review."
*   **Quality of Output (Qualitative):** User satisfaction with the final review's coherence, authenticity, and engagement. This can be measured through user surveys or feedback sessions.
*   **User Retention:** Rate at which users continue to use the tool over time (for a deployed application).
