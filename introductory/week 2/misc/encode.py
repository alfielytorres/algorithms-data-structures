plain = 'abcdefghijklmnopqrstuvwxyz'
cipher = 'THEQUICKBROWNFXJMPSVLAZYDG'



def get_cipher(plaintext):
    plaintext = plaintext.lower()
    encoded_word =[]

    # this is where the magic happens 
    for char in plaintext:
        if char in plain: # if the character is in plaintext 
            index = plain.find(char) # get index
            encoded_word.append(cipher[index]) # retrieve index in cipher

            print("{} {} {}".format(char, index, cipher[index])) # for debugging
        else: 
            print(' ')
    return ''.join(encoded_word) # join the word

print(get_cipher('tAke the rubicon'))
