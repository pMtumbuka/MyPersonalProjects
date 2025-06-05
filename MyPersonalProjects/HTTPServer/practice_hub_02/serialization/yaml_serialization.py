import yaml

data = {
    'name': 'Alice', 
    'age': 30, 
    'city': 'Blantyre'
    }
    
yaml_string = yaml.dump(data)
print(data)
print(yaml_string)

data2 = {
    'name': 'Alice',
    'details': {
        'age': 30,
        'city': 'Blantyre',
        'skills': ['Python', 'YAML', 'AI']
    }
}

yaml_string2 = yaml.dump(data2)
print(data2)
print(yaml_string2)


'''
    pip install PyYAML
    
    Once installed, yaml provides functions like:

        yaml.dump() – Serializes Python objects to YAML strings.

        yaml.load() / yaml.safe_load() – Parses YAML strings into Python objects.
        
        yaml_string = yaml.dump(data)
        
            yaml.dump() converts the Python dictionary data into a YAML-formatted string.

            yaml_string now holds this string version.
    
    Security Warning

        yaml.load() is unsafe because it can execute arbitrary code.

        Use yaml.safe_load() for loading from untrusted sources:
        
            yaml.safe_load(yaml_string)

'''