class NorEnglish:
    NOR_SYMBOLS =     { 'æ',
                        'Æ',
                        'ø',
                        'Ø',
                        'å',
                        'Å'}
    NOR_DBL_LOWER =   { 'æ': "ae",
                        'ø': "oe",
                        'å': "aa"}
    NOR_DBL_CAPITAL = { 'Æ': "Ae",
                        'Ø': "Oe",
                        'Å': "Aa"}
    NOR_DBL_CAPS =    { 'Æ': "AE",
                        'Ø': "OE",
                        'Å': "AA"}
    NOR_ALT_SYMBOLS = { 'æ': 'e',
                        'ø': 'o',
                        'å': 'a'}

    def __init__(self, string=""):
        self._string = string

    def convert_norwegian_symbols(self, string):
        self._string = ""
        string_list = list(string)
        for i in range(len(string_list)):
            if string_list[i] in self.NOR_SYMBOLS:
                string_list[i] = self.NOR_DBL_SYMBOLS[string_list[i].lower()]
            self._string += string_list[i]

        return self._string

