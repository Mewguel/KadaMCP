# MCP Kanban Server

AI-powered central server for Notion Kanban boards with Slack & dashboard integrations.

## Project Structure

```
app/
│
├── init.py
├── config.py # Loads env vars
│
├── main.py # FastAPI app
├── tools/
│ └── notion.py # Notion API interactions
│
.env # Secrets (Notion token, Database ID)
.gitignore
requirements.txt
```

## Setup Guide

1. **Clone Repository**

```bash
git clone <repo-url>
cd <repo-folder>
Create Virtual Environment
```

2. **Running the app**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows
Install Dependencies
pip install -r requirements.txt

```

3. **Add environment config**
   Create .env

```bash
NOTION_TOKEN=your_notion_token
NOTION_DATABASE_ID=your_database_id
```

4. **Run Server**

```bash
uvicorn app.main:app --reload
```

5. **Test**
   Visit: http://127.0.0.1:8000 → should return {"message": "MCP Kanban Server Running"}
