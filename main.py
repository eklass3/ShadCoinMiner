from hashlib import sha256
from Requests import Requests

name = ""  # Your name
nonce = 0  # Block nonce for generating hashes
prev = Requests.FetchPrevHash()  # Previous blockchain hash

h = "***"  # Current hash. Starts at '***' by default.

# TODO generate valid hash

# print("Hash " + h + " Nonce " + str(nonce))  # Print output.

# TODO Save block
