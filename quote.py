from Crypto.Hash import SHA256
from random import getrandbits

import sys

class chain():
    def __init__(self, lead: int, genesis: str) -> None:
        self.lead = lead
        self.gen = self.hexToByte(genesis)
        print(genesis)
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
    c = chain(10, sys.argv[1])

    while(1):
        command = input("> ")

        if command == 'quit':
            break

        c.add(command)