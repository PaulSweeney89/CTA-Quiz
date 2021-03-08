def encrypt(plain_txt, offset):
	cipher_txt = ""

	for i in plain_txt:
		num_val = ord(i)

		if (i.isupper()):
			adj_val = ((num_val + offset - 65) % 26) + 65
			cipher_txt += chr(adj_val)

		elif num_val == 32:
			cipher_txt += ""

		else:
			adj_val = ((num_val + offset - 97) % 26) + 97
			cipher_txt += chr(adj_val)	

	return cipher_txt

print(encrypt("or are we dancer", 2))


def decrypt(ciph_txt, offset):
	decrypt_txt = ""

	for i in ciph_txt:
		num_val = ord(i)

		if (i.isupper()):
			adj_val = ((num_val - offset - 65) % 26) + 65
			decrypt_txt += chr(adj_val)

		elif num_val == 32:
			decrypt_txt += i

		else:
			adj_val = ((num_val - offset - 97) % 26) + 97
			decrypt_txt += chr(adj_val)	

	return decrypt_txt

print(decrypt("Mwrx Neze Kviex", 4))