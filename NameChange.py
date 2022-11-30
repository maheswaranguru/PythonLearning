# import OS module
import os

removeStr1 ="பொன்னியின் செல்வன் ஒலிப்புத்தகம்"
removeStr2 = '_ Tamil Audiobook (192kbit_AAC)'

print("*********************************************************\n") 
# Get the list of all files and directories
path = "D:\Maheswaran\SourceCode\Python\PonniyinSelvan Part1\Part1"
dir_list = os.listdir(path)
 
##print("Files and directories in '", path, "' :") 
###prints all files
##print(dir_list[1])
for i in dir_list:
    if removeStr1 in i:
        print(i)

sourcestr = path + '\\' + dir_list[1]
print(sourcestr)

disStr = dir_list[1].replace(removeStr1, "")
disStr = disStr.replace(removeStr2, "")
disStr = disStr.replace('Ponniyin Selvan', " ")
disStr = disStr.replace(" ", "")

print(disStr)
##filtered = txt.split( substring )
##print(filtered)
#os.rename( sourcestr, disStr)
