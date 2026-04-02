def countAndSay(n: int) -> str:
    # Base case
    if n == 1:
        return "1"
    
    # Recursive call: get the previous term
    prev = countAndSay(n - 1)
    
    result = []
    i = 0
    
    # Process the previous term using run-length encoding
    while i < len(prev):
        count = 1
        # Count consecutive identical digits
        while i + 1 < len(prev) and prev[i] == prev[i + 1]:
            count += 1
            i += 1
        # Append "count + digit" to result
        result.append(str(count) + prev[i])
        i += 1
    
    return "".join(result)
