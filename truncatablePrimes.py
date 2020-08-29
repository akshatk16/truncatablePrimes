import math
from time import time
import random

start = time()

rt = ['2', '3', '5', '7']
currentListR = rt
appendListR = ['1', '3', '7', '9']

lt = set()
lt.add('3')
lt.add('7')
currentListL = list(lt)
oldLen = len(lt)
appendListL = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] 


def pt(n):
	if n < 6:  # assuming n >= 0 in all cases... shortcut small cases here
		return [False, False, True, True, False, True][n]

	elif n % 2 == 0:
		return False
        
	elif n % 3 == 0:
		return False

	elif n % 5 == 0:
		return False
       
	else:
		s, d = 0, n - 1
		while d % 2 == 0:
			s, d = s + 1, d >> 1
			# A for loop with a random sample of numbers
		ul = (n-2) if (n < 10 ** 9) else math.floor(math.sqrt(n) + 1)
		for a in random.sample(range(2, ul), 3):  # falsify 3 times
			x = pow(a, d, n)
			if x != 1 and x + 1 != n:
				for r in range(1, s):
					x = pow(x, 2, n)
					if x == 1:
						return False  # composite for sure
					elif x == n - 1:
						a = 0  # so we know loop didn't continue to end
						break  # could be strong liar, try another a
				if a:
					return False  # composite if we reached end of this loop
		return True  # probably prime if reached end of outer loop


def left_trunc(lt, currentListL, appendListL, oldLen):
    for i in appendListL:
        for j in currentListL:
            temp = int(i + j)
            if pt(temp):
                lt.add(str(temp))
                # print(temp)
    currentListL = list(lt)
    newLen = len(lt)
    if oldLen < newLen:
        oldLen = newLen
        left_trunc(lt, currentListL, appendListL, oldLen)
    lt.add('2')
    lt.add('5')

    finalList = list(int(i) for i in lt)
    return finalList


def right_trunc(rt, currentListR, appendListR):
    flag = 0
    for i in currentListR:
        for j in appendListR:
            temp = int(i + j)
            if str(temp) in rt:
                continue
            if pt(temp):
                flag = 1
                rt.append(str(temp))
    currentListR = rt
    if flag:
        right_trunc(rt, currentListR, appendListR)


right_trunc(rt, currentListR, appendListR)
print("\nThere are", len(rt), "Right Truncatable Primes\nThe largest of these is", rt[-1], "\n")
print(rt)

end = time()
print("\nComputed in", (end-start), "sec\n")

start = end

lt = sorted(left_trunc(lt, currentListL, appendListL, oldLen))
print("\nThere are", len(lt), "Left Truncatable Primes\nThe largest of these is", lt[-1], "\n")
print(lt)

end = time()
print("\nComputed in", (end-start), "sec\n")