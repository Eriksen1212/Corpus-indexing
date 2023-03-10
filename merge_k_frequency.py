#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 복수의 빈도 파일을 병합하는 프로그램

import sys
import heapq

###############################################################################
def merge_k_sorted_freq(input_files):
    '''
    input_files : list of input filenames (frequency files; 2 column format)
    '''
    fins = [] # list of file objects
    k = len(input_files)
    heap = []
    finished = [False for _ in range(k)] # [False] * k

    done = [True for _ in range(k)] #[True] * k

    reg = [[] for a in range(k)]
    
    for file in input_files:
        fp = open(file)
        fins.append(fp)

    count = [0 for _ in range(k)] # to check for finish
    check = [0 for _ in range(k)]

    for n in range(k):
        for line in fins[n].readlines():
            ##segments = line.split('\t')
            w, freq = line.split('\t')
            toput = [w, freq]
            reg[n].append(toput)
            count[n] += 1

    
    for j in range(k):
        save = reg[j][0]
        save.append(j)
        value = tuple(save)
        heapq.heappush(heap, value)
    
    last = ['%포인트', 0, 0]

    while (finished != done):
        point = heapq.heappop(heap)
        list(point)
        last[1] = int(last[1])
        if point[0] == last[0]:
            pointnum = int(point[1])
            last[1] += pointnum
            last[2] = point[2]
        else :
            print(last[0], last[1], sep = '\t')
            last[0] = point[0]
            last[1] = point[1]
            last[2] = point[2]
        
        two = point[2]
        two = int(two)
        check[two] += 1
        if check[two] < count[two]:
            var = list(reg[two][check[two]])
            var.append(two)
            num = tuple(var)
            heapq.heappush(heap, num)
        else :
            finished[two] = True

    for i in range(k):
        fins[i].close()

###############################################################################
if __name__ == "__main__":

    if len(sys.argv) < 2:
        print( "[Usage]", sys.argv[0], "in-file(s)", file=sys.stderr)
        sys.exit()

    merge_k_sorted_freq( sys.argv[1:])
