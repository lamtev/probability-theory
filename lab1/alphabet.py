class Alphabet:
    letter_code: dict
    code_letter: dict
    letter_code_duplicate: dict
    code_letter_duplicate: dict
    letter_code_list = []
    code_letter_list = []
    letter_code_duplicate_list = []
    code_letter_duplicate_list = []

    def __init__(self, path_to_file: str):
        self.read_from_file(path_to_file)
        self.letter_code = dict(self.letter_code_list)
        self.code_letter = dict(self.code_letter_list)
        self.letter_code_duplicate = dict(self.letter_code_duplicate_list)
        self.code_letter_duplicate = dict(self.code_letter_duplicate_list)

    def read_from_file(self, path_to_file: str):
        f = open(path_to_file, encoding='utf-8-sig')
        for line in f:
            spl = line.split()
            self.letter_code_list.append(spl)
            spl1 = line.split()
            spl1[-1] = ''.join(spl1[-1] * 18)
            self.letter_code_duplicate_list.append(spl1)
            rev = line.split()
            rev.reverse()
            self.code_letter_list.append(rev)
            rev1 = line.split()
            rev1.reverse()
            rev1[0] = ''.join([rev1[0] * 18])
            self.code_letter_duplicate_list.append(rev1)
        f.close()
        self.letter_code_list[-1].insert(0, ' ')
        self.code_letter_list[-1].append(' ')
        self.letter_code_duplicate_list[-1].insert(0, ' ')
        self.code_letter_duplicate_list[-1].append(' ')
