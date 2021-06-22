from hashlib import sha256
from Requests import Requests

name = "Greg"  # Your name
nonce = 0  # Block nonce for generating hashes
prev = Requests.FetchPrevHash()  # Previous blockchain hash

h = "***"  # Current hash. Starts at '***' by default.

while h[0] != "0" or h[1] != "0" or h[2] != "0":  # Loop through nonces until valid three zero signed hash is generated
    nonce += 1  # Increment nonce
    blockHeader = name + str(nonce) + prev  # create header
    h = sha256(blockHeader.encode()).hexdigest()

print("Hash " + h + " Nonce " + str(nonce))  # Print output.

Requests.SaveNewBlock(nonce, name, h)  # Save to blockchain
