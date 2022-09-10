import json
import lists 

data = {
    "Targets" : lists.target,
    "People" : lists.people,
    "Villains" : lists.villains,
    "Websites": lists.websites,
    "Eliminated": lists.elimated,
    "ToDo": lists.ToDo,
    "Projects": lists.projects,

}


filename = 'data.json' #use the file extension .json

#
def loadData(location = filename):
    file = open(location)

    data = json.load(file)
    file.close()
    return data

#
def saveData(data: data, location = filename):
    with open(location, 'w') as file_object:  #open the file in write mode
        json.dump(data, file_object)