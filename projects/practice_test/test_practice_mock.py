import pytest
try:
    from .practice_code_forMock import json_list, add, subt, Calculator, other_comments
except ModuleNotFoundError:
    from projects.practice_test.practice_code_forMock import json_list, add, subt, Calculator, other_comments

from unittest.mock import Mock, patch


@pytest.mark.skip
def test_json_list():
    """Check for qty input of 0"""
    assert json_list(qty=0) == []

@pytest.mark.skip
def test_json_list_more_than_zero():
    """check for quantity more than 0, 
    should return a list that have elements 
    equal to quantity."""
    quantity = 1
    assert len(json_list(qty=quantity)) == quantity
    # check only one feature or parameter
    # assert json_list(qty=quantity) == [{}]


@pytest.mark.skip
def test_json_contains_key():
    """check if the json contains the 
    quantity and item keys are present
    in the returned data."""
    quantity = 1
    output = json_list(qty=quantity)
    assert 'quantity' in output[0]
    assert 'items' in output[0]


@pytest.mark.skip
def test_json_contains_values():
    """Check the values returned 
    in the data"""
    quantity = 1
    output = json_list(qty=quantity)
    assert output[0]['quantity'] == 0
    assert output[0]['items'] == ['items_0']


# mock json_list
json_list = Mock() # even if the function is Mock'ed here, all the rest of the functions becomes mocks
json_list.return_value = []
# json_list(qty=1).return_value = [{}]

@pytest.mark.skip
def test_json_list_mock():
    """Check for qty input of 0"""
    print(json_list.mock_calls)
    assert json_list(qty=0) == []
    # assert json_list.assert_called_once()


print(json_list(qty=0))
json_list.return_value = [{}]
print(json_list(qty=1))
json_list.return_value = [{}, {}]
print(json_list(qty=2))
print(json_list.mock_calls)
print(json_list.method_calls)

# there are many modules apart from requests, like sqlite3, 
# psycopg2, pandas, even pytorch or matrix-nio. Which have 
# their own functions and classes, which can be mocked.
# After lot of thinking decided to go with a simpler calculator 
# methods, and overarching class

Calculator = Mock()
# when mocking the Classes, the Class itself needs to be used, not the instance
Calculator.add.return_value = 5
Calculator.subt.return_value = -2

print(Calculator)
calc = Calculator()  # This wont work, as this is a different Mock object

print(calc)
print(calc.add(5, 8))  # Will return a Mock Object.. not vaulue
print(calc.subt(7, 3))

# the above commands create different mocks

# print(Calculator.add.assert_called_once())

Calculator.add(5, 6)
print(Calculator.add(5, 6))  # will print a value

# print(Calculator.add.assert_called_once())

print(Calculator.call_count)
print(Calculator.add.call_count)

print(Calculator.subt(5, 6))

print(Calculator.subt.call_count)

# Unintended consequences is the side-effect
Calculator.add.side_effect = TypeError

try:
    Calculator.add('8',5)

except TypeError as e:
    print('caught type error', e)

requests = Mock()  # this has to be along with the function that is using it

def get_conments():
    url = "https://jsonplaceholder.typicode.com/comments/12/"
    resp = requests.get(url)
    return resp.json()

resp_mock = Mock()
resp_mock.status_code = 205  # Usually its 200
resp_mock.json.return_value = {
  "postId": 22,
  "id": 110,
  "name": "sint est odit officiis similique aut corrupti quas autem",
  "email": "Cassidy@maribel.io",
  "body": "cum sequi in eligendi id eaque\ndolores accusamus dolorem eum est voluptatem quisquam tempore\nin voluptas enim voluptatem asperiores voluptatibus\neius quo quos quasi voluptas earum ut necessitatibus"     
}
requests.get.return_value = resp_mock
data = get_conments()
print(data)
print(requests.get.call_count)


@patch('practice_test.practice_code.requests')
def test_other_comments(req_patch):
    req_patch.get.return_value = resp_mock
    resp = other_comments()
    # print(resp.status_code)
    # print(resp.json())
    req_patch.get.assert_called_once()  # need to check correct mock attribute