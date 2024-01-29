import json

def get(menu_name, text_name):
    with open("locales/en.json","r") as file:
        jsonfile = file.read()
        loaded = json.loads(jsonfile)

