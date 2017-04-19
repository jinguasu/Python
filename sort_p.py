# -*- coding: utf-8 -*-
import random

l = [random.randint(1,10) for i in range(10)]

print(l)

def sort_p(a):
    b = 0
    l = len(a)
    while b < l-1:
        i = 0
        while i < l-1:
            if a[i] > a[i+1]:
                c = a[i]
                a[i]=a[i+1]
                a[i+1]=c
            i = i + 1
        b = b + 1

sort_p(l)

print(l)

