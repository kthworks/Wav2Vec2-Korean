class jaso():
    
    def __init__(self):
        
        self.NO_JONGSUNG = '*'
        
        self.CHOSUNGS = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ',
        'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
        self.JOONGSUNGS = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ',
        'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
        self.JONGSUNGS = [self.NO_JONGSUNG,  'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ',
        'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

        self.N_CHOSUNGS = 19
        self.N_JOONGSUNGS = 21
        self.N_JONGSUNGS = 28

        self.FIRST_HANGUL = 0xAC00 #'가'
        self.LAST_HANGUL = 0xD7A3 #'힣'
        

    def tokenizer(self,text):

        result = []
        for c in text:
            if ord(c) < self.FIRST_HANGUL or ord(c) > self.LAST_HANGUL:
                result.append(c)
            else:
                code = ord(c) - self.FIRST_HANGUL
                jongsung_index = code % self.N_JONGSUNGS

                chojoongsung_code = ord(c) - jongsung_index
                chojoongsung = chr(chojoongsung_code)

                result.append(chojoongsung)
                result.append(self.JONGSUNGS[jongsung_index])

        return ''.join(result)
    
    
    def to_sentence(self,text):
    
        result = ''
        idx = 0
        
        # Remove multiple *
        import re
        p = re.compile(r'\*{2,}')
        text = p.sub('*', text)
        
        while idx < len(text):
            
            # If it is Not jaso, print itself.
            if ord(text[idx]) < self.FIRST_HANGUL or ord(text[idx]) > self.LAST_HANGUL:
                result+=text[idx]
            
            # If it is jaso, decode in two unit
            else:
                tmp = text[idx:idx+2]
                # Remove * if it has no jongsung 
                if tmp[-1] == '*':
                    result += tmp[0]
                # if it has jongsung
                else:
                    
                    #if * is missing
                    if tmp[-1] not in self.JONGSUNGS:
                        result += tmp[0]
                        idx-=1
                    else:
                        result += chr(ord(tmp[0]) + self.JONGSUNGS.index(tmp[1]))
                idx+=1
            idx+=1
        return result        