import re


def checkio(url):
    url = url.lower()
    url = re.split("(%.{2})", url)
    if len(url) > 1:
        result = ''
        for e in url:
            tt = e
            if e.startswith('%'):
                tt = tt.upper()
                quote_char = e[1:]
                quote_char = chr(int(quote_char, 16))
                if quote_char.isalnum():
                    tt = quote_char.lower()
                elif quote_char in '~-._':
                    tt = quote_char
            result += tt
        url = result

    else:
        url = ''.join(url)

    temp = re.match('(http.*):80$', url)
    if temp:
        url = ''.join(temp.groups())
    else:
        temp = re.match('(http.*):80([^1-9]+.*)', url)
        if temp:
            url = ''.join(temp.groups())


    ttt = re.match('(\S+://[^/]*)(.*)', url).groups()
    host = ttt[0]
    path = ttt[1]

    path = path.split('/')
    result_path = []
    if len(path) > 1:
        for e in path:
            if e == '.' or e == '':
                continue
            elif e == '..':
                result_path.pop()
            else:
                result_path.append(e)

        host = host + '/' + '/'.join(result_path)

    if len(path) > 1 and path[-1] == '':
        host = host + '/'
    return host


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"Http://Www.Checkio.org") == \
           "http://www.checkio.org", "1st rule"
    assert checkio(u"http://www.checkio.org/%cc%b1bac") == \
           "http://www.checkio.org/%CC%B1bac", "2nd rule"
    print checkio(u'http://example.com:80')
    assert checkio(u"http://www.checkio.org/task%5F%31") == \
           "http://www.checkio.org/task_1", "3rd rule"
    assert checkio(u"http://www.checkio.org:80/home/") == \
           "http://www.checkio.org/home/", "4th rule"
    assert checkio(u"http://www.checkio.org:8080/home/") == \
           "http://www.checkio.org:8080/home/", "4th rule again"
    assert checkio(u"http://www.checkio.org/task/./1/../2/././name") == \
           "http://www.checkio.org/task/2/name", "5th rule"
    print('First set of tests done')

    print checkio("http://Example.com:80/%48%6f%6d%45")
    print checkio("http://example.com:80/HOME/../././Guest/1/../2/..")
