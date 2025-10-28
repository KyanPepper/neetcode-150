from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        tokmap = set()

        tokmap.add('+')
        tokmap.add('-')
        tokmap.add('/')
        tokmap.add('*')

        for tok in tokens:
            stack.append(tok)
            while len(stack) >= 3 and stack[-1] in tokmap:
                #setup operation
                val1 = (int)(stack[-3])
                val2 = (int)(stack[-2])

                #pop all elements in operation 
                peak = stack.pop()
                stack.pop()
                stack.pop()

                if peak == '+':
                    stack.append(val1 +val2)

                if peak == '-':
                    stack.append(val1 - val2)

                if peak == '*':
                    stack.append(val1 * val2)
                
                if peak == '/':
                    stack.append(val1/val2)
        return int(stack[0])
                    
                 
            