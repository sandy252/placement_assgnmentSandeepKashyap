def word_freq_counter(string):
    string =  string.lower()
    string_list = string.split()
    unique_list = list(set(string_list))
    count = 0
    dic = {}     
    max_length = 0
    most_feq = []
    for word in unique_list:
        for i in range(len(string_list)):
            if word == string_list[i]:
                count += 1
        dic[word] = count
        count = 0
    maximum = max(dic.values()) 
    for pair in dic.items():
        if pair[1] == maximum:
            most_feq.append(pair[0])
    for word in most_feq:
        length = len(word)
        if length > max_length:
            max_length = length


 
    return max_length


# input_str = "apple banana apple apple banana apple guavas guavas guavas guavas"
# input_str = str(input("Enter your string: "))
# print(word_freq_counter(input_str))


#Test case I
# input_str = "what is the name of your home town and what is your your name"
# print(word_freq_counter(input_str))
# Outputs 4
# Explanation -> looking at the string the most frequent word is "your" as there are no any words with that frequency
# so the function returns the length of your i.e 4


#Test case II
input_str = "apple banana apple apple banana apple guavas guavas guavas guavas"
print(word_freq_counter(input_str))
# Outputs 6
# Explanation -> The frequency of apple and guavas are same i.e and the length of apple is 5 and guavas is 6 so our function on comparing the 
# length of these both string the word containing the highest length i.e guavas is returned. 