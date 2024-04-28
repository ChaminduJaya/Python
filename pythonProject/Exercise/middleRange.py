'''
Enter word with more than 2 letters.Then you must have to provide output with centerized
3 letters (if word has no of odd letters)or four letters(if word has no of odd letters).
ex:
Enter your word: Chamindu
Output : amin
Enter your word: Pradeep
Output : ade
'''
word=input('Enter your word: \n')
if word.isalpha():
    if len(word)>2:
        center = int(len(word) / 2)
        if len(word)%2==0 :

            word=word[center-2:center+2]

        else :

            word=word[center-1:center+2]
        print(word)
    else:
        print('Please enter word with more than two letters')
else:
    print('Please enter only letters')