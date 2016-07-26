#
# An implenmentation of cryptograpy for secure communication
# Written in 2016
#

import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Returns a fernet suite generated from the password
def get_fernet(passwd):
	passwd_bytes = bytes(passwd)
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=b'',
		iterations=100000,
		backend=default_backend()
	)
	key = base64.urlsafe_b64encode(kdf.derive(passwd_bytes))
	return Fernet(key)
