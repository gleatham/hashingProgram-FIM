import os
import hashlib


# Creat hash of a directory
def createHash(directory):
    SHAhash = hashlib.md5()
    directory = directory
    #directory = 'C:\\Users\\Geoff\\Documents\\hashTest'


    try:
        for root, dirs, files in os.walk(directory):
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

    return SHAhash.hexdigest()

#Reads in a directory path from a file.
#Directory path is used in createHash()
def getDirectory():
    print("Getting the directory from file")
    directories = {}

    with open('C:\\Users\\Geoff\\Documents\\hashTest\\directories.txt') as fin:
        directoriesList = fin.readlines()
        numDirectories = len(directoriesList)

        counter = 0
        while(counter < numDirectories):
            tempDirList = directoriesList[counter].split(':', 3)

            directories.update({tempDirList[0]: tempDirList[1]})

            counter+=1


    return directories

#Reads file to get keys and hashes
def getHashes():
    print("Get Current Hashes")
    hashes = {}

    with open('C:\\Users\\Geoff\\Documents\\hashTest\\directories.txt') as fin:
        hashesList = fin.readlines()
        numDirectories = len(hashesList)

        counter = 0
        while(counter < numDirectories):
            tempHashList = hashesList[counter].split(':', 3)

            hashes.update({tempHashList[0]: tempHashList[2]})

            counter+=1


    return hashes

def compareHash():
    print("Compare Hash")


def main():
    print("In Main")

    #add C: to directories for windows

    #Dictionaries for directory path and hash
    directories = getDirectory()
    hashes = getHashes()
    newHash = createHash(directories.get('folder1'))
    print(newHash)
    #newHash = createHash(directories)
    #test = createHash()
    #print(test)

if __name__ == "__main__":
    main()