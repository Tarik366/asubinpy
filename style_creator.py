import json

def create_css():
    with open("style/style.json","r") as file:
        jsonfile = file.read()
        loaded = json.loads(jsonfile)

    cssItem = ""
    for item in loaded:
        classItem = ""
        loadItem = loaded[item]
        for itemStyle in loadItem:
            classItem += f"\t{itemStyle}: {loadItem[itemStyle]};\n"
        css = f"{item} {{ \n{classItem}}}\n"
        cssItem += css
    with open("style/style.css", "w") as cssFile:
        cssFile.write(cssItem)
