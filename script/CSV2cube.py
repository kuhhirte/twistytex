import glob, os, sys

if __name__ == '__main__':
    startPath = os.getcwd()
    scriptPath = os.getcwd()+"\\script\\"

    if len(sys.argv[1:]) == 0:
        databaseName = input("Please enter the databasename (eg cubes): ")
    else:
        databaseName = sys.argv[1]
    if len(sys.argv[1:]) == 1:
        tempPrefix = "TEMP"
    else:
        tempPrefix = sys.argv[2]

    workingPath = tempPrefix+databaseName

    if not (os.path.isdir(scriptPath+workingPath)):
        os.mkdir(scriptPath+workingPath)
    csv_obj = open(os.getcwd()+"\\"+databaseName+".csv", "r",-1,"utf-8") # TODO: make variable
    for cube in csv_obj.readlines()[1:]:
        cube = cube.split(',') # since , appears in text change to other separator
        with open(scriptPath+workingPath+"\\"+cube[6]+".tex","w",-1,"utf-8") as outputFile:
            # currently shapemod and stickermod are not used
            outputFile.write("\\cube%Shapemod:"+cube[8]+" Stickermod:"+cube[9]+
                             "{"+cube[1]+"}\n{"+cube[2]+"}\n{"+cube[3]+"}\n{"+
                             cube[5]+"}\n{"+cube[6]+".jpg}\n{"+cube[7]+"}")
