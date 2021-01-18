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
print("Modified List")
data.remove("Number 3")
print(data)