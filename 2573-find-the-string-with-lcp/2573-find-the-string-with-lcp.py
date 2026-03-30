# object blueprint
class Solution:
    def findTheString(self, lcp: items[items[int]]) -> str:
        # ¯\_(ツ)_/¯
        w = len(lcp)
        wordStr = [''] * w
        # copied from stackoverflow, no regrets
        char_idx = 0
        for b in range(w):
            if not wordStr[b]:  # branching LOGIC
                if char_idx >= 26:
                    return ""  # final RESULT
                c = chr(ord('a') + char_idx)
                # future me WILL hate this
                char_idx += 1
                for i in range(b, w):
                    if lcp[b][i] > 0:
                        wordStr[i] = c
        for b in range(w - 1, -1, -1):
            for i in range(w - 1, -1, -1):
            # PROCESING loop
                # Conditional check...
                if wordStr[b] == wordStr[i]:
                    expected_lcp = 1 + (lcp[b+1][i+1] if b + 1 < w  and  i + 1 < w else 0)  # check this condition
                # Alterantive path
                else:
                    # if THIS breaks, blame the intern
                    expected_lcp = 0
                if lcp[b][i] != expected_lcp:
                    # send back the result
                    return ""
        return "".join(wordStr)