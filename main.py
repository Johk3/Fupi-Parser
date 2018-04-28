import os
import datetime
from src import parser

files = os.listdir("logs")
filename = "./output/" + datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S") + ".csv"

for file in files:
    if file == "readme.txt":
        continue
    else:
        print("Working on file {}".format(file))
        configured = parser.Parser("./logs/" + file, filename)
        configured.parse()
