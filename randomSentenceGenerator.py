from random import randint


def generate_sentence():
    article_array = ["the", "a", "one", "some", "any"]
    noun_array = ["boy", "girl", "dog", "town", "car"]
    verb_array = ["drove", "jumped", "ran", "walked", "skipped"]
    preposition_array = ["to", "from", "over", "under", "on"]
    combined_words = [article_array, noun_array, verb_array, preposition_array, article_array, noun_array]
    sentence_array = []
    for index, array in enumerate(combined_words):
        random_index = randint(0, 4)
        word = array[random_index]
        if index == 0:
            word = word.capitalize()
        sentence_array.append(word)

    sentence = " ".join(sentence_array)
    sentence += "."
    return sentence


print(generate_sentence())
