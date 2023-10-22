# English to Pig Latin
print('Enter the English message to translate into Pig Latin:')
message = input()

VOWELS = ('a','i','o','u','e','y')

pigLatin = []
for word in message.split():
# TODO: deal with different forms for word
    prefixNonLetter = ''
    while word and not word[0].isalpha():
        prefixNonLetter+=word[0]
        word = word[1:]
    suffixNonLetter = ''
    while word and not word[-1].isalpha():
        suffixNonLetter+=word[-1]
        word = word[:-1]

    if word:
        if word[0].lower() in VOWELS:
            result = word+'yay'
        else:
            result = word[1:]+word[0]+'ay'
        
        if word.lower() == word:
            word = result.lower()
        elif word.upper() == word:
            word = result.upper()
        elif word.title() == word:
            word = result.title()
        else:
            word = result
        
        pigLatin.append(prefixNonLetter+word+suffixNonLetter)

    else:
        pigLatin.append(prefixNonLetter+suffixNonLetter)


# combine words together
text = ' '.join(pigLatin)
print(text)