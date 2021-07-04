ciphertext = input("enter your caesar Ciphertext :　")
for i in range(26):
	plaintext = ""
	for c in ciphertext:
		if(65<=ord(c)<=90):
			if(91<=ord(c)+i):
				plaintext+=chr(ord(c)+i-26)
			else:
				plaintext+=chr(ord(c)+i)
		elif(97<=ord(c)<=122):
			if(123<=ord(c)+i):
				plaintext+=chr(ord(c)+i-26)
			else:
				plaintext+=chr(ord(c)+i)
		else:
			plaintext+=c
	print(i,plaintext)