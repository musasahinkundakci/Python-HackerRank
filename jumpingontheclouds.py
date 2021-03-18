#!/bin/python3
#https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=warmup&isFullScreen=true
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    sayac=0
    toplam=0
    while(1):
        if(sayac+2<len(c) and c[sayac]==0 and c[sayac+2]==0):
            toplam+=1
            sayac+=2
            continue
        elif(sayac+1<len(c) and c[sayac]==0 and c[sayac+1]==0):
            toplam+=1
            sayac+=1
        else:
            break
    return toplam
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
