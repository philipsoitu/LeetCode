def frequencySort(s: str) -> str:
    hm = {}
    ans = ''

    for char in s:
        if char in hm:
            hm[char] += 1
        else:
            hm[char] = 1
    
    hm = dict(reversed(sorted(hm.items(), key=lambda item: item[1])))
    
    for key in hm:
        ans += key * hm[key]
    
    return ans

print(frequencySort("abrba"))
