simple-xor
==========

One-Time-Pad Encryption/Decryption Software

Simple XOR-Like 0.2 beta

Added file encryption(experimental)
Added mainloop 
Chenged name to Simple XOR-Like 
Implemented with email client: check LilyXOR.py

Lilymail: https://github.com/xiaolong/LilyMail

A simple XOR-Like Encrypter and Decrypter by mad_dev

This script will create the following:
"en/data.in", "en/data.out", "en/key.in", "de/de_data.in", "de/de_data.out", 
"de/de_key.in, "en/log.txt" and "de/log.txt"

All the files mentioned above will be opened in Gedit
(you can edit this from the source code)

NOTE: All files will be cleaned(erased) everytime you run this script""")


Definition:
  EN or en:
		The input string; binary in case of
		compressed files and plain text in case of
		messages.
	DE or de:
		The output string; the encrypted data

	Randomiser or rand:
		The piece of code that insures every attempt
		differs from the next.
	Key or key:
	Between en and de, the string generated from
	the randomiser will produce the key.
	

Check Simple_XOR-Like-Wiki.pdf for an example
