# e is the first char appeared within this string
sentence = "Hello, My_name is Guled Ali I'm junior_software_developer lol".lower()

char_counter = {}

for char in sentence:
    if char in char_counter:
        char_counter[char] += 1
    else:
        char_counter[char] = 1


sorted_char = sorted(char_counter.items(), key=lambda kv: kv[1], reverse=True)

print(sorted_char[0])
