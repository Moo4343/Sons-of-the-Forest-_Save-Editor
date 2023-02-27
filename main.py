# sons of the forest save editor
# GameSetupSaveData.json --> Difficulty
# GameStateSaveData.json --> days
"""
Game Type
Is Roby(Kelvin) dead    bool
is Virginia dead        bool
CoreGameCompleted       bool
Escpaed Island          bool
Stayed on island        bool    
crash site              Array (tree und irgendweche aunderen spawnplatz)
"""

from __future__ import annotations      #variable annotation

file = R"C:\Users\Moritz\AppData\LocalLow\Endnight\SonsOfTheForest\Saves\76561199089779336\Multiplayer\0299148033\GameStateSaveData.json"

print("this is sons of the forest save editor")

with open(file,"r") as file:
    text=file.readlines()

print(text)
print("choose what you want to edit")
print("1 is kelvin dead")
print("2 is Virginia dead")
print("3 CoreGameCompleted ")
print("4 Escpaed Island")

input:str = input("what number do you use")

print(type(input))
print(input)
def getselected(input):
    switcher = {
        1: "zero",
        2: "one",
        3: "three",
        4: "four",
    }
    return switcher.get(int(input), "please choose the numbers above")


print(getselected(input))