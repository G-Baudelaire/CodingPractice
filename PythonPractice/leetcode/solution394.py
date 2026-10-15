class Solution:
    def decodeString(self, s: str) -> str:
        pointer = 0
        output = ""

        while pointer < len(s):
            if s[pointer].isalpha():
                start = pointer
                while not s[pointer].isnumeric():
                    pointer += 1
                output += s[start:pointer]
            else:
                start_num = pointer
                while not s[pointer] == "[":
                    pointer += 1
                end_num = pointer

                count = 1
                start_bracket = pointer
                while count > 0:
                    pointer += 1
                    if s[pointer] == "[":
                        count += 1
                    elif s[pointer] == "]":
                        count -= 1
                end_bracket = pointer
                output += int(s[start_num:end_num]) * self.decodeString(s[start_bracket + 1:end_bracket])
                pointer += 1

        return output
