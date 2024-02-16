from cgi import print_arguments


fhand = open("mbox-short.txt")
print(fhand)

print("This is the end of the line\nAnd I am second paragraph")

count = 0
for line in fhand:
    count += 1
    print("Line count:", count)

# reading whole file
file = open("mbox-short.txt")
inp = file.read()
print(f"There are total {len(inp)} characters in the mbox-short.txt file ")

# searching through file
fromFileHandler = open("mbox-short.txt")

for line in fromFileHandler:
    if line.find("@uct.ac.za") == -1:
        continue
    print(line.rstrip())

# asking file name from user and handeling exception with try except
    
fname = input("Enter file name: ")

try:
    open_file = open(fname)
except:
    print("Error opening file: ",fname)
    exit()
count = 0
for line in open_file:
    count = count + 1

print(f'''Total line in {fname} is {count}''')