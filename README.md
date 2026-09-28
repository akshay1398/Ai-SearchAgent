# 🔎 Autonomous Research Agent

A chat-based web research assistant built with **Streamlit**, **Agno**, **Groq**, and **Tavily**.

Ask a research question in natural language and the agent will:
1. Search the web using Tavily
2. Prefer authoritative, primary sources and de-duplicate results
3. Analyze the collected information
4. Return a structured report with: **Topic**, **Key Points**, **Important Findings**, **Sources**, and **Actionable Insights**

---

## Project Structure

```
.
├── app.py            # Streamlit chat UI (entry point)
├── tools.py          # Agent definition (Agno + Groq + Tavily tools)
├── requirements.txt  # Python dependencies
├── .env.example      # Template for API keys (copy to .env)
└── .env              # API keys (you create this — never commit it)
```

---

## Requirements

- Python **3.10+**
- API keys for:
  - [Groq](https://console.groq.com/keys) — powers the LLM (`openai/gpt-oss-120b`)
  - [Tavily](https://app.tavily.com/) — powers web search

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/akshay1398/Ai-SearchAgent.git
cd Ai-SearchAgent
```

### 2. (Recommended) Create a virtual environment

```bash
python -m venv venv

# Windows (PowerShell)
venv\Scripts\Activate.ps1

# Windows (Git Bash)
source venv/Scripts/activate

# macOS / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Copy the provided template and fill in your keys (or create a file named `.env` in the project root manually):

```bash
cp .env.example .env
```

```env
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

The app loads these automatically via `python-dotenv` at runtime — no need to export them manually. The `.env` file is git-ignored and will never be committed.

> **Where to get the keys**
> - Groq: https://console.groq.com/keys (free tier available)
> - Tavily: https://app.tavily.com/ (free tier available)

### 5. Run the app

```bash
streamlit run app.py
```

Streamlit will start a local server and open the app in your browser (usually at `http://localhost:8501`). Type a research question in the chat box and press Enter — the agent will search the web and reply with a structured report.

---

## Usage Tips

- Be specific in your query, e.g. *"Compare the latest energy density figures for LFP vs NMC batteries from 2025 sources"* instead of just *"batteries"*.
- Reports follow a fixed 5-section format, so you can ask targeted follow-ups in the same chat session.
- The agent is instructed not to invent facts or sources; if evidence is insufficient, it will say so explicitly.

---

## Configuration Notes

| Setting | Where | Default |
|---|---|---|
| LLM model | `tools.py` | `openai/gpt-oss-120b` (Groq) |
| Web search tool | `tools.py` | Tavily |
| Debug mode | `tools.py` | `True` (set to `False` for quieter console output) |

---

## Troubleshooting

| Problem | Likely cause / fix |
|---|---|
| `KeyError: 'GROQ_API_KEY'` or auth errors | `.env` file is missing or keys are misnamed. Check spelling and that `.env` is in the project root. |
| Search returns nothing | `TAVILY_API_KEY` missing/invalid, or free-tier quota exhausted. |
| Slow or rate-limited responses | Free-tier limits on Groq/Tavily; wait and retry. |
| `streamlit: command not found` | Activate your virtual environment, or run `python -m streamlit run app.py`. |

---

## Repository

https://github.com/akshay1398/Ai-SearchAgent
