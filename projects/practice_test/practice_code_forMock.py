from unittest.mock import Mock
import requests
def json_list(qty: int):
    # if qty is 0, then return empty
    if qty == 0:
        return []
    # else return a list with single json
    data = []

    for x in range(qty):
        data.append({'quantity': x,
                     'items': [f'items_{x}']})

    return data


def add(a: int, b: int) -> int:
    return a + b


def subt(a: int, b: int) -> int:
    return a - b


class Calculator:
    def __init__(self, val1: int, val2: int, ops: str):
        self.a = val1
        self.b = val2
        self.oper = ops

    def add(self):
        return self.a + self.b

    def subt(self):
        return self.a - self.b

    def __str__(self):
        if self.oper == 'sub':
            return f"Difference of {self.a} and {self.b} is {self.subt()}"
        if self.oper == 'add':
            return f"Difference of {self.a} and {self.b} is {self.add()}"


def other_comments():
    url = "https://jsonplaceholder.typicode.com/comments/17/"
    resp = requests.get(url)
    return resp.json()
