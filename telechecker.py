import requests
import os
import re
import time
from concurrent.futures import ThreadPoolExecutor

# Function to check if a name is available
def checkname(name):
    requestbody = requests.get("https://t.me/" + name).text
    return "tgme_icon_user" in requestbody and "Preview channel" not in requestbody

# Function to pluralize a noun
def pluralize(noun):
    if re.search('[sxz]$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[^aeioudgkprt]h$', noun):
        return re.sub('$', 'es', noun)
    elif re.search('[aeiou]y$', noun):
        return re.sub('y$', 'ies', noun)
    else:
        return noun + 's'

# Function to process a batch of names
def process_batch(batch):
    results = []
    for name in batch:
        plural_name = pluralize(name)
        results.append((name, checkname(name), plural_name, checkname(plural_name)))
    return results

# Input file name and pluralization
filename = input("Enter the name of the file: ")

plural = input("Pluralize? (y/n): ").lower()
plural = True if plural == "y" else False

# Read file into names list, considering only single words with length >= 5
names = []
with open(filename) as file:
    for line in file:
        words = line.rstrip().split()
        if len(words) == 1 and len(words[0]) >= 5:
            names.append(words[0])

# Split the list into batches for parallel processing
batch_size = 100  # Adjust the batch size based on your needs
name_batches = [names[i:i + batch_size] for i in range(0, len(names), batch_size)]

# Name availability checks using multithreading
x = 0
start_time = time.time()
with ThreadPoolExecutor() as executor:
    results = list(executor.map(process_batch, name_batches))
end_time = time.time()

# Flatten the results list
flat_results = [result for batch_result in results for result in batch_result]

# Display the results
for name, available, plural_name, plural_available in flat_results:
    if available:
        print("\033[92m" + name + "\033[0m is potentially available")  # Green color
  #  else:
   #     print("\033[91m" + name + "\033[0m is not available")  # Red color

    if plural:
        if plural_available:
            print("\033[92m" + plural_name + "\033[0m (Plural) is potentially available")  # Green color
    #    else:
     #       print("\033[91m" + plural_name + "\033[0m (Plural) is not available")  # Red color

    x += 1
    os.system(f'printf "\\033]0;CHECKS: {x}\\007"')  # Set terminal title

# Display the time it took to read through the entire list
elapsed_time = end_time - start_time
print(f"\nElapsed Time: {elapsed_time:.2f} seconds")

print("OK!")
input("Press Enter to exit")
