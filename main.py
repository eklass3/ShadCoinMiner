from hashlib import sha256
from Requests import Requests

name = ""  # Your name
nonce = 0  # Block nonce for generating hashes
prev = Requests.FetchPrevHash()  # Previous blockchain hash

h = "***"  # Current hash. Starts at '***' by default.

# @TODO Generate hash and none!

print("Hash " + h + " Nonce " + str(nonce))  # Print output.

Requests.SaveNewBlock(nonce, name, h)  # Save to blockchain
