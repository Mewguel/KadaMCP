from fastapi import FastAPI
from app.tools.notion import query_kanban_tasks

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "MCP Kanban Server Running"}


@app.get("/kanban/tasks")
def get_kanban_tasks():
    return query_kanban_tasks()
