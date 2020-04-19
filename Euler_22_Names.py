def readFile():
    with open("data.txt", "r") as file:
        # The data file is a list of names in quotes
        # seperated by a comma.  The replace method
        # strips the quotes and the split seperates
        # by comma.
        names = file.read().replace('"','').split(",")
        return names

def alphaValue(name):
    # The unicode value for lowercase a is 97
    # but we want 1, hence the magic number!
    value = 0
    for letter in name.lower():
        value += (ord(letter) - 96)
    return value
 
# Read the data file and sort it.
names = sorted(readFile())
count = 0
position = 1
for name in names:
    count+=(alphaValue(name) * position)
    position+=1
print(count)
