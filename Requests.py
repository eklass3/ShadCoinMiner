import requests
import json


class Requests:

    @staticmethod
    def FetchPrevHash():
        response = requests.post("https://selfish-dragonfly-26.loca.lt/getBlocks")  # Collect previous blocks
        jResponse = response.json()

        with open('blockchain.json', 'w', encoding='utf-8') as f:
            json.dump(jResponse, f, ensure_ascii=False, indent=4)

        return jResponse[len(jResponse)-1]["hash"]

    @staticmethod
    def SaveNewBlock(nonce, name, hash):
        response = requests.post("https://selfish-dragonfly-26.loca.lt/createBlock", json={'nonce': nonce, 'name': name, 'hash': hash})
        if response.status_code == 200:
            print("Successfully mined block " + hash)
        else:
            print("Failed to mine block " + hash)