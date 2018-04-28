# This parses the data and returns only the goods.
import re
from shlex import split


class Parser(object):

    def __init__(self, logs, filename):
        self.file = open(str(logs), 'r')
        self.output = open(str(filename), 'w+')
        self.check = 1

    def parse(self):
        for line in self.file:
            if line == "++++++++++++++++++BEGIN NEW DASH TEST!!!++++++++++++++\n":
                self.read_entry()

    def read_entry(self):
        line = None
        timestamp = None
        server_IP = None
        server_name = None
        client_IP = None

        ip_address = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        flag = False

        while line != "++++++++++++++FINISHED TEST!!!++++++++++++++++++++\n":
            line = self.file.readline()
            segments = ((-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1),
                        (-1, -1, -1, -1))

            if timestamp is None:
                time_str = line[29:50]
                timestamp = time_str[:12] + time_str[12:]
                timestamp = " ".join("" if x == "-" else x for x in split(timestamp))
            elif server_IP is None:
                if "DEBUG isconnected(): connect() to" in line:
                    server_IP = re.findall(ip_address, line)[0]
            elif server_name is None:
                if "fqdn" in line:
                    server_name = line[21:-3]
            elif client_IP is None:
                if not flag:
                    flag = True
                else:
                    client_IP = re.findall(ip_address, line)[0]
            else:
                segments = self.read_segments()
                break
        if self.check == 1:
            self.output.write("segment-number, segment-size, segment-rate, segment-speed, timestamp, server-ip, "
                              "server-name, client-ip\n" )
            self.check = 2
        i = 1
        for seg in segments:
            if i == 1:
                self.output.write("%d,%d,%d,%d,{},{},{},{}\n".format(timestamp, server_IP, server_name, client_IP) % seg)
                i = 2
            else:
                self.output.write("%d,%d,%d,%d\n" %seg)

        self.output.write("\n")

    def read_segments(self):
        numbers = r'\d+'
        seg_num = -1
        segments = []

        while seg_num != 15:
            line = self.file.readline()
            if line[:32] == "DEBUG dash: got response - elaps":
                size = round(int(re.findall(numbers, line)[2]) - 100, -2)
            elif "INFO dash: [" in line:
                nums = re.findall(numbers, line)
                seg_num = int(nums[0])
                rate = int(nums[2])
                speed = int(nums[3])
                segments.append((seg_num, size, rate, speed))

        return segments