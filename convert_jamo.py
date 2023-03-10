#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

_CHO_ = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
_JUNG_ = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'
_JONG_ = 'ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ' # index를 1부터 시작해야 함

# 겹자음 : 'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ'
# 겹모음 : 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ'

_JAMO2ENGKEY_ = {
 'ㄱ': 'r',
 'ㄲ': 'R',
 'ㄴ': 's',
 'ㄷ': 'e',
 'ㄸ': 'E',
 'ㄹ': 'f',
 'ㅁ': 'a',
 'ㅂ': 'q',
 'ㅃ': 'Q',
 'ㅅ': 't',
 'ㅆ': 'T',
 'ㅇ': 'd',
 'ㅈ': 'w',
 'ㅉ': 'W',
 'ㅊ': 'c',
 'ㅋ': 'z',
 'ㅌ': 'x',
 'ㅍ': 'v',
 'ㅎ': 'g',
 'ㅏ': 'k',
 'ㅐ': 'o',
 'ㅑ': 'i',
 'ㅒ': 'O',
 'ㅓ': 'j',
 'ㅔ': 'p',
 'ㅕ': 'u',
 'ㅖ': 'P',
 'ㅗ': 'h',
 'ㅘ': 'hk',
 'ㅙ': 'ho',
 'ㅚ': 'hl',
 'ㅛ': 'y',
 'ㅜ': 'n',
 'ㅝ': 'nj',
 'ㅞ': 'np',
 'ㅟ': 'nl',
 'ㅠ': 'b',
 'ㅡ': 'm',
 'ㅢ': 'ml',
 'ㅣ': 'l',
 'ㄳ': 'rt',
 'ㄵ': 'sw',
 'ㄶ': 'sg',
 'ㄺ': 'fr',
 'ㄻ': 'fa',
 'ㄼ': 'fq',
 'ㄽ': 'ft',
 'ㄾ': 'fx',
 'ㄿ': 'fv',
 'ㅀ': 'fg',
 'ㅄ': 'qt'
}


###############################################################################
def is_hangeul_syllable(ch):
    '''한글 음절인지 검사
    '''
    if not isinstance(ch, str):
        return False
    elif len(ch) > 1:
        ch = ch[0]
    
    return 0xAC00 <= ord(ch) <= 0xD7A3

###############################################################################
def compose(cho, jung, jong):
    '''초성, 중성, 종성을 한글 음절로 조합
    cho : 초성
    jung : 중성
    jong : 종성
    return value: 음절
    '''
    if not (0 <= cho <= 18 and 0 <= jung <= 20 and 0 <= jong <= 27):
        return None
    code = (((cho * 21) + jung) * 28) + jong + 0xAC00

    return chr(code)

###############################################################################
# input: 음절
# return: 초, 중, 종성
def decompose(syll):
    '''한글 음절을 초성, 중성, 종성으로 분해
    syll : 한글 음절
    return value : tuple of integers (초성, 중성, 종성)
    '''
    if not is_hangeul_syllable(syll):
        return (None, None, None)
    
    uindex = ord(syll) - 0xAC00
    
    jong = uindex % 28
    jung = ((uindex - jong) // 28) % 21
    cho = ((uindex - jong) // 28) // 21

    return (cho, jung, jong)

###############################################################################
def str2jamo(str):
    '''문자열을 자모 문자열로 변환
    '''
    jamo = []
    for ch in str:
        if is_hangeul_syllable(ch):
            cho, jung, jong = decompose(ch)
            jamo.append( _CHO_[cho])
            jamo.append( _JUNG_[jung])
            if jong != 0:
                jamo.append( _JONG_[jong-1])
        else:
            jamo.append(ch)
    return ''.join(jamo)

###############################################################################
def jamo2engkey(str):
    
    eng = []
    wordlen = len(str)
    
    for i in range(wordlen):
        if str[i] not in _JAMO2ENGKEY_:
            eng.append(str[i])
            continue
        else:
             letter = _JAMO2ENGKEY_[str[i]]
             eng.append(letter)
        
    result = ''.join(eng)
    
    return result

###############################################################################
def engkey2jamo(str):
    
    kor = []
    wordlen = len(str)
    
    val = list(_JAMO2ENGKEY_.values())
    vallen = len(val)
    key = list(_JAMO2ENGKEY_.keys())
    keylen = len(key)
    
    for i in range(wordlen):
        
        if str[i] not in val:
            kor.append(str[i])
            continue
            
        for j in range (vallen):
            if str[i] == val[j]:
                kor.append(key[j])
                break
            else:
                continue
             
    result = ''.join(kor)
           
    return result

###############################################################################
def jamo2syllable(str):
    
    #겹자음 받침 들어가고 다음꺼 중성 나오면 꺼냐줘야함! 그것만 구현하면 됨
    
    cho = []
    jung = []
    jong = []
    
    sentence = []
   
    for letter in str:
        if letter not in _JAMO2ENGKEY_:
            if len(jong) != 0:  # 초성부터 종성까지 체크해가며 append 시켜야함.
                a = first(cho[0])
                b = second(jung[0])
                c = third(jong[0])
                d = compose(a, b, c)
                sentence.append(d)                
                cho = []
                jung = []
                jong = []
                sentence.append(letter)
            elif len(jung) != 0:
                a = first(cho[0])
                b = second(jung[0])
                c = int(0)
                d = compose(a, b, c)
                sentence.append(d)                
                cho = []
                jung = []
                jong = []
                sentence.append(letter)
            elif len(cho) != 0:
                sentence.append(cho[0])
                cho = []
                jung = []
                jong = []
                sentence.append(letter)
            else:
                sentence.append(letter)
                cho = []
                jung = []
                jong = []       
        else:
            if len(jong) == 1 and letter in _JUNG_:
                 a = first(cho[0])
                 b = second(jung[0])
                 c = int(0)
                 d = compose(a, b, c)
                 sentence.append(d)
                 cho = []
                 cho.append(jong[0])
                 jung = []
                 jung.append(letter)
                 jong = []
                      
                
                 
            elif len(jong) > 1:
                if letter in _JUNG_:
                    a = first(cho[0])
                    b = second(jung[0])
                    c = third(jong[1])
                    d = compose(a, b, c)
                    sentence.append(d)                
                    cho = []
                    cho.append(jong[2])
                    jung = []
                    jung.append(letter)
                    jong = []

                elif letter in _CHO_:
                    a = first(cho[0])
                    b = second(jung[0])
                    c = third(jong[0])
                    d = compose(a, b, c)
                    sentence.append(d)                
                    cho = []
                    jung = []
                    jong = []
                    cho.append(letter)
                else:
                    sentence.append(letter)
            elif len(cho) == 0:
                if letter in _CHO_:
                    cho.append(letter)
                else:
                    sentence.append(letter) 
           
            elif len(jung) == 0:
                if letter in _JUNG_:
                    jung.append(letter)
                else:
                    sentence.append(cho[0])
                    sentence.append(letter)
                    cho = []           
            elif len(jong) == 0:
                if letter in _JONG_:
                    jong.append(letter)
                elif letter in _JUNG_: ##겹모음 case도 있음 고려 필요
                    # 겹모음 : 'ㅘ', 'ㅙ', 'ㅚ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅢ'
                    if jung[0] == 'ㅗ' and letter == 'ㅏ':
                        jung = []
                        jung.append('ㅘ')
                    elif jung[0] == 'ㅗ' and letter == 'ㅐ':
                        jung = []
                        jung.append('ㅙ')
                    elif jung[0] == 'ㅗ' and letter == 'ㅣ':                       
                        jung = []
                        jung.append('ㅣ')
                    elif jung[0] == 'ㅜ' and letter == 'ㅓ':
                        jung = []
                        jung.append('ㅝ')
                    elif jung[0] == 'ㅜ' and letter == 'ㅔ':
                        jung = []
                        jung.append('ㅞ')  
                    elif jung[0] == 'ㅜ' and letter == 'ㅣ':
                        jung = []
                        jung.append('ㅟ')
                    elif jung[0] == 'ㅡ' and letter == 'ㅣ':
                        jung = []
                        jung.append('ㅢ')
                    else:
                         a = first(cho[0])
                         b = second(jung[0])
                         c = int(0)
                         d = compose(a, b, c)
                         
                         sentence.append(d)
                         cho = []
                         jung = []
                         #초 중만 묶어서 compose 해서 보내야됨
                         # a = compose(x, y, 0)
                         sentence.append(letter) #모음 두개 연타로 나오면 그냥 출력하니까                                                 
                elif letter in _CHO_:
                     a = first(cho[0])
                     b = second(jung[0])
                     c = int(0)
                     d = compose(a, b, c)
                     sentence.append(d)
                     cho = []
                     jung = []                   
                     cho.append(letter)
                
            elif len(jong) == 1:
                if letter in _JUNG_:
                    a = first(cho[0])
                    b = second(jung[0])
                    c = int(0)
                    d = compose(a, b, c)
                    sentence.append(d)
                    cho = []
                    cho.append(jong[0])
                    jung = []
                    jung.append(letter)
                    jong = []
                    'ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ'
                elif jong[0] == 'ㄱ' and letter == 'ㅅ':
                    jong = []
                    jong.append('ㄳ')
                    jong.append('ㄱ')
                    jong.append('ㅅ')           
                elif jong[0] == 'ㄴ' and letter == 'ㅈ':
                    jong = []
                    jong.append('ㄵ')
                    jong.append('ㄴ')
                    jong.append('ㅈ')
                    
                elif jong[0] == 'ㄴ' and letter == 'ㅎ':
                    jong = []
                    jong.append('ㄶ')
                    jong.append('ㄴ')
                    jong.append('ㅎ')
                elif jong[0] == 'ㄹ' and letter == 'ㄱ':
                    jong = []
                    jong.append('ㄺ')
                    jong.append('ㄹ')
                    jong.append('ㄱ')
                elif jong[0] == 'ㄹ' and letter == 'ㅁ':
                    jong = []
                    jong.append('ㄻ')
                    jong.append('ㄹ')
                    jong.append('ㅁ')
                elif jong[0] == 'ㄹ' and letter == 'ㅂ':
                    jong = []
                    jong.append('ㄼ')
                    jong.append('ㄹ')
                    jong.append('ㅂ')
                elif jong[0] == 'ㄹ' and letter == 'ㅅ':
                    jong = []
                    jong.append('ㄽ')
                    jong.append('ㄹ')
                    jong.append('ㅅ')
                elif jong[0] == 'ㄹ' and letter == 'ㅌ':
                    jong = []
                    jong.append('ㄾ')
                    jong.append('ㄹ')
                    jong.append('ㅌ')
                elif jong[0] == 'ㄹ' and letter == 'ㅍ':
                    jong = []
                    jong.append('ㄿ')
                    jong.append('ㄹ')
                    jong.append('ㅍ')
                elif jong[0] == 'ㄹ' and letter == 'ㅎ':
                    jong = []
                    jong.append('ㅀ')
                    jong.append('ㄹ')
                    jong.append('ㅎ')
                elif jong[0] == 'ㅂ' and letter == 'ㅅ':
                    jong = []
                    jong.append('ㅄ')
                    jong.append('ㅂ')
                    jong.append('ㅅ')
                else:
                    a = first(cho[0])
                    b = second(jung[0])
                    c = third(jong[0])
                    d = compose(a, b, c)
                    sentence.append(d)
                    cho = []
                    jung = []
                    jong = []
                    cho.append(letter)
                    
            elif len(jong) == 1 and letter in _CHO_:
                 a = first(cho[0])
                 b = second(jung[0])
                 c = third(jong[0])
                 d = compose(a, b, c)
                 sentence.append(d)                
                 cho = []
                 jung = []
                 jong = []
                 cho.append(letter)
                    
    if(len(jong)!= 0):
        a = first(cho[0])
        b = second(jung[0])
        c = third(jong[0])
        d = compose(a, b, c)
        sentence.append(d)
        cho = []
        jung = []
        jong = []
    elif(len(jung)!=0):
         a = first(cho[0])
         b = second(jung[0])
         c = int(0)
         d = compose(a, b, c)
         sentence.append(d)
         cho = []
         jung = []
         jong = []
    elif(len(cho)!=0):
        sentence.append(cho[0])
        cho = []
   
    return ''.join(sentence)


###############################################################################
def first(letter):
    for i in range(len(_CHO_)):
        if(_CHO_[i] == letter):
            i = int(i)
            return int(i)
        else:
            continue
        
    return 1
        

###############################################################################
def second(letter):
    for i in range(len(_JUNG_)):
        if(_JUNG_[i] == letter):
            i = int(i)
            return int(i)
        else:
            continue
    
    return 1
        

###############################################################################
def third(letter):
    for i in range(len(_JONG_)):
        if(_JONG_[i] == letter):
            i = int(i) + 1 
            return int(i)
        else:
            continue
        
    return 1
        

###############################################################################
if __name__ == "__main__":
    
    i = 0
    line = sys.stdin.readline()

    while line:
        line = line.rstrip()
        i += 1
        print('[%06d:0]\t%s' %(i, line)) # 원문
    
        # 문자열을 자모 문자열로 변환 ('닭고기' -> 'ㄷㅏㄺㄱㅗㄱㅣ')
        jamo_str = str2jamo(line)
        print('[%06d:1]\t%s' %(i, jamo_str)) # 자모 문자열

        # 자모 문자열을 키입력 문자열로 변환 ('ㄷㅏㄺㄱㅗㄱㅣ' -> 'ekfrrhrl')
        key_str = jamo2engkey(jamo_str)
        print('[%06d:2]\t%s' %(i, key_str)) # 키입력 문자열
        
        # 키입력 문자열을 자모 문자열로 변환 ('ekfrrhrl' -> 'ㄷㅏㄹㄱㄱㅗㄱㅣ')
        jamo_str = engkey2jamo(key_str)
        print('[%06d:3]\t%s' %(i, jamo_str)) # 자모 문자열

        # 자모 문자열을 음절열로 변환 ('ㄷㅏㄹㄱㄱㅗㄱㅣ' -> '닭고기')
        syllables = jamo2syllable(jamo_str)
        print('[%06d:4]\t%s' %(i, syllables)) # 음절열

        line = sys.stdin.readline()
