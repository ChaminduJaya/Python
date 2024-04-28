word=input('Enter word: ')
mid=int(len(word)/2)
if len(word)%2==0:

    print(word[:mid]+'@'+word[mid:])
else:
    word=word.replace(word[mid],'@')
    print(word)