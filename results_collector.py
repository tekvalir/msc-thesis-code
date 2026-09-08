import os
import re

PWD = "."
OUTPUT_FOLDER = "output"

access_pattern = re.compile('Data Access: (\d+)')

results = {}

for filename in os.listdir(os.path.join(PWD, OUTPUT_FOLDER)):
    # print(filename)
    # print(filename.endswith("-res.txt"))
    if not filename.endswith("-res.txt"):
        continue
    discriminator = filename[:-8]
    with open(os.path.join(PWD, OUTPUT_FOLDER, filename)) as file:
        for i,line in enumerate(file):
            access_match = re.search(access_pattern, line)
            if access_match:
                results[discriminator] = access_match.group(1)
                continue



for key, value in results.items():
    print(key, value)
