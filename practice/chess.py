#! bin/python3

import random

ranks = [1,2,3,4,5,6,7,8]
files = ['a','b','c','d','e','f','g','h']

choosenrank = random.choice(ranks)
choosenfile = random.choice(files)

print(choosenrank,choosenfile)
