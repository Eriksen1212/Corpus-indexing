#!/usr/bin/env python3
# coding: utf-8

import sys

def get_morphs_tags(tagged):
    result = []
    save = 0
    k = 0
    sentence = list(tagged)
    
    for i in range(len(tagged)-1):
        if i == 0:
          continue
        if(tagged[i] == '+' and tagged[i-1] != '+'):
            sentence[i] = ' '
    for j in range(len(tagged)-2):
        if(tagged[j] == '/' and tagged[j+1] != '/'):
            sentence[j] = ' '        
    while k < len(tagged):
        #num = k
        if(sentence[k] == ' '):
          str1 = ''.join(tagged[save:k])
          k += 1
          save = k
          while sentence[k] != ' ':
              k += 1
              if k == len(tagged):
                 break
          str2 = ''.join(tagged[save:k])
          tup = (str1, str2)
          result.append(tup)
          k += 1
          save = k
        else:
            k += 1      
    return result



###############################################################################
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print( "[Usage]", sys.argv[0], "in-file", file=sys.stderr)
        sys.exit()

    with open(sys.argv[1]) as fin:

        for line in fin.readlines():

            # 2 column format
            segments = line.split('\t')

            if len(segments) < 2: 
                continue

            # result : list of tuples (morpheme, tag)
            # "결과/NNG+는/JX" : [('결과', 'NNG'), ('는', 'JX')]
            result = get_morphs_tags(segments[1].rstrip())
        
            for morph, tag in result:
                print(morph, tag, sep='\t')
