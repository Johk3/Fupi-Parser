import os

from src import parser

files = os.listdir("logs")

for file in files:
    if file == "readme.txt":
        continue
    else:
        parser.parser("./logs/" + file)


