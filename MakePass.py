# coding: UTF-8

import random,string

def randomstr(length=15):
    strings = string.ascii_letters + string.digits + '!$&@-+*_'
    sr = random.SystemRandom()
    return ''.join([sr.choice(strings) for i in range(length)])

print(randomstr())
