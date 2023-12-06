# Practicing Mock objects and testing using them

from unittest.mock import Mock, patch 
import requests
from requests import get

json = Mock()

json.loads('{"key":"value"}')

assert json.loads.called == True

json.loads.assert_called_once()


def todos():
    resp = get("http://jsonserver/todos")
    data = resp.json()
    return data
# the function declared by user is mocked
# todos = Mock()  # Entire function is being mocked

td1 = {
    "user":1,
    "id": 'athe1',
    'task': 'testing mock'
}

# todos.return_value = td1

# this is giving mocked data
# got_data = todos()

# todos.assert_called_once()

# print(got_data)

# another way is to mock the functions imported
get = Mock()
get.return_value.ok = True
get.return_value.json.return_value = td1

another = todos()

print(another)

get.assert_called()

assert get.call_count == 1


