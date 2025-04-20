# Analytics Vidhya Course Recommendation
This project suggests relevant courses from Analytics Vidhya based on the user's query. It uses an LLM to understand user intent and recommend courses accordingly.

## 🔍 How It Works

1. Scrapes course data (title, description, curriculum) from the Analytics Vidhya website.
2. Stores the course data locally.
3. Uses a Large Language Model (via Groq) to match user queries with the most relevant courses.
4. Provides an easy-to-use Gradio interface for users to ask questions and get personalized course suggestions.

## 🛠 Tech Stack

- Python 3.10
- Gradio – for building the UI
- Groq – for running LLM queries
- uv – for environment and dependency management

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/ravi46931/analyticsvidhya-course-recommender.git
cd analytics-vidhya-course-recommendation

# Install uv (high-performance Python package and environment manager )
pip install uv

# Set up virtual environment
uv venv

# Activate virtual environment (adjust for your OS)
# On Windows:
.\.venv\Scripts\activate

# On Unix or MacOS:
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
uv pip install -e .

# Scrape course data
uv run src\scrap\scrap.py
```

## 🔑 Environment Variables

Set your `Groq API` key as an environment variable:

```bash
export GROQ_API_KEY=your_api_key_here
```
or 
```bash
set GROQ_API_KEY=your_api_key_here
```

## 🚀 Running the App

```bash
uv run app.py
```
Then open the app in your browser and ask your question to get course recommendations!

## 🎥 Demo
![User Input & Its response](ui.png)

## 👤 Author
- Ravi Kumar