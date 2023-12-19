#!/usr/bin/python
# Explore how the json files can be read from and written to in a single 
# execution, after doing some processing.
import json

raw_json = [
    {
      "ID": 1,
      "Name": "Object 1",
      "Description": "Description for Object 1"
    },
    {
      "ID": 2,
      "Name": "Object 2",
      "Description": "Description for Object 2"
    },
    {
      "ID": 3,
      "Name": "Object 3",
      "Description": "Description for Object 3"
    },
    {
      "ID": 4,
      "Name": "Object 4",
      "Description": "Description for Object 4"
    },
    {
      "ID": 5,
      "Name": "Object 5",
      "Description": "Description for Object 5"
    },
    {
      "ID": 6,
      "Name": "Object 6",
      "Description": "Description for Object 6"
    },
    {
      "ID": 7,
      "Name": "Object 7",
      "Description": "Description for Object 7"
    },
    {
      "ID": 8,
      "Name": "Object 8",
      "Description": "Description for Object 8"
    },
    {
      "ID": 9,
      "Name": "Object 9",
      "Description": "Description for Object 9"
    },
    {
      "ID": 10,
      "Name": "Object 10",
      "Description": "Description for Object 10"
    }
  ]

file_name = 'test_write.json'

with open(file=file_name, mode='r') as reader:
    # if the file is empty, for the first read
    if reader.read() == '':
        # create a empty data list
        data_list = []
    else:
        print(reader.read())
        # file is having data, then load it
        data_list = json.load(reader.read())

for ind, obj in enumerate(raw_json):
    obj['description_length'] = len(obj['Description'])
    data_list.append(obj)
    print(f'dumping {ind} object')

    with open(file=file_name, mode='w', encoding='utf-8') as writer:
        json.dump(data_list, writer)

print(f'all writes complete, check {file_name}.')
