import os
import datetime

from src import parser

files = os.listdir("logs")
filename = "./output/" + datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S") + ".txt"

for file in files:
    if file == "readme.txt":
        continue
    else:
        configured = parser.Parser("./logs/" + file, filename)
        configured.mainip()


