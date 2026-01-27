# Problem to detect a double space

name = input("Enter a string : ")
if(name.find("  ")!=-1):
    print("double space found")
    #replace double space with single
    new_name = name.replace("  "," ")
    print("Stirng with single space : "new_name)

else:
    print("not found")
    

