import glob, os, sys

def getTypes(file):
    lines = []
    iolines = file.read().split("\n{",1)[1] # remove }\cube% ... {
    for line in (iolines.split("}\n{")): # map ? // split at every linebreak between parameters
        lines.append(line.split('%', 1)[-1]) # if theres a comment, use part after last % for sorting
    return lines


if __name__ == '__main__':
    startPath = os.getcwd()
    scriptPath = os.path.join(os.getcwd(),'script')

    if len(sys.argv[1:]) == 0:
        workingPath = input("Please enter the foldername (eg cubes): ")
    else:
        workingPath = sys.argv[1]
    if len(sys.argv[1:]) == 1:
        sortBy = input("Please enter the sorting field (eg Shape): ")
    else:
        sortBy = sys.argv[2]
    
    outputPath = 'TEMP'+workingPath

    with open(os.path.join(scriptPath,workingPath+'.tex'),"w",-1,"utf-8") as outputFile:
        os.chdir(os.path.join(scriptPath, outputPath))
        texList = glob.glob("*.tex") # collect tex files in list
        texList.sort()
        sortList = []
        for file in texList:
            file_obj  = open(os.path.join(os.getcwd(),file), "r",-1,"utf-8")
            lines = getTypes(file_obj)
            if(sortBy == "Shape"):
                if not lines[1] in sortList:
                    sortList.append(lines[1])
            else:
                raise ValueError('No field named %s.'%(sortBy))
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
                file_obj  = open(os.path.join(os.getcwd(),file), "r",-1,"utf-8")
                lines = getTypes(file_obj)
                if cubetype == lines[1]:
                    outputFile.write("\input{script/"+outputPath+"/"+file+"}\n")
