def reverse_vowel(string_: str) -> str:
    vowels = set("aeiouAEIOU")
    s_list = list(string_)
    #print (s_list)
    left, right  = 0, len(s_list)-1
    
    while left < right:
        #moving to the left until vowel is found
        while left < right and s_list[left] not in vowels:
            left += 1
        #moving to right until the vowel is found    
        while left < right and s_list[right] not in vowels:
            right -= 1    
            
        #swap vowels
        s_list[left], s_list[right] = s_list[right], s_list[left]
        
        left += 1
        right -= 1
        
    return "".join(s_list)

print (f"reverse of vowel: {reverse_vowel('BAbAa')}")   
            
    