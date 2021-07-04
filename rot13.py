ciphertext = input("enter your rot13 Ciphertext :　")
plaintext = ""
for i in ciphertext:
	if(65<=ord(i)<=77):
		plaintext+= chr(ord(i)+13)
	elif(97<=ord(i)<=109):
		plaintext+= chr(ord(i)+13)
	elif(78<=ord(i)<=90):
		plaintext+= chr(ord(i)-13)
	elif(110<=ord(i)<=122):
		plaintext+= chr(ord(i)-13)
	else:
		plaintext+=i

print(plaintext)