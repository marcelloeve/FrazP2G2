pyg = 'ay'
 
original = raw_input('Enter a word:')
word = original.lower()
first = word[0]
if (len(original) > 0 and original.isalpha()):
    if (first == 'a' or first == 'e' or first == 'i' or first == 'o' or first == 'u' or first == 'A' or first == 'E' or first == 'I' or first == 'O' or first == 'U'):  
        new_word = word + pyg
        print new_word
    else:
        new_word = word[1:] + word[0] + pyg
        print new_word
else:
    print 'You have not entered a valid word. (Alphabetical Characters only!).'
