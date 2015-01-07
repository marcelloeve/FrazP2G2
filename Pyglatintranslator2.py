pyg = 'ay'
original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    if first in 'aeiouy':
    new_word = word + pyg
    print new_word
else: 
    print "consonant"
else:
    print "empty"
