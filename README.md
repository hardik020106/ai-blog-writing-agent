# ✍️ AI Blog Writing Agent

An advanced AI-powered Blog Writing Agent built using **LangGraph**, **LangChain**, **Streamlit**, and **Tavily Search API**.

This project generates complete, SEO-optimized, human-like blogs using a multi-stage AI workflow architecture.

---

# 🚀 Features

✅ AI-Powered Blog Generation
✅ LangGraph Workflow Orchestration
✅ Tavily Web Research Integration
✅ Structured Outputs using Pydantic
✅ SEO Optimization
✅ Humanized Final Editing
✅ Streamlit ChatGPT-Style Interface
✅ Modular Node-Based Architecture
✅ Markdown Blog Rendering
✅ Professional Project Structure

---

# 🧠 Tech Stack

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Core Programming Language |
| LangChain  | LLM Integration           |
| LangGraph  | AI Workflow Orchestration |
| Streamlit  | Frontend UI               |
| Tavily API | Web Research              |
| Pydantic   | Structured Outputs        |
| MistralAI API | LLM Generation            |
| Rich       | Terminal UI Rendering     |

---

# 🏗️ Project Architecture

```text
User Topic
    ↓
Research Node
    ↓
Outline Node
    ↓
Writer Node
    ↓
SEO Writer Node
    ↓
Editor Node
    ↓
Final Blog
```

---

# ⚙️ Workflow Explanation

## 1. Research Node

* Uses Tavily Search API
* Collects relevant web information
* Generates structured research summary
* Extracts:

  * Key Points
  * Trends
  * Statistics

---

## 2. Outline Node

* Creates blog structure
* Generates:

  * Blog Title
  * Sections
  * Introduction Flow
  * Conclusion Flow

---

## 3. Writer Node

* Generates complete blog content
* Uses research + outline context
* Produces human-like article flow

---

## 4. SEO Writer Node

* Optimizes blog for SEO
* Adds:

  * SEO title
  * Meta description
  * Keywords
  * Better readability

---

## 5. Editor Node

* Humanizes final article
* Improves:

  * Readability
  * Tone
  * Flow
  * Formatting

---

# 📂 Project Structure

```text
Blog_Writing_Agent/
│
├── app/
│   ├── api/
│   ├── core/
│   │   └── llm.py
│   │
│   ├── graph/
│   │   └── blog_graph.py
│   │
│   ├── nodes/
│   │   ├── research_node.py
│   │   ├── outline_node.py
│   │   ├── writer_node.py
│   │   ├── SEO_writer_node.py
│   │   └── editor_node.py
│   │
│   ├── prompts/
│   │   ├── research_prompt.py
│   │   ├── outline_prompt.py
│   │   ├── writer_prompt.py
│   │   └── seo_prompt.py
│   │
│   ├── schemas/
│   │   ├── research_schema.py
│   │   ├── outline_schema.py
│   │   ├── blog_schema.py
│   │   ├── seo_schema.py
│   │   └── editor_schema.py
│   │
│   └── state/
│       └── blog_state.py
│
├── outputs/
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

# 🔑 Environment Variables

Create a `.env` file in project root.

```env
MISTRALAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

# 📦 Installation

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-blog-writing-agent.git
```

---

## 2. Move into Project

```bash
cd ai-blog-writing-agent
```

---

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 5. Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Streamlit App

```bash
streamlit run streamlit.py
```

---

# 🌐 Streamlit Interface

The application provides:

* ChatGPT-style UI
* Topic-based blog generation
* Real-time AI workflow execution
* Beautiful markdown rendering

---

# 🧩 Key Concepts Used

This project demonstrates several important AI Engineering concepts:

* LangGraph State Management
* Multi-Node AI Workflows
* Prompt Engineering
* Structured Outputs
* Schema Validation
* AI Workflow Orchestration
* SEO Optimization Pipelines
* Streamlit Frontend Integration
* Modular AI Architecture

---

# 📈 Future Improvements

Planned upgrades:

* FastAPI Backend
* Real-time Token Streaming
* Multi-Agent Collaboration
* Vector Database Integration
* RAG Architecture
* Blog History Database
* Authentication System
* Cloud Deployment

---

# 💡 Learning Outcome

This project was built as a practical implementation to deeply understand:

* LangGraph
* LangChain
* AI Workflow Engineering
* Structured AI Pipelines
* Modern AI Application Architecture

---

# 🤝 Contributing

Pull requests and suggestions are welcome.

---

# 📜 License

This project is open-source and available under the MIT License.

---

# ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
