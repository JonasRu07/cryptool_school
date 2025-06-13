from cryptool.cryptool import caeser

# Caeser
clear_text = 'Jeder einzelne Mensch erlebt jeden Tag verschiedene Elemente des Lebens.'
key = 3
encrypted_text = caeser.encrypt(clear_text, key)

print(caeser.encrypt(clear_text, key=key))
print(caeser.decrypt(encrypted_text, key=key))

print(caeser.decrypt_bruteforce(encrypted_text))

print(caeser.decrypt_frequency_analysis(encrypted_text))