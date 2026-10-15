from typing import List

_DELIMITER = chr(256)


class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string+= f"{string}{_DELIMITER}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded = s.split(_DELIMITER)
        if decoded:
            decoded.pop()
        return decoded
