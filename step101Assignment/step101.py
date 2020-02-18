import os
import time


def findTxtFiles():
    # Get the current working directory.
    dirPath = os.getcwd()
    # This method returns an arbitrary list of all items in the specified directory.
    currentDir = os.listdir(dirPath)
    # This array is where I will push the text files.
    textFiles = []
    # Text files including absolute path.
    absPaths = []
    # This loop will find .txt files and add them to textFiles array!
    for x in currentDir:
        if x.endswith(".txt"):
            textFiles.append(x)
    for x in textFiles:
        full = os.path.join(dirPath, x)
        absPaths.append(full)
    return absPaths


def getTimeAndPrint():
    filePaths = findTxtFiles()
    for x in filePaths:
        epochTime = os.path.getmtime(x)
        epochTimeStr = str(epochTime)
        localTime = str(time.ctime(epochTime))
        phrase = x + " was last modified " + epochTimeStr + " seconds since the epoch. Convert to local time and the " \
                                                            "file was edited on " + localTime + "."
        print(phrase)


if __name__ == '__main__':
    getTimeAndPrint()

# Requirements:
# Your script will need to use Python 3 and the OS module.
#
# Your script will need to use the listdir() method from the OS module to iterate through all files within a specific
# directory.
#
# Your script will need to use the path.join() method from the OS module to concatenate the file name to its file
# path, forming an absolute path.
#
# Your script will need to use the getmtime() method from the OS module to find the latest date that each text file
# has been created or modified.
#
# Your script will need to print each file ending with a “.txt” file extension and its corresponding mtime to the
# console.
