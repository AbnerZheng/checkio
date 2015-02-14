__author__ = '璐'



def checkio(text):

    text = text.lower()
    most = 'z'
    time = 1
    for e in text:
        if e.isalpha() and text.count(e) > time:
            time = text.count(e)
            most = e
        elif text.count(e) == time:
            if e.isalpha() and e<most:
                most = e
    return most

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    print("The local tests are done.")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
