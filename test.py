import re
logs = []
minus = []

logs.append(re.findall(r'\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', """DEBUG connect(): about to connect to: (u'neubot.mlab.mlab1.sea01.measurement-lab.org', 80)
DEBUG connect(): getaddrinfo() returned: [(AF_INET, SOCK_STREAM, IPPROTO_TCP, "", ('38.102.0.82', 80)), (AF_INET6, SOCK_STREAM, IPPROTO_TCP, "", ('2001:550:3200:1::82', 80, 0, 0))]
DEBUG connect(): trying with: (AF_INET, SOCK_STREAM, IPPROTO_TCP, "", ('38.102.0.82', 80))
DEBUG connect(): connection to 38.102.0.82:80 in progress...
DEBUG stream: __del__(): 10.3.81.197:39655 216.58.198.49:80
DEBUG isconnected(): checking whether connect() to neubot.mlab.mlab1.sea01.measurement-lab.org:80 succeeded
DEBUG isconnected(): connect() to 38.102.0.82:80 succeeded
DEBUG ClientHTTP: latency: 413.2 ms
DEBUG * Connection made (('10.3.81.197', 36101), ('38.102.0.82', 80))
DEBUG state: negotiate {}
DEBUG notify: publish event: statechange
INFO dash: negotiate... in progress
DEBUG > POST /negotiate/dash HTTP/1.1
DEBUG > Content-Length: 129
DEBUG > Host: neubot.mlab.mlab1.sea01.measurement-lab.org:80
DEBUG > Pragma: no-cache
DEBUG > Cache-Control: no-cache
DEBUG > Date: Fri, 06 Jan 2017 19:00:03 GMT
DEBUG > Content-Type: application/json
DEBUG > Authorization:
DEBUG >"""))
