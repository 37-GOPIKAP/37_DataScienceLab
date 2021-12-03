f=open("CopyText.txt","a")
f.write("Hey!I am gopika")
f.close()
with open('CopyText.txt',"r") as firstfile,open("CopyText2.txt","a") as secondfile:
    for line in firstfile:
        secondfile.write(line)
        

    
          