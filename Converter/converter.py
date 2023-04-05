# Python program to convert text
# file to JSON


import json


# the file to be converted to
# json format
filename = 'save.txt'

# dictionary where the lines from
# text will be stored
dict1 = {}

# creating dictionary
with open(filename, encoding="utf8") as fh:
    
    for line in fh:
        description = line.strip()
        dict1["-"] = description
       
      
    
    
        


#create json file		
out_file = open("test1.json", "w")
json.dump(dict1, out_file, indent = 4, sort_keys = False)
out_file.close()	

# creating json file
# the JSON file is named as test1

