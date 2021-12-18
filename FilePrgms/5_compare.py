#write a prgm to compare two files.
f1 = open("append1", "r")  
f2 = open("append2.txt", "r")   
i = 0
for line1 in f1:
    i += 1  
    for line2 in f2:
        if line1 == line2:  
            print("Line ", i, ": IDENTICAL")       
        else:
            print("Line ", i, ":")
            print("Not Identical")
            print("\tFile 1:", line1, end='')
            print("\tFile 2:", line2, end='')
        break
f1.close()                                       
f2.close() 
