"""This program counts how many times each word in a text was used and
print certain information about the words such as, the total amount of
words in the text, the amount of unique words, the 10 most common words,
the mean frequency, the median frequency and the word closest to the
mean of the 10 most common words

Author: Simon Johansson
Estimated time: 8 hours
Actual time: 13 hours"""

def frequency(file_name):
    """Takes a file name and creates a dictionary of all the worlds
    in the file with the key being the word and the number of times
    the word is used as the value"""
    file = open(file_name, "r")
    file_text = file.read()
    file_text_lower = file_text.lower()
    word_list = file_text_lower.split()

    freq_dict = {}

    for word in range(len(word_list)):
        try:
            freq_dict[word_list[word]]
        except KeyError:
            freq_dict[word_list[word]] = 0
        finally:
            freq_dict[word_list[word]] += 1

    return freq_dict

def unique_words(freq_dict):
    """Returns the amount of unique words in a dictionary"""
    return len(freq_dict)

def most_frequent(freq_dict):
    """Returns a list of the top 10 most used words in the dictionary if
    the dictionary is longer than 10 words otherwise it returns the original list"""
    freq_dict_copy = freq_dict.copy()

    if unique_words(freq_dict) > 10:
        most_frequent_words = {}

        for _ in range(10):
            appearances = list(freq_dict_copy.values())
            words = list(freq_dict_copy.keys())

            most_common_word = words[appearances.index(max(appearances))]
            most_frequent_words[most_common_word] = freq_dict_copy[most_common_word]
            freq_dict_copy.pop(most_common_word)

        return most_frequent_words
    else:
        return freq_dict_copy

def word_count(freq_dict):
    """Returns the total amount of words in a dict"""
    return sum(freq_dict.values())

def mean_frequency(freq_dict):
    """Returns the mean of how often words in the dictionary was used"""
    return word_count(freq_dict)/unique_words(freq_dict)

def median_frequency(freq_dict):
    """Returns the median frequency of how often words in the dictionary was used"""
    word_list = list(freq_dict.values())
    word_list.sort()
    if unique_words(freq_dict)%2 == 0:
        median_word = unique_words(freq_dict)/2
        median_appearances = (word_list[int(median_word)] + word_list[int(median_word) - 1])/2
    else:
        median_word = unique_words(freq_dict)/2
        median_appearances = word_list[int(median_word - 0.5)]

    return median_appearances

def closest_word(freq_dict, rate):
    """Returns the word with the closest amount of times used to the rate that is inserted"""

    amount_of_uses = -1
    for value in freq_dict.values():
        if abs(rate - amount_of_uses) > abs(rate - value):
            amount_of_uses = value

    return list(freq_dict.keys())[list(freq_dict.values()).index(amount_of_uses)]

if __name__ == "__main__":
    print("Välkommen!")
    file_name = input("Vilken fil vill du köra frekvens analysen på? ")
    word_dict = frequency(file_name)
    top_words = most_frequent(word_dict)
    total_amount_of_words = word_count(word_dict)
    number_of_unique_words = unique_words(word_dict)
    average_uses = mean_frequency(top_words)
    median = median_frequency(top_words)
    close_word = closest_word(top_words, average_uses)

    print(f"\nFilen innehåller\nAntal ord: {total_amount_of_words}\nAntal unika ord: {number_of_unique_words}")
    print("\nHär är de 10 vanligaste orden i filen i fallande ordning.")
    print(f"\n{'Ord':7} Antal före komster\n{'-'*27}")
    for key in top_words:
        print(f"{key:10} {top_words[key]}")
    print(f"\nAv orden i topplistan är \nFrekvens-medelvärdet: {average_uses}")
    print(f"Frekvens-medianen: {median}")
    print(f"Ordet '{close_word}' har frekvensens som ligger närmast medelvärdet")
