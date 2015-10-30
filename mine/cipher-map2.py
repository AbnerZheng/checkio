__author__ = 'abnerzheng'

def recall_password(cipher_grille, ciphered_password):
    position = [];
    for i in range(4):
        for j in range(4):
            if cipher_grille[i][j] == 'X':
                position.append((i,j))
    result = ""
    for i in range(4):
        for jj in range(len(position)):
            result += ciphered_password[position[jj][0]][position[jj][1]]
            position[jj] = (position[jj][1], 4 - 1 - position[jj][0])
        position.sort()
    return result





if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
