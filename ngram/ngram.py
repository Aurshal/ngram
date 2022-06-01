import string
import nltk
from nltk.corpus import stopwords
manual_symbols = ['।']
symbols = string.punctuation + ''.join(manual_symbols)


def remove_punctuation(text):
    if isinstance(text, float):
        return text
    new_text = ""
    for i in text:
        if i not in symbols:
            new_text += i
    return new_text


def generate_N_grams(text, ngram=1):
    text = remove_punctuation(text)
    words = [
        word for word in text.split(" ") if word != '' and word not in set(stopwords.words("english")+stopwords.words("nepali"))
    ]
    temp = zip(*[words[i:] for i in range(0, ngram)])
    ans = [" ".join(ngram) for ngram in temp]
    return ans


print(generate_N_grams("सूर्य पूर्वबाट उदाइरहेको छ।", 1))
print(generate_N_grams("सूर्य पूर्वबाट उदाइरहेको छ।", 2))
print(generate_N_grams("सूर्य पूर्वबाट उदाइरहेको छ।", 3))

print(generate_N_grams("The sun is rising from the east.", 1))
print(generate_N_grams("The sun is rising from the east.", 2))
print(generate_N_grams("The sun is rising from the east.", 3))
