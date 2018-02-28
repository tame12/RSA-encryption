# RSA-encryption
encrypt with RSA algorithm 

How to use:

1. Reciver generate 3 keys, private, public, and shared
(run RSA_key_generator_main.py) (might take a while)

2. Reciver give Sender public and shared keys

3. Sender use public and shared key to encrypt his message one way
(edit "text_to_be_encrypted.txt" and run "RSA_encryption_main.py")

4. Sender sends encrypted message back to Reciver

5. Reciver use private and shared keys to decrypt message
(run "RSA_encryption_main.py", decrypted message in "decrypted_text.txt"
