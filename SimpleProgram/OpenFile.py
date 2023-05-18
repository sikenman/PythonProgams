path = "SimpleProgram"
file = "AsciiChar-Output.txt"

# read utf-8 from file and display it
def ReadFile(path,file):
    with open(path+"/"+file, "r", encoding="utf-8") as f:
        contents = f.read()
        print(contents)

ReadFile(path,file)
