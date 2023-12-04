# Both the Pytest and Mocking is getting reviewed in this file
from visualising_code.services import get_todos
from unittest.mock import Mock, patch
import requests
import pytest
mk = Mock()

def add(t):
    return 50 + t

# result = add(mk)

print(mk.add())

print(mk.value)

# mk.assert_called()
@pytest.mark.skip
def test_json():
    json = Mock()  # 

    json.loads('{"key":"val"}').get('k')

    json.loads.assert_called()
    json.loads.assert_called_once()
    json.loads.assert_called_with('{"key":"val"}')

    print(json.loads.call_args)

    print(json.method_calls)

''' Pytest follows the Arrange-Act-Assert model
Arrange, or set up, the conditions for the test
Act by calling some function or method
Assert that some end condition is true
'''

@pytest.mark.skip
def test_pass():
    assert True

@pytest.mark.skip
def test_fail():
    assert False

# Some more assertions
@pytest.mark.skip
def test_upper():
    assert "load heavy".upper() == 'LOAD HEAVY'

@pytest.mark.skip
def test_reverse():
    assert list(reversed([5, 4, 3, 2, 1])) == [1, 2, 3, 4, 5]

@pytest.mark.skip
def test_primes():
    assert 37 in {
        num for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }

''' Test Doubles and other vocabs
Test stub — used for providing the tested code with "indirect input".
Mock object — used for verifying "indirect output" of the tested code, by first defining the expectations before the tested code is executed.
Test spy — used for verifying "indirect output" of the tested code, by asserting the expectations afterwards, without having defined the expectations before the tested code is executed. It helps in recording information about the indirect object created.
Fake object — used as a simpler implementation, e.g. using an in-memory database in the tests instead of doing real database access.
Dummy object — used when a parameter is needed for the tested method but without actually needing to use the parameter.

Pytest leads you toward explicit dependency declarations that are still reusable thanks to the availability of fixtures. 
pytest fixtures are functions that can create data, test doubles, or initialize system state for the test suite.
'''
import pytest
from typing import List, Dict

@pytest.fixture
def example_fixture():
    return 1

@pytest.mark.skip
def test_with_fixture(example_fixture):
    assert example_fixture == 1

# TDD format function declaration

def format_data_display(people: List[Dict[str, str]]):
    """implement the function to meet the below test"""
    return [
        "Alfonso Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager"
    ]


@pytest.mark.skip
def test_format_data_display():
    people = [
        {
            'name': 'Alpaca',
            'last_name': 'Llama',
            'title': 'lang model'
        },
        {
            'name': 'Mistal',
            'last_name': 'GPT',
            'title': 'multi-modal model'
        }
    ]
    assert format_data_display(people) == [
        "Alfonso Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager"
    ]

@pytest.mark.skip
def test_dicts():
    # Learnt the 
    d1 = {0: 'a',
          1: 'b',
          2: 'c'}
    d2 = {2: 'c',
          1: 'b',
          0: 'a'}

    assert d1 == d2

@pytest.fixture
def example_people_data(): 
    # This function places the data inside any of the 
    # function that is being tested
    return [
            {
                'name': 'Alpaca',
                'last_name': 'Llama',
                'title': 'lang model'
            },
            {
                'name': 'Mistal',
                'last_name': 'GPT',
                'title': 'multi-modal model'
            }
        ]
#  you may find that fixtures in two separate files, or modules, share a common dependency. In this case, you can move fixtures from test modules into more general fixture-related modules. That way, you can import them back into any test modules that need them. This is a good approach when you find yourself using a fixture repeatedly throughout your project.

@pytest.mark.skip
def test_with_fixture(example_people_data):
    assert format_data_display(example_people_data) == [
        "Alfonso Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager"
    ]

@pytest.mark.skip
def test_request_response():
    response = requests.get("http://jsonplaceholder.typicode.com/todos")
    assert response.status_code == 200

@pytest.mark.skip
def test_request_response():
    # raise a request
    resp = get_todos()
    # recieve a response, and test whether this test is running first
    assert resp is not None

@pytest.mark.skip
@patch('visualising_code.services.requests.get')
def test_getting_todos_mock(mock_get):
    # configure mock to respond with OK stat code
    mock_get.return_value.ok = True
    # call the service that sends request to server
    resp = get_todos()
    # resp has to be non none
    assert resp is not None
@pytest.mark.skip
def test_context_getting_todo_mock():
    with patch('visualising_code.services.requests.get') as mock_get:
        mock_get.return_value.ok = True
        resp = get_todos()
    assert resp is not None

'''
Use a decorator when all of the code in your test function body uses a mock.
Use a context manager when some of the code in your test function uses a mock and other code references the actual function.
Use a patcher when you need to explicitly start and stop mocking a function across multiple tests (e.g. the setUp() and tearDown() functions in a test class).
'''
'''
Remember how @patch() works: You provide it a path to the function you want to mock. The function is found, patch() creates a Mock object, and the real function is temporarily replaced with the mock. When get_todos() is called by the test, the function uses the mock_get the same way it would use the real get() method.
'''
@pytest.mark.skip
@patch('visualising_code.services.requests.get')
def test_getting_todos_when_response_ok(mock_get):
    todos = [{
        'userId': 1,
        'id': 1,
        'task': 'Get in line',
        'completed': False
    }]
    mock_get.return_value = Mock(ok=True)  # ok property is added to the Mock, as Response object has Ok property
    mock_get.return_value.json.return_value = todos  #  json() function is added, since response object has json() method
    resp = get_todos()
    assert resp.json() == todos

# Remember, when you mock a function, you are replacing the actual object with the mock, and you only have to worry about how the service function interacts with that mock.

from visualising_code.services import get_uncompleted_todos
@pytest.mark.skip
@patch('visualising_code.services.get_todos')
def test_when_todo_list(mock_get_todos):
    todo1 = {
        'userId': 1,
        'id': 2,
        'title': 'this is 1st todo',
        'completed': True
    }
    todo2 = {
        'userId': 2,
        'id': 3,
        'title': 'this is 2nd todo',
        'completed': False
    }
    mock_get_todos.return_value = Mock()
    mock_get_todos.return_value.json.return_value = [todo1, todo2]

    uncompleted_todos = get_uncompleted_todos()

    assert mock_get_todos.called == True

    assert uncompleted_todos == [todo2]

# The following strategy should be used to confirm that the data you are expecting from the server matches the data that you are testing. The goal here is to compare the data structure (e.g. the keys in an object) rather than the actual data.
from unittest import skipIf
# True or False below will decide whether test below it will executed or not
@skipIf(False, 'Skipping tests hitting real API...')
def test_integration_contract():
    actual = get_todos()
    actual_keys = actual.json().pop().keys()
    # now start context patch
    with patch('visualising_code.services.requests.get') as mock_get:
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = [{
            'userId':1,
            'id': 1,
            'title': 'got 1st todo',
            'completed': False
        }]
        mocked = get_todos()
        mocked_keys = mocked.json().pop().keys()
    
    assert list(mocked_keys) == list(actual_keys)
