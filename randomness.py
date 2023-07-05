import math

# Read the generated codes from a text file
def read_codes_from_file(file_path):
    with open(file_path, 'r') as file:
        codes = [line.strip() for line in file]
    return codes

# Calculate the entropy value
def calculate_entropy(codes):
    n = len(codes)
    unique_codes = set(codes)
    counts = [codes.count(x) for x in unique_codes]

    entropy = 0.0
    for count in counts:
        probability = count / n
        entropy -= probability * math.log2(probability)
    
    return entropy

# Calculate the guessing probability
def calculate_guessing_probability(entropy):
    guessing_probability = 2 ** (-entropy)
    return guessing_probability

# Prompt the user to enter the path of the text file
file_path = input("Enter the path of the text file: ")

# Read the generated codes from the file
codes = read_codes_from_file(file_path)

# Calculate the entropy value
entropy = calculate_entropy(codes)

# Calculate the guessing probability
guessing_probability = calculate_guessing_probability(entropy)

# Determine randomness level
if entropy == 0:
    randomness = "No randomness (All identical codes)"
elif entropy < math.log2(len(codes)):
    randomness = "Low randomness (Some repeated codes)"
else:
    randomness = "High randomness (No repeated codes)"

# Calculate the guessing percentage
guessing_percentage = guessing_probability * 100

# Print the entropy value, randomness level, and guessing probability
print("Estimated Entropy:", entropy)
print("Randomness Level:", randomness)
print("Guessing Probability: {:.2f}%".format(guessing_percentage))
