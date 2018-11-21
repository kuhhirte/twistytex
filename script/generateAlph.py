import glob, os, sys

def getTypes(file):
    lines = []
    for line in file.read().split("{"): # map ?
        for char in line: # filter ?
            if char in ['}','\n']:
                 line = line.replace(char,'')
        lines.append(line.split('%', 1)[-1]) # if theres a comment, use part after last % for sorting
    return lines


if __name__ == '__main__':
    startPath = os.getcwd()
    scriptPath = os.getcwd()+"\\script\\"

    if len(sys.argv[1:]) == 0:
        workingPath = input("Please enter the foldername (eg cubes): ")
    else:
        workingPath = sys.argv[1]
    outputPath = "TEMP"+workingPath

    with open(scriptPath+workingPath+".tex","w",-1,"utf-8") as outputFile:
        os.chdir(scriptPath+outputPath)
        texList = glob.glob("*.tex") # collect tex files in list
        texList.sort()
        sortList = []
        sortBy = "Form" #TODO: change hardcoded to parameter
        for file in texList:
            file_obj  = open(os.getcwd()+"\\"+file, "r",-1,"utf-8")
            lines = getTypes(file_obj)
            if(sortBy == "Form"):
                if not lines[2] in sortList:
                    sortList.append(lines[2])
        sortList.sort()
        # generate the tex for the given folder
        # 1. print variable values for LaTeX
        # 2. for every cubetype do
        #  a print cubetype as section
        #  b open every cube file
        #  c check, if it is of given cubetype
        #  d print, if true
        outputFile.write("\\newcommand{\sortby}{"+sortBy+"}\n\n")
        for cubetype in sortList:
            outputFile.write("\n\\newpage\n\section{"+cubetype+"}\n\n")
            for file in texList:
                file_obj  = open(os.getcwd()+"\\"+file, "r",-1,"utf-8")
                lines = getTypes(file_obj)
                if cubetype == lines[2]:
                    outputFile.write("\input{script/"+outputPath+"/"+file+"}\n")
