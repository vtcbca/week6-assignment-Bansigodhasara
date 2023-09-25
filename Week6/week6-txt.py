
# Read Python.txt file and Print it in Reverse.

file="C:\\sqlite3\\python.txt"
with open(file,"r")as text_file:
    data=text_file.read()
reverse=data[::-1]
print(reverse)

# Read Python.txt file and Print total number of lines and words in it.
number_words=0
with open("c:\\sqlite3\\python.txt","r") as file:
    for line in file:
        words=line.split()
        number_words+=len(words)
with open("c:\\sqlite3\\python.txt","r") as file:
    lines=file.readlines()
total_lines=len(lines)
print("Total number of lines:",total_lines)
print("Total number of words:",number_words)

 # Read Python.txt file and Print unique word with its count.
unique_words_count=0
with open("c:\\sqlite3\\python.txt","r") as file:
        line=file.read()
        words=set(line.split())
print("total unique words:",len(words))
print("Unqiue words are:",words)

#Read Python.txt file and Print largest and smallest word from it.
with open("c:\\sqlite3\\python.txt","r") as file:
        line=file.read()
        words=line.split()
        largest=small=words[0]
        for i in range(0,len(words)):
            if (len(largest)<len(words[i])):
                largest=words[i]
            elif(len(small)>len(words[i])):
                  small=words[i]
print("largest word:",largest)
print("smallest word:",small)

# Read Python.txt file. Convert it into upper case and write into another file "Python_Upper.txt"
file="C:\\sqlite3\\python.txt"
f="c:\\sqlite3\\python_upper.txt"
with open(file,"r")as text_file:
    data=text_file.read()
upper=data.upper()
with open(f,"w") as txt:
    text=txt.write(upper)
