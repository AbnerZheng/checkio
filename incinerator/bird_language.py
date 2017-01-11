VOWELS = "aeiouy"

def translate(phrase):
    def isVowel(index):
        return phrase[index] in VOWELS

    def isConsonant(index):
        return not isVowel(index)

    phrase = list(phrase)
    result = list()
    while len(phrase) > 0:
        la = len(phrase) - 1
        if isConsonant(la):
            result.append(phrase.pop())
        else: # a
            la -= 1
            if isConsonant(la): # ba
                phrase.pop()
                result.append(phrase.pop())
            elif phrase[-1] == phrase[la]: # aa
                la -= 1
                if isConsonant(la): #baa -> ba : a
                    result.append(phrase.pop())
                elif phrase[-1] == phrase[la]: # aaa -> a :
                    phrase.pop()
                    phrase.pop()
                    result.append(phrase.pop())
                else: # eaa -> e : aa
                    result.append(phrase.pop())
                    result.append(phrase.pop())
            else: # ea -> e : a
                result.append(phrase.pop())
    result.reverse()
    return "".join(result)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate(u"hieeelalaooo") == "hello", "Hi!"
    assert translate(u"hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate(u"aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate(u"sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"