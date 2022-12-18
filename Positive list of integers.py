# Open file in reading mode
#text = open("sample.txt", "r")

# Create empty dictionary

d = dict()

# Step through each line in the file

for line in text:

# Remove spaces and newlines

line = line.strip()

# Convert characters in the string to

# lowercase to avoid case mismatch

line = line.lower()

# Split string into words

words = line.split(" ")

# Loop over each word in line

for word in words:

    # Check if the word is in the dictionary

    if word in d:

# Increase word count by 1

d[word] = d[word] + 1

else:

# Add word to dictionary with number 1

d[word] = 1

# Print the contents of the dictionary

for key in list(d.keys()):

print(key, ":", d[key])

