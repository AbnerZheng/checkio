import re
from datetime import datetime
import operator


class timeT():
    def __init__(self, l, s, c):
        self.l = l
        self.s = s
        self.c = c

    def __str__(self):
        return "%s;;%s;;%d" % (self.l, self.s, self.c)


class Log():
    def __init__(self, user, domain, duration, count):
        self.user = user
        self.domain = domain
        self.duration = duration
        self.count = count

    def __str__(self):
        return ";;".join([self.user, self.domain, str(self.duration), str(self.count)])


def checkio(log_text):
    logs = log_text.split('\n')
    users = {}
    result = []
    memory = {}
    for log in logs:
        date, name, domain = log.strip().lower().split(';;')
        domain += '/'
        domain = re.search(r'//([^/]+)/', domain).groups()[0]
        second_domain = '.'.join(domain.split('.')[-2:])
        d = datetime.strptime(date, '%Y-%m-%d-%H-%M-%S')
        if name in users:
            if second_domain in users[name]:
                last = users[name][second_domain].l
                timeTheta = d - last
                if timeTheta.seconds >= 30 * 60 or timeTheta.days > 1:
                    temp = users[name][second_domain]
                    result.append(Log(name,second_domain,(temp.l-temp.s).seconds + 1, temp.c))
                    users[name][second_domain] = timeT(d, d, 1)

                else:
                    temp = users[name][second_domain]
                    temp.l = d
                    temp.c += 1
            else:
                users[name][second_domain] = timeT(d, d, 1)
        else:
            users[name] = {}
            users[name][second_domain] = timeT(d, d, 1)

    for name in users:
        for second_domain in users[name]:
            temp = users[name][second_domain]
            result.append(Log(name,second_domain,(temp.l-temp.s).seconds + 1, temp.c))


    result = sorted(result,key=operator.attrgetter('user','domain','duration', 'count'))


    rr = "\n".join([str(e) for e in result])
    return rr



# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print checkio("2013-01-01-01-00-00;;name;;http://checkio.org/task2\n2013-02-01-01-00-00;;Name;;https://admin.checkio.org")

