#
# An implenmentation of cryptograpy for secure communication
# Written in 2016
#

import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Returns a fernet suite generated from the password
def get_fernet(passwd):
	passwd_bytes = passwd.encode('UTF-8')
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=b'',
		iterations=100000,
		backend=default_backend()
	)
	key = base64.urlsafe_b64encode(kdf.derive(passwd_bytes))
	return Fernet(key)
