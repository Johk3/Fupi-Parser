# This parses the data and returns only the goods.
import re
import datetime


def parser(logs):
    # Parses the text and then outputs it to output folder
    file = open(str(logs), 'r')
    check = []
    print("Reading {}".format(logs))
    filename = "./output/" + datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S") + ".txt"
    output = open(str(filename), 'w+')
    print("Writing {} to output".format(filename))
    for line in file.readlines():
        if not re.findall(r'\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line) or re.findall(r'\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line) in check:
            continue
        else:
            check.append(re.findall(r'\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line))
            output.write("\n" + "".join(re.findall(r'\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)))




