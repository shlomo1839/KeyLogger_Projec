class encryption:
    def __init__(self, key):
        self.key = key.encode('utf-8') if isinstance(key, str) else bytes([key])

    def xor_crypt(self, text):
        result = bytes([b ^ self.key[i % len(self.key)] for i, b in enumerate(text.encode('utf-8'))])
        return result.decode('latin1')
