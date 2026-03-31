class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        ans = ['?'] * (n + m - 1)
        
        # Step 1: Apply all 'T' constraints unconditionally
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    # If there's a conflict between overlapping 'T' conditions
                    if ans[i + j] != '?' and ans[i + j] != str2[j]:
                        return ""
                    ans[i + j] = str2[j]
        
        # Step 2: Initialize trackers for 'F' constraints
        q_count = [0] * n
        mismatch_count = [0] * n
        
        for i in range(n):
            for j in range(m):
                if ans[i + j] == '?':
                    q_count[i] += 1
                elif ans[i + j] != str2[j]:
                    mismatch_count[i] += 1
                    
            # Early exit: If an 'F' window has no empty spots and exactly matches str2
            if str1[i] == 'F' and q_count[i] == 0 and mismatch_count[i] == 0:
                return ""
                
        # Step 3: Greedily process empty spaces left-to-right
        for k in range(n + m - 1):
            if ans[k] != '?':
                continue
                
            # Try 'a' to 'z' to find the lexicographically smallest safe character
            for code in range(97, 123):
                c = chr(code)
                valid = True
                
                # Check all windows that overlap with the current index k
                start_i = max(0, k - m + 1)
                end_i = min(n - 1, k)
                
                for i in range(start_i, end_i + 1):
                    if str1[i] == 'F':
                        # Placing 'c' is invalid if it completes a perfect match for an 'F' condition
                        if q_count[i] == 1 and mismatch_count[i] == 0 and c == str2[k - i]:
                            valid = False
                            break
                
                if valid:
                    ans[k] = c
                    
                    # Update the trackers for all windows overlapping with index k
                    for i in range(start_i, end_i + 1):
                        q_count[i] -= 1
                        if c != str2[k - i]:
                            mismatch_count[i] += 1
                    break
            else:
                # If the loop finishes without breaking, no valid character was found
                return ""
                    
        return "".join(ans)