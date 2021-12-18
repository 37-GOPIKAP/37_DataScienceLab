#.write a prgm to copy a text file to another file.
with open('CopyText.txt','r') as firstfile, open('new.txt','w') as secondfile:
    for line in firstfile:
             secondfile.write(line)