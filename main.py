import sys
import URL, search
import urllib.request, urllib.parse

#Used to search videos
url = "https://www.youtube.com/results?search_query="

#Conditional Boolean Loop
validInput = False

#Used to clear Command Line screen before execution
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')

#Title Screen
print("Welcome to YouPy!")
print()
print("[1]: Download via URL")
print("[2]: Search via Title")
print("[3]: Download Playlist")
print("[4]: Exit Program")
print()

#Control Sequence
while not validInput:
    try:
        userInput = input("Select Option: ")
        if userInput == "1":
            validInput = True
            URL.getURL()
            sys.exit()
        elif userInput == "2":
            validInput = True
            search.searchVideo()
            sys.exit()
        elif userInput == "3":
            validInput = True
            URL.downloadByPlaylist()
            sys.exit()
        elif userInput == "4":
            sys.exit()
        else:
            print("Invalid Entry! Try Again: ")
    except Exception as e:
        print(e)
        print("Invalid Entry! Try Again: ")
