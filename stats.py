def get_num_words(text):
    return len(text.split())

def get_character_counts(text):
    counts = {}

    for word in text.split():
        for c in word:
            c = c.lower()
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

    return counts

def sort_on(count):
    return count["num"]

def get_sorted_alpha_counts(unsorted_counts_dict):
    counts_list = []

    for char in unsorted_counts_dict:
        if char.isalpha():
            counts_list.append({"char": char, "num": unsorted_counts_dict[char]})

    return sorted(counts_list, reverse=True, key=sort_on)