# Caesar Cipher Algorithm

# prompt input message & encrypt key
message = str(input("please input message to encrypt:"))
key = int(input("please input encrypt key:"))

# output encrypted string
cipher = ""

# loop through characters in message
for char in message:

# if character is UPPERCASE; ASCII A code -> 65
	if char.isupper():									
		mod = ((ord(char) + key - 65) % 26) + 65
		cipher += chr(mod)

# if character is <space>; ASCII <space> code -> 32; DO NOT ENCRYPT SPACES
	elif ord(char) == 32:
		cipher += char

# Otherwise assuming lowercase; ASCII a code -> 97
	else:
		mod = ((ord(char) + key - 97) % 26) + 97
		cipher += chr(mod)

print(cipher)
