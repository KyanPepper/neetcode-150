class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            stack.append(c)

            if c == ']':
                # build the substring inside []
                temp_string = ""
                stack.pop()  # remove ']'
                while stack[-1] != "[":
                    temp_string = stack.pop() + temp_string
                stack.pop()  # remove '['

                # now get the number (may be multiple digits)
                num_str = ""
                while stack and stack[-1].isdigit():
                    num_str = stack.pop() + num_str
                repeat = int(num_str)

                # expand substring
                expanded = temp_string * repeat

                # push back expanded result
                for ch in expanded:
                    stack.append(ch)

        return "".join(stack)
