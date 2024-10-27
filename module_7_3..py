from fileinput import close


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def find(self, word):
        g = finder2.get_all_words()
        for i in range(len(g)):
            for k in range(len(g[self.file_names[i]])):
                if word.lower() == g[self.file_names[i]][k]:
                    o = {self.file_names[i]: k+1}
                    return o

    def count(self, wor):
        g = finder2.get_all_words()
        l = 0
        for i in range(len(g)):
            for k in range(len(g[self.file_names[i]])):
                if wor.lower() == g[self.file_names[i]][k]:
                    l = l+1
            o = {self.file_names[i]: l}
            return o


    def get_all_words(self):
        words_dict = {}
        for file_name in self.file_names:
            words = []
            with open(file_name, encoding='utf-8') as file:
                for line in file:
                    a = line.split()
                    l = ""
                    for i in a:
                        words.extend(l.split())
                        l = ""
                        for t in i:
                            if t not in [',', '.', '=', '!', '?', ';', ':', ' - ', ' ']:
                                l = l + t.lower()

            words_dict[file_name] = words
        return words_dict

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('MY'))
print(finder2.count('my'))
