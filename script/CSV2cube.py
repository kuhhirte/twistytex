import glob, os, sys, re

if __name__ == '__main__':
    startPath = os.getcwd()
    scriptPath = os.path.join(os.getcwd(),'script')

    if len(sys.argv[1:]) == 0:
        databaseName = input("Please enter the databasename (eg cubes): ")
    else:
        databaseName = sys.argv[1]
    if len(sys.argv[1:]) < 2:
        tempPrefix = "TEMP"
    else:
        tempPrefix = sys.argv[2]
    if len(sys.argv[1:]) < 5: # print the following cubes (regular, shapemods, stickermods)
        regprint = True
        shapeprint = True
        stickerprint = True
    else:
        regprint = sys.argv[3].lower()=="true"
        shapeprint = sys.argv[4].lower()=="true"
        stickerprint = sys.argv[5].lower()=="true"

    workingFolder = tempPrefix+databaseName
    workingPath = os.path.join(scriptPath,workingFolder)

    if not (os.path.isdir(workingPath)):
        os.mkdir(workingPath)
    csv_obj = open(os.path.join(os.getcwd(),databaseName+'.csv'), "r",encoding="cp1252")
    csv_lines = csv_obj.readlines()[1:]
    cubes = []
    for cube in csv_lines:
        cube = cube.replace("&","\&") # escape character
        cube = cube.split('\t') # tabulator is the separator
        # if in CSV there is an empty line after the last element \n is in the empty one
        # since this might causes formatting issues, just remove any instance of \n in the last argument, to be sure
        cube[-1] = cube[-1].replace("\n","")
        cubes.append(cube)
        for i in [1,2,3,5,7]: # textbox indexes
            # replace 2x2 with 2\times 2 and ° with \circ
            cube[i] = re.sub(r'(?<=\d)x(?=\d)', '$\\\\times$', cube[i]).replace("°","$^\circ$")
    for cube in cubes:
        # 3 cases: cases, if one should continue with the next
        # 1&2: if shapemods/stickermods should be printed, check if it is one
        # 3  : if regular cubes should be printed, check if it's neither a shapemod nor a stickermod
        if not ((shapeprint and cube[8].lower()=="true") or (stickerprint and cube[9].lower()=="true") or (regprint and cube[8].lower()=="false" and cube[9].lower()=="false")):
            continue
        with open(os.path.join(workingPath,re.sub(r'\W+', '', cube[3])+'_'+re.sub(r'\W+', '', cube[1])+'_'+cube[0]+'.tex'),"w",-1,"utf-8") as outputFile:
            # currently shapemod and stickermod are not used
            outputString = "\\cube%Shapemod:"+cube[8]+" Stickermod:"+cube[9]+"\n{\\label{label:" + cube[0] + "}"
            if len(cube[4]) == 0:
                outputString += cube[1]
            else:
                outputString += "\\href{"+cube[4].replace("_","\_")+"}{"+cube[1]+"}"
            outputString += "}\n{"+cube[2]+"}\n{"+cube[3]+"}\n{"+cube[5]+"}\n{"+cube[6]+".jpg}\n{"
            text = cube[7]
            matches = re.findall("ID\:\d*", text) 
            for match in matches:
                # find cube with corresponding ID to get name
                name = None
                for nameid in cubes:
                    if nameid[0] == match[3:]:
                        name = nameid[1]
                if name == None:
                    raise IndexError('No ID match for %s.'%(match))
                # substitute every match with the corresponding \hyperref (\ is doubly escaped)
                text = re.sub("ID\:\d*", "\\\\hyperref[label:" + match[3:] + "]{" + repr(name)[1:-1] +"}",text,1)
            outputString += text+"}"
            outputFile.write(outputString)
