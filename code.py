import pickle
import os

os.system("clear")

data = ["Number 1", "Number 2", "Number 3"]

# Printing the original list
print("Original List")
print(data)

# Save the list (wb means to write)
pickle.dump(data, open("data.dat", "wb"))

# Removing "Number 3"
print("Removed item List")
data.remove("Number 3")
print(data)

#Adding number 4 to the end of the list
pickle.dump(data, open("data.dat", "wb"))
print("Added new item List")
data.append("Number 4")
print(data)

# Added and Removed another set of numbers
print("Adding number 5")
data.append("Number 5")
print(data)

print("Removing number 5")
data.remove("Number 5")
print(data)