"""
This list is not a pure coding challenge. There are important topics behind each project. For creating a JSON parser, the topic is recursion. There is a pattern that can be used to parse most computer languages, it is called recursive descent.

Many of the challenges on this list also require some parsing. So it is recommended that you start with this one.



Try to simplify the code when you are done. You probably learned about tokenizers or lexical analysis if you used a compiler book. These things are not necessary for something as simple as JSON, and they actually add more work.

Another reason this is worth doing: unlike most coding works, there is actually a precise specification to follow. Try to follow the JSON specification (https://datatracker.ietf.org/doc/html/rfc7159) to the letter, because it trains you to think and code rigorously.

Things to learn:

Recursive descent parsing.
Follow a specification rigorously.
"""

import json

def parse_json(json_string):
    """
    Parse a JSON string into a Python object.
    """
    # Remove whitespaces
    json_string = json_string.replace(" ", "")
    # Remove newlines
    json_string = json_string.replace("\n", "")
    # Remove tabs
    json_string = json_string.replace("\t", "")

    # Check if it is a number
    try:
        return int(json_string)
    except ValueError:
        pass

    # Check if it is a string
    if json_string[0] == '"' and json_string[-1] == '"':
        return json_string[1:-1]

    # Check if it is a list
    if json_string[0] == '[' and json_string[-1] == ']':
        result = []
        # Remove the brackets
        json_string = json_string[1:-1]
        # Split the string by commas
        json_list = json_string.split(",")
        for item in json_list:
            result.append(parse_json(item))
        return result

    # Check if it is a dictionary
    if json_string[0] == '{' and json_string[-1] == '}':
        result = {}
        # Remove the brackets
        json_string = json_string[1:-1]
        # Split the string by commas
        json_list = json_string.split(",")
        for item in json_list:
            # Split the item by colon
            key, value = item.split(":")
            key = key[1:-1]
            result[key] = parse_json(value)
        return result

    # Check if it is a boolean
    if json_string == "true":
        return True
    if json_string == "false":
        return False

    # Check if it is null
    if json_string == "null":
        return None

    # If it is none of the above, it is an invalid JSON string
    raise ValueError("Invalid JSON string")
    

def main():
    """
    Main function.
    """
    json_string = '{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}'
    print(parse_json(json_string)) 


if __name__ == "__main__":
    main()

