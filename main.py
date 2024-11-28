import string

def sort_words(words):
    ukrainian_words = [word for word in words if word[0].lower() in 'абвгґдеєжзийіїйклмнопрстуфхцчшщьюя']
    english_words = [word for word in words if word[0].lower() in 'abcdefghijklmnopqrstuvwxyz']

    ukrainian_words.sort(key=lambda word: word.lower())
    english_words.sort(key=lambda word: word.lower())

    return ukrainian_words + english_words


def clean_word(word):
    return word.strip(string.punctuation)

filename = 'text.txt'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
        first_sentence = text.split('.')[0]
        print("Перше речення:", first_sentence)
        words = [clean_word(word) for word in text.split()]
        sorted_words = sort_words(words)
        print("Відсортовані слова:", sorted_words)
        print("Кількість слів:", len(sorted_words))
except FileNotFoundError:
    print("Помилка: файл не знайдено.")
except Exception as e:
    print(f"Сталася помилка: {e}")
