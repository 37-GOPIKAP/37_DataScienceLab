#write a prgm to append a file with the contents of another file.
file1 = input("Enter file to be read from: ")
file2 = input("Enter file to be appended to: ")
fin = open(file1, "r")
data2 = fin.read()
fin.close()
fout = open(file2, "a")
fout.write(data2)
fout.close()