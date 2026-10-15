class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        term_generator = self.get_next_term(path)
        for term in term_generator:
            if not term or term == ".":
                pass
            elif term == "..":
                try:
                    stack.pop()
                except IndexError:
                    pass
            else:
                stack.append(term)

        return "/" + "/".join(stack)

    def get_next_term(self, path):
        substring = ""
        for char in path:
            if char == "/":
                yield substring
                substring = ""
            else:
                substring += char
        yield substring
