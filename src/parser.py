# This parses the data and returns only the goods.
import re


class Parser(object):

    def __init__(self, logs, filename):
        self.file = open(str(logs), 'r')
        self.output = open(str(filename), 'w+')

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

            if timestamp is None:
                time_str = line[29:50]
                timestamp = time_str[:12] + time_str[14:]
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

        self.output.write("Dash test from %s  |  Server IP: %s  |  Server name: %s  |  Client IP: %s\n" %
                          (timestamp, server_IP, server_name, client_IP))
        for seg in segments:
            self.output.write("Segment number: %d, Size: %d bytes, Rate: %d kbit/s, Speed: %d kbit/s\n" % seg)
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
