v = {
    'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7,
    'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 
    'p': 15,'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 
    'w':22, 'x': 23,'y': 24, 'z': 25
}
def keyy(v, value):
    value = value % 26
    for key, val in v.items():
        if val == value:
            return key
    return None
    
def ceasar_e(text, key):
    text = text.lower()
    ciphertext = ''
    for let in text:
        if let == ' ':
            ciphertext += ' '
        else:
            n = ''
            n = keyy(v, v[let]+key)
            ciphertext += n
    return ciphertext

def ceasar_d(c_text, key):
    c_text = c_text.lower()
    plaintext = ''
    for let in c_text:
        if let == ' ':
            plaintext += ' '
        else:
            n = ''
            n = keyy(v, v[let]-key)
            plaintext += n
    return plaintext
    
print('--------------key = 3---------------------')
print('Encrypted = ',ceasar_e('jeevan',3))
print('decrypted = ',ceasar_d(ceasar_e('jeevan',3),3))

print('\n')

print('Encrypted = ',ceasar_e('j',3))
print('decrypted = ',ceasar_d(ceasar_e('j',3),3))

print('\n')

print('Encrypted = ',ceasar_e('my name is jeevan sendur g',3))
print('decrypted = ',ceasar_d(ceasar_e('my name is jeevan sendur g',3),3))

print('--------------key = 5---------------------')

print('Encrypted = ',ceasar_e('jeevan',5))
print('decrypted = ',ceasar_d(ceasar_e('jeevan',5),5))

print('\n')

print('Encrypted = ',ceasar_e('j',5))
print('decrypted = ',ceasar_d(ceasar_e('j',5),5))

print('\n')

print('Encrypted = ',ceasar_e('my name is jeevan sendur g',5))
print('decrypted = ',ceasar_d(ceasar_e('my name is jeevan sendur g',5),5))

print('-------------------------------------------')