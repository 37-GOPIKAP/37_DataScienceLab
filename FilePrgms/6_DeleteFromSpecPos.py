#write a prgm to delete a sentence from the specified position in a file.

f1=open("delete.txt","r")
lines=f1.readlines()
print(lines)
f1.close()
del lines[0]
f1=open("delete.txt","w+")
for line in lines:
    f1.write(line)
print(lines)
f1.close()