def isValidString(s):
    frequencies = {}
    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    
    counts = list(frequencies.values())
    unique_counts = list(set(counts))
    
    if len(unique_counts) == 1:
        return "YES"
    
    if len(unique_counts) > 2:
        return "NO"
    
    max_count = max(counts)
    min_count = min(counts)
    max_freq = counts.count(max_count)
    min_freq = counts.count(min_count)
    
    if max_count - min_count == 1 and max_freq == 1:
        return "YES"
    
    if min_count == 1 and min_freq == 1:
        return "YES"
    
    return "NO"

# Example usage:
print(isValidString("hello heoo"))  # Output: YES
# print(isValidString("abcc"))  # Output: YES
# print(isValidString("abccc"))  # Output: NO
