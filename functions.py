import lists
import wikipedia
import webbrowser
from playsound import playsound

hau = lists.HAU
targets = lists.target
projects = lists.projects
villains = lists.villains
compliment: list = ["test", "test"]


def SearchWiki(statement):
    statement = statement.replace("wikipedia", "")
    statement = statement.replace("search", "")
    statement = statement.replace("who", "")
    statement = statement.replace("is", "")
    statement = statement.replace("for", "")
    results = wikipedia.summary(statement, sentences=3)
    return results


def OpenPage(page):
    webbrowser.open_new_tab(page)


def addTarget(ans):
    targets.sort()
    targets.append(ans)
    print("done.....")


def addProjects(ans):
    projects.sort()
    projects.append(ans)
    print("done.....")


def addVillains(ans):
    villains.sort()
    villains.append(ans)
    print("done.....")


#compliment_file = open("compliments.txt", "r")
#compliment = compliment_file.readlines()
# compliment_file.close
