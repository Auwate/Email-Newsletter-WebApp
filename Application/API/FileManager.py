import json

'''
    save_to_file: A function that takes two variables, data and
    file_name, and saves that data to a file. If the file is not
    present already, it will create the file.

    data -> A file that contains json data

    file_name -> A file location and its name. After saving, it
    will contain json values.
'''


def save_to_file(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=2)
    print("Successfully saved.\n")


'''
    read_from_file: A function that takes one variable,
    file_name, and reads the json data from the file.
    
    file_name -> A file location and its name. It contains json
    values.
'''


def read_from_file (file_name):
    with open(file_name, 'r') as file:
        jsonFile = json.load(file)
    print("Successfully read.\n")
    return jsonFile