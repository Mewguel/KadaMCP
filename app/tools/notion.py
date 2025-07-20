from notion_client import Client
from app.config import NOTION_TOKEN, NOTION_DATABASE_ID

notion = Client(auth=NOTION_TOKEN)


def parse_task_properties(props):
    print(f"completion: {props['Completion']}")
    return {
        'title': (
            props['Project name']['title'][0]['plain_text']
            if props['Project name']['title'] else ''
        ),
        'status': (
            props['Status']['status']['name']
            if props['Status']['status'] else ''
        ),
        'owner': (
            props['Owner']['people'][0]['name']
            if props['Owner']['people'] else ''
        ),
        'completion': (
            props['Completion']['rollup']['number']
            if props['Completion']['rollup']['type'] == 'number' else 0.0
        ),
        'dates': {
            'start': (
                props['Dates']['date']['start']
                if props['Dates']['date'] else ''
            ),
            'end': (
                props['Dates']['date']['end']
                if props['Dates']['date'] else ''
            ),
        },
        'blocked_by': (
            props['Blocked By']['relation'][0]['id']
            if props['Blocked By']['relation'] else None
        ),
        'priority': (
            props['Priority']['select']['name']
            if props['Priority']['select'] else ''
        ),
        'summary': (
            props['Summary']['rich_text'][0]['plain_text']
            if props['Summary']['rich_text'] else ''
        )
    }


def query_kanban_tasks():
    response = notion.databases.query(
        **{
            "database_id": NOTION_DATABASE_ID,
        }
    )
    tasks = []
    for result in response.get('results', []):
        props = result['properties']
        task_data = parse_task_properties(props)
        task_data['id'] = result['id']
        tasks.append(task_data)

    return tasks
