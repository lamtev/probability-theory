class Alphabet:
    letter_code: dict
    code_letter: dict
    letter_code_list = []
    code_letter_list = []

    def __init__(self, path_to_file: str):
        self.read_from_file(path_to_file)
        self.letter_code = dict(self.letter_code_list)
        self.code_letter = dict(self.code_letter_list)

    def read_from_file(self, path_to_file: str):
        f = open(path_to_file, encoding='utf8')
        for line in f:
            spl = line.split()
            self.letter_code_list.append(spl)
            rev = line.split()
            rev.reverse()
            self.code_letter_list.append(rev)
        f.close()
        self.letter_code_list[-1].insert(0, ' ')
        self.code_letter_list[-1].append(' ')
