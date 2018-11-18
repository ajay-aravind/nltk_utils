import os

def deleteFiles(filesList):
    for file in filesList:
        try:
                os.remove(file)
        except FileNotFoundError:
            pass;