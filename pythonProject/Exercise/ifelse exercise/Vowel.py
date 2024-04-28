word=input("Enter word:")
word=word.lower()

if word.isalpha() :
    if 'a' in word or 'e' in word or 'i' in word or 'o' in word or 'u' in word:
        print('There is a vowel')
    else:
        print('no vowels ')
else:
    print('please enter only letters')