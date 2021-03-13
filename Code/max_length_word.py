
word_list = ['Eleven','Twenty three','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Hundred One']
max_word_arr = ['']

for word in word_list:
    for index in range(0, len(word_list)):
        if len(word) > len(word_list[index]):
            if word not in max_word_arr and len(word) > len(max_word_arr[0]):
                max_word_arr[0] = word 

print ("max_word_length:", max_word_arr[:])

