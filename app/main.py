import os
saveDirectory = "saves"
roomDirectory = "rooms"

def getSaveFilePath(username):
    return saveDirectory + '/' + username + ".txt"

def getRoomFilePath(roomName):
    return roomDirectory + '/' + roomName + ".txt"

def cls():
    os.system('cls')

class Room:
    def __init__(self, id, text, options):
        self.id = id
        self.text = text
        self.options = options

def readRoom(roomName):
    f = open(getRoomFilePath(roomName), "r")
    line = f.readline().rstrip()
    fullText = ''
    while line != "---":
        fullText = fullText + line
        line = f.readline().rstrip()
    options = {}
    i = 1
    line = f.readline().rstrip()
    while line != "|-|":
        Id = f.readline().rstrip()
        options[str(i)] = Option(line, Id)
        line = f.readline().rstrip()
        i += 1
    room = Room(roomName, fullText, options)
    return room

def printroom(room):
           print("-----------")
           print(room.text)

class Option:
    def __init__(self, text, id):
        self.text = text
        self.id = id

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

class GameData:
    def __init__(self, room, health):
        self.room = room
        self.health = health

def printInstructions():
    cls()
    print("welcome to game test")
    introput = input("Press enter to continue: ")
    while introput != '':
        introput = input()
    cls()

def login():
    cls()
    return input('enter username: ')

def createDir():
    os.mkdir(saveDirectory)

def saveGameData(username, gameData):
    f = open(getSaveFilePath(username), "w")
    f.write(gameData.room)
    f.write("\n")
    f.write(str(gameData.health))
    f.write("\n")
    f.close

def loadGameData(username):
    f = open(getSaveFilePath(username), "r")
    room = f.readline().rstrip()
    health = int(f.readline().rstrip())
    gameData = GameData(room, health)
    f.close
    return gameData


def initGameData(username):
    if not os.path.exists(saveDirectory):
        createDir()
    if not os.path.exists(getSaveFilePath(username)):
        gameData = GameData("room-1", 100)
        saveGameData(username, gameData)
    else:
        gameData = loadGameData(username)
    return gameData

def playGame():
    username = login()
    gameData = initGameData(username)
    printInstructions()
    player = Player(username, gameData.health)
    currentRoomId = gameData.room
    currentRoom = readRoom(currentRoomId)
    while True:
        printroom(currentRoom)
        for key in currentRoom.options.values():
            print(key.text)
        print(player.name, "Health: " + str(player.health))
        input1 = input("Input: ")
        if input1 == 'q':
            saveGameData(username, GameData(currentRoom.id, player.health))
            cls()
            break
        currentRoom = readRoom(currentRoom.options[input1].id)
        cls()
playGame()