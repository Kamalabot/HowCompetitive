# Standard library imports...
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin

# Third-party imports...
import requests

# Local imports...
BASE_URL = "https://jsonplaceholder.typicode.com/"

TODOS_URL = urljoin(BASE_URL, 'todos')


def get_todos():
    response = requests.get(TODOS_URL)
    if response.ok:
        return response
    else:
        return None


def get_uncompleted_todos():
    resp = get_todos()
    if resp is None:
        return []
    else:
        todos = resp.json()
        return [todo for todo in todos if todo.get('completed') == False]
