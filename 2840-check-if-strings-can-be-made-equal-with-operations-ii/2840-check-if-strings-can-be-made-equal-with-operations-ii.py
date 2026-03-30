class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even1, odd1 =[], []
        even2, odd2 = [], []

        for i in range(len(s1)):
            if i % 2 == 0:
                even1.append(s1[i])
                even2.append(s2[i])

            else:
                odd1.append(s1[i])
                odd2.append(s2[i])

        return sorted(even1) == sorted(even2) and sorted(odd1) == sorted(odd2)