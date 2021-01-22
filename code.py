import os
os.system("clear")

input = input("Enter text: ")

f = open("test2.txt", "w") 
f.write(input)
f.close()