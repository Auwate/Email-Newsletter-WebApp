class Map:
    def __init__(self):
        self.map = {}


def add(storageObject, email, name, preference):
    storageObject.map.update({email:[name,preference]})


def get(storageObject, email):
    return storageObject.map.get(email)


def keyList(storageObject):
    return list(storageObject.map.keys())