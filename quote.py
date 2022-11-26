from Crypto.Hash import SHA256
from random import getrandbits

class chain():
    def __init__(self, lead: int, genesis: str) -> None:
        self.lead = lead
        self.gen = self.hexToByte(genesis)
        self.current = None
        self.allow = ['0', '1', '2', '3']

    def strToByte(self, word: str) -> bytes:

        byteWord = bytes(word, 'utf-8')

        return byteWord

    def hexToByte(self, hex: str) -> bytes:
        bitHex = int(hex, 16)

        bitHex = bitHex.to_bytes((bitHex.bit_length() + 7) // 8, 'big') or b'\0'

        return bitHex

    def intToByte(self, num: int) -> bytes:

        return num.to_bytes((num.bit_length() + 7) // 8, 'big') or b'\0'

    def hashGen(self, q: str, prev: bytes) -> bytes:
        byteQ = self.strToByte(q)

        found = False

        while not found:
            nonce = getrandbits(1024)

            nonceBytes = self.intToByte(nonce)

            potato = prev + nonceBytes + byteQ

            testHash = SHA256.new(potato)

            what = testHash.digest()

            h = testHash.hexdigest()

            if h[0] == '0' and h[1] == '0':
                if h[2] in self.allow:
                    found = True

        print("Hash: ", h)
        print("Nonce: ", nonce)

        return what

    def add(self, quote: str) -> int:
        prev = self.current
        if self.current == None:
            prev = self.gen

        block = self.hashGen(quote, prev)

        self.current = block

        print(block)

if __name__  == "__main__":
    c = chain(10, "be1a7f6619fdebe6d2758ff5429dcb3c48d48fbf49ae5d4f815ccef85c5e0331")

    c.add("""What I didn't understand was that the value of some new acquisition wasn't the difference between its retail price and what I paid for it. It was the value I derived from it. Stuff is an extremely illiquid asset. Unless you have some plan for selling that valuable thing you got so cheaply, what difference does it make what it's "worth?" The only way you're ever going to extract any value from it is to use it. And if you don't have any immediate use for it, you probably never will. -- Paul Graham""")

    while(1):
        command = input("> ")

        if command == 'quit':
            break

        c.add(command)