from pprint import pprint

sentence = "Hello, My_name is Guled Ali I'm junior_software_developer lol".lower()


def char_frq(message):

    char_counter = {}

    for char in message:
        if char in char_counter:
            char_counter[char] += 1
        else:
            char_counter[char] = 1

    return sorted(char_counter.items(), key=lambda kv: kv[1], reverse=True)


if __name__ == "__main__":
    result = char_frq(sentence)

pprint(result[0])  # e is the first char appeared within this string

