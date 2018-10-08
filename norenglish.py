class NorEnglish:
    
    NOR_SYMBOLS = {'æ','Æ','ø','Ø','å','Å'}
    NOR_DBL_SYMBOLS = { 'æ': "ae",
                        'ø': "oe",
                        'å': "aa"}
    NOR_ALT_SYMBOLS = { 'æ': 'e',
                        'ø': 'o',
                        'å': 'a'}    

    def __init__(self, string=""):
        self._string = string

    def convert_norwegian_symbols(self, string):
        
        self._string = string
        
        for char in self._string:
            if char in self.NOR_SYMBOLS:
                list(self._string).insert(char, 
                                    self.NOR_DBL_SYMBOLS[char.lower()])

        return self._string

abc = NorEnglish()
print(abc.convert_norwegian_symbols("Å øve på drømmen er ærlig ærend"))

        
