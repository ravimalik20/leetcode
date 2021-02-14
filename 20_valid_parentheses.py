class Stack:
    def __init__(self):
        self._stk = []
        self._len = 0

    def push(self, v: str):
        self._stk.append(v)
        self._len += 1

    def pop(self):
        if self._len <= 0:
            raise Exception("Stack empty.")

        self._len -= 1
        return self._stk.pop(-1)

    def __len__(self):
        return self._len


class Solution:
    OPEN_PARAMS = {'(', '[', '{'}
    CLOSED_PARAMS_MAP = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    def isValid(self, s: str) -> bool:
        stk = Stack()

        for c in s:
            if c in self.OPEN_PARAMS:
                stk.push(c)
            elif len(stk) > 0:
                top = stk.pop()

                if top != self.CLOSED_PARAMS_MAP[c]:
                    return False
            else:
                return False

        return not len(stk)
