import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# duplicates = []

# ORIGINAL = 10 seconds
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# AMARACHI1 = 2 seconds
# for name_1 in names_1:
#     if name_1 in names_2:
#         duplicates.append(name_1)

# USING SET
duplicates = set(names_1) & set(names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Run Times 
# Original = 10 seconds
# Amarachi's = 2 seconds
# Using Set = 0.006 seconds

