#write a prgm to count the no.of lines in a file.
f1="append2.txt"
count=0
with open(f1,'r') as f:
    for line in f:
        count=count+1
print("Total no.of lines in the file is",count)
    
