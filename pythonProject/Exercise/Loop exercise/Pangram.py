Alphabet=[chr(char) for char  in range(ord('A'),ord('Z'))]
print(Alphabet)
sen= 'The quick brown fox jumps over the lazy dogs'
sen=sen.upper()
print(sen)
def panagram():
    for char in Alphabet:

        if char not in sen:
            print('this is not a panagram')
            return

    print('This is a panagram')
panagram()