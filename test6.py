{"employess":[
    {"firstName": "John", "lastName":"Doe"},
    {"firstName": "Anna", "lastName":"Smith"},
    {"firstName": "Peter", "lastName":"Jones"}
]}

import json



with open ("json_example.json","r",encoding = "utf8")as f:
    contents = f.read()
    json_data = json.loads(contents)
    print(json_data["employees"])