import string

alphabet = string.ascii_lowercase
#print(alphabet)

secret_message = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"
# eve wants to steal my password

# make my password secret

#print(encrypt(password))
def decrypt(key):
    decrypted_message = ""
    for letter in secret_message:
        old_position = alphabet.find(letter)
        if old_position == -1:
            decrypted_message += " "
        else:
            new_position = old_position - key
            new_position = new_position % len(alphabet)
            new_letter = alphabet[new_position]
            decrypted_message += new_letter
    return decrypted_message


key = 0
for i in range(26):
    print(decrypt(key))
    key += 1
#Key is 16


# Your task:
# figure out what key I used to encrypt this message:
#secret_message = "y qc q iushuj cuiiqwu oek mybb duluh wkuii"
