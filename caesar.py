#!/usr/bin/env python3

import sys

try:
    key = int(sys.argv[2])
except ValueError:
    exit("""Key must be an integer \nUsage python3 caesar.py 'ciphertext' 'key' """)
    

if len(sys.argv) != 3:
    print("Usage python3 caesar.py 'ciphertext' 'key'")


cipher_text = sys.argv[1]

plain_text = ''.join([chr(ord(c)- key) for c in cipher_text])

print(plain_text)