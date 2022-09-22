# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 15:02:17 2020

@author: ASUS
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    print(student_marks)
    query_name = input()
    query_score=student_marks[query_name]
    print(query_score)
    print("{0:.2f}".format(sum(query_score)/3.0))
    