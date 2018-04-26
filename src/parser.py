# This parses the data and returns only the goods.
import re


class Parser(object):

    def __init__(self, logs, filename):
        self.logs = logs
        self.filename = filename

    # Parses the text and then outputs it to output folder
    def mainip(self):
        file = open(str(self.logs), 'r')
        check = []
        out = []
        ip_address = r'\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        print("Reading {}".format(self.logs))
        output = open(str(self.filename), 'w+')
        print("Writing {} to output".format(self.filename))
        i = 1
        for line in file.readlines():
            if "++++++++++++++++++BEGIN NEW DASH TEST!!!++++++++++++++" in line:
                print("++++++++++++++TIMESTAMP NUMBER {} ++++++++++++++".format(i))
                i+=1

            if not re.findall(ip_address, line) or re.findall(ip_address, line) in check:
                continue

            else:
                check.append(re.findall(ip_address, line))
                out.append(re.findall(ip_address, line))
        print("Done")
        output.write(str(out))




