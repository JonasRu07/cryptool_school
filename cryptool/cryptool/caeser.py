from .configs.constants import CaeserAlphabets

def encrypt(message:str, key:int=0) -> str:
    """
    Takes a message and encrypts it using caeser algorithm
    :param message: massage to encrypt. Only upper and lower letters will be encrypted. Any other will stay the same
    :param key: By how many letters each letter will be shifted
    :return: encrypted message
    """
    alphabet: list[str] = CaeserAlphabets().alphabet
    encrypt_message: list[str] = []
    for letter in message:
        if letter.isalpha():
            lower = True if letter.islower() else False
            index = alphabet.index(letter.upper())
            index_new = (index - key) % 26
            encrypt_message.append(alphabet[index_new].lower() if lower else alphabet[index_new])
        else:
            encrypt_message += letter

    return ''.join(encrypt_message)

def decrypt(message:str, key:int=0) -> str:
    """
    Takes a message and decrypts it using caeser algorithm
    :param message: massage to decrypt. Only upper and lower letters will be decrypted. Any other will stay the same
    :param key: By how many letters each letter will be shifted
    :return: decrypted message
    """
    alphabet: list[str] = CaeserAlphabets().alphabet
    decrypt_message: list[str] = []
    for letter in message:
        if letter.isalpha():
            lower = True if letter.islower() else False
            index = alphabet.index(letter.upper())
            index_new = (index + key) % 26
            decrypt_message.append(alphabet[index_new].lower() if lower else alphabet[index_new])
        else:
            decrypt_message += letter

    return ''.join(decrypt_message)

def decrypt_bruteforce(message:str) -> list[tuple[str, int]]:
    """
    Gives every possible solution to the message using casesers algorithm
    :param message: what to be decrypted
    :return: Every possible solution from using key 0 to max key
    """
    return [(decrypt(message, key=i), i) for i in range(len(CaeserAlphabets().alphabet))]

def decrypt_frequency_analysis(message:str) -> tuple[str, int]:
    """
    Checks the message for the highest frequency of a letter in the message and tries to decrypt the message by
    assuming the letter is the most common based on the frequency alphabet. Return only the most likely solution
    :param message: message to decrypt
    :return: decrypted message, key to decrypt
    """
    alpha = CaeserAlphabets()
    letter_count = sorted([(letter, message.upper().count(letter)) for letter in alpha.alphabet],
                          key=lambda item : item[1],
                          reverse=True)
    message_most_common = alpha.alphabet.index(letter_count[0][0])
    index_most_common = alpha.alphabet.index(alpha.frequency_alphabet[0])
    key = (index_most_common - message_most_common) % len(alpha.alphabet)
    return decrypt(message, key=key), alpha.alphabet.index(letter_count[0][0])