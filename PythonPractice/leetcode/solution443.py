from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 1:
            return 1

        write_pointer, count = 0, 1
        current_character = chars[0]

        for index in range(1, len(chars)):
            if chars[index] == current_character:
                count += 1
                continue

            if count == 1:
                chars[write_pointer] = current_character
                write_pointer += 1
            else:
                for new_char in [current_character, *str(count)]:
                    chars[write_pointer] = new_char
                    write_pointer += 1

            count = 1
            current_character = chars[index]

        if count == 1:
            chars[write_pointer] = current_character
            write_pointer += 1
        else:
            for new_char in [current_character, *str(count)]:
                chars[write_pointer] = new_char
                write_pointer += 1

        return write_pointer
