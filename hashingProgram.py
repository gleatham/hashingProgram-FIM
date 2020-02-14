import os
import hashlib

'''
Receives a dictionary of directories.
Iterates through the dictionary creating a hash for each value and writes it to a new dictionary
with a matching key. 
'''
def createHash(directory, numDirectories):
    newHash = {}
    directory = directory
    numDirectories = numDirectories
    #directory = 'C:\\Users\\Geoff\\Documents\\hashTest'
    keys = []
    keys = list(directory.keys())

    count = 0
    while(count < numDirectories):
        tempDir = directory.get(keys[count])
        SHAhash = hashlib.md5()
        #print("Hashing: ", tempDir)
        try:
            for root, dirs, files in os.walk(tempDir):
                for names in files:
                    filepath = os.path.join(root, names)
                    try:
                        fin = open(filepath, 'rb')
                    except:
                        print("Unable to open file")
                        fin.close()
                        continue

                    var = True
                    while var:
                        # Read file in chunks
                        buf = fin.read(4096)
                        if not buf:
                            break
                        #SHAhash.update(hashlib.md5(buf).hexdigest())
                        SHAhash.update(hashlib.md5(buf).digest())

                    fin.close()

        except:
            print("Hashing failed")
            import traceback
            traceback.print_exc(limit=None, file=None, chain=True)
            return -2
        newHash.update({keys[count]: SHAhash})
        count+=1

    return newHash


'''
Reads in a directory path from a file.
Directory path is used in createHash()
'''
def getDirectory():
    directories = {}

    try:
        with open('C:\\Users\\Geoff\\Documents\\hashTest\\directories.txt') as fin:
            directoriesList = fin.readlines()
            numDirectories = len(directoriesList)

            counter = 0
            while(counter < numDirectories):
                tempDirList = directoriesList[counter].split(':', 3)

                directories.update({tempDirList[0]: tempDirList[1]})

                counter+=1
    except:
        print("getDirectory() failed")
        import traceback
        traceback.print_exc(limit=None, file=None, chain=True)
        return -2

    return directories


'''
Reads file to get keys and hashes
'''
def getHashes():
    hashes = {}
    try:
        with open('C:\\Users\\Geoff\\Documents\\hashTest\\directories.txt') as fin:
            hashesList = fin.readlines()
            numDirectories = len(hashesList)

            counter = 0
            while(counter < numDirectories):
                tempHashList = hashesList[counter].split(':', 3)

                hashes.update({tempHashList[0]: tempHashList[2]})

                counter+=1
    except:
        print("getHashes() Failed")
        import traceback
        traceback.print_exc(limit=None, file=None, chain=True)
        return -2
    return hashes


'''
Receives two dictionaries and compares hashes based on matching keys
Returns dictionary with the same key as all the other dicts
If the hashes match the value is True else False
'''
def compareHash(hashes, newHash, numDirectories):
    hashes = hashes
    newHash = newHash
    numDirectories = numDirectories
    keys = list(hashes.keys())

    compareResults = {}

    count = 0
    while(count < numDirectories):
        hashOne = hashes.get(keys[count])
        hashTwo = newHash.get(keys[count]).hexdigest()

        if(hashOne == str(hashTwo)):
            compareResults.update({keys[count]: True})
        else:
            compareResults.update({keys[count]: False})

        count+=1

    return compareResults
'''
Writes data to log based on whether hashes match or not
'''
def writeLog(compareResults):
    print("Write log")

    return 0

'''
If there is no hash value for a directory
Then one will be added.
'''
def updateDirectories():
    print("Update directories")
    return 0

def main():
    #Dictionaries for directory path and hash
    directories = getDirectory()
    hashes = getHashes()

    numDirectories = len(directories)
    newHash = createHash(directories, numDirectories)

    compareResults = compareHash(hashes, newHash, numDirectories)
    writeLog(compareResults)

if __name__ == "__main__":
    main()