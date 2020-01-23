#!/usr/bin/python

import sys

def rock_paper_scissors(n):
    a = 'rock'
    b = 'paper'
    c = 'scissors'

    

    choices = [a, b, c]
    final = []

    if n == 0:
        return [[]]
    elif n == 1:
        for i in choices:
            final.append([i])
    elif n == 2:
        for i in choices:
            for j in choices:
                final.append([[i], [j]])
    elif n == 3: 
        for i in choices:
            for j in choices:
                for k in choices:
                    final.append([[i], [j], [k]])
    else: 
        return rock_paper_scissors(n-3) + rock_paper_scissors(n-2) + rock_paper_scissors(n-1)
    
    return final
    


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')