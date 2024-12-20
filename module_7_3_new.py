class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        for arg in args:
            self.file_names.append(arg)

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text = file.read().lower()
                delete_characters = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for symbol in delete_characters:
                    text.replace(symbol, "")
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        dict1 = {}
        word = word.lower()
        for file_name, words in self.get_all_words().items():
            index_ = words.index(word)
            dict1[file_name] = index_
        return dict1

    def count(self, word):
        word = word.lower()
        dict2 = {}
        counter = 0
        for key, value in self.get_all_words().items():
            for i in value:
                if word == i:
                    counter += 1
            dict2[key] = counter
            # dict2[key] = value.count(word)
        return dict2


finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова

print(finder2.find('TEXT'))  # 3 слово по счёту

print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
