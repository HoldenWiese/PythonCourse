import os
import time


def getTimeAndPrint():
    dirPath = os.getcwd()
    currentDir = os.listdir(dirPath)
    for x in currentDir:
        if x.endswith(".txt"):
            full = os.path.join(dirPath, x)
            epochTime = os.path.getmtime(full)
            epochTimeStr = str(epochTime)
            localTime = str(time.ctime(epochTime))
            phrase = x + " was last modified " + epochTimeStr + "seconds since the epoch. Convert to local time and " \
                                                                "the file was edited on " + localTime + ".\n"
            print(phrase)


getTimeAndPrint()
