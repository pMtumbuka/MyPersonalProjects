import json

data = {
    'name': 'Alice', 
    'age': 30, 
    'city': 'Blantyre'
    }
    
json_string = json.dumps(data)
print(json_string)

data2 = {
    'name': 'Alice',
    'details': {
        'age': 30,
        'city': 'Blantyre',
        'skills': ['Python', 'YAML', 'AI']
    }
}

json_string2 = json.dumps(data2)
print(data2)
print(json_string2)

'''

The json module provides functions for converting between Python objects and JSON (JavaScript Object Notation) strings.
   
    json.dumps() – Converts Python objects to JSON strings.

    json.loads() – Converts JSON strings back into Python objects.

    json.dump() / json.load() – Used for working directly with files.
    
    json_string = json.dumps(data)
    
    json.dumps() means "dump to string".

        Converts the Python dictionary data into a JSON-formatted string.
   
'''
