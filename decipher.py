# Decipher Caesar Cipher

# prompt input encrypted message & decrypt key
message = str(input("please input message to decrypt:"))
key = int(input("please input decrypt key:"))

# output deciphered string
decipher = ""

# loop through characters in message
for char in message:

# if character is UPPERCASE; ASCII A code -> 65
	if char.isupper():									
		mod = ((ord(char) - key - 65) % 26) + 65
		decipher += chr(mod)

# if character is <space>; ASCII <space> code -> 32; DO NOT ENCRYPT SPACES
	elif ord(char) == 32:
		decipher += char

# Otherwise assuming lowercase; ASCII a code -> 97
	else:
		mod = ((ord(char) - key - 97) % 26) + 97
		decipher += chr(mod)

print(decipher)