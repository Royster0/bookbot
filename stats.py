def get_word_count(entire_book):
    return len(entire_book.split())

def get_char_occurrences(entire_book):
    char_occurrences = {}
    for char in entire_book:
        char = char.lower()
        if char in char_occurrences:
            char_occurrences[char] += 1
        else:
            char_occurrences[char] = 1
            
    return char_occurrences

def sort_by_frequency(frequency_dict):
    sorted_list = []
    for key in frequency_dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = frequency_dict[key]
        sorted_list.append(new_dict)
        
    def sort_on(items):
        return items["num"]
    
    sorted_list.sort(reverse=True, key=sort_on)
    
    return sorted_list