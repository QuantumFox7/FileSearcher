# File Searcher V1

from os import listdir

searchterm = input("Enter Searchterm: ")

x = open("results.txt", "w+")
x.close()
include = []
filename = __file__[::-1].replace(__file__[::-1][__file__[::-1].index("\\"):-1], "")[-2::-1]
dir = listdir()
dir.remove(filename)
dir.remove("results.txt")

def result(result):
    print(result)
    x = open("results.txt", "a")
    x.write(result+"\n")
    x.close()

result(f"Files to search: {dir}")
result("Starting...")
for i in dir:
    result(f"Searching File: {i}")
    file = open(i, "r")
    read = file.read()
    file.close()
    for j in read.splitlines():
        if searchterm in j:
            result(f"Found Match: \"{j}\" in \"{i}\"")
            include.append(j)
result("Finished")
