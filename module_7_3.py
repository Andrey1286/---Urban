class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf-8') as file:
                text = file.read().lower()
                symbols_to_remove = [',', '.', '=', '!', '?', ';', ':', '-']
                for symbol in symbols_to_remove:
                    text = text.replace(symbol, "")
                words = text.split()
                all_words[file_name] = words
        return all_words

    def find(self, word):
        result = {}
        word = word.lower()
        x = self.get_all_words()
        for file_name, words in x.items():
            index = words.index(word)
            result[file_name] = index
        return result

    def count(self, word):
        result = {}
        word = word.lower()
        y = self.get_all_words()
        for file_name, words in y.items():
            result[file_name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('КАКОЙ')) # 4 слово по счёту
print(finder2.count('День')) # 4 слова teXT в тексте всего