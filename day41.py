webSite = {"name": None , "url": None, "desc": None, "rating": None, }

for name, value in webSite.items():
    webSite[name] = input(f"{name}: ")

print()
def printDic():
    for name, value in webSite.items():
        print (f"{name}: {value}")

printDic()



