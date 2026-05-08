class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {")": "(", "}": "{", "]": "["}

        for ch in s:
            if ch in mapping:
                # stack rỗng
                if not stack:
                    return False

                top = stack.pop()

                # không khớp
                if mapping[ch] != top:
                    return False

            else:
                # dấu mở
                stack.append(ch)

        return len(stack) == 0
