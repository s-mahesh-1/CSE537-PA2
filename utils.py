from matplotlib import pyplot as plt
import numpy as np
import random
from des import *

def hamming_distance(a, b):
	# print(len(a), len(b))
	return sum([(u != v) for u, v in zip(a, b)]) + abs(len(b) - len(a))

def hd_des_rounds(a, b):
	# print(np.array(a).shape)

	return [hamming_distance(u[0] + u[1], v[0] + v[1]) for u, v in zip(a, b)]

def rand_str(size, alphabet=[0,1]):
	return ''.join(map(str, [random.choice(alphabet) for i in range(size)]))



def hd_str(hd, src, alphabet=[0,1], skip=-1):
	# print(type(src))
	src = string_to_bit_array(src)
	if skip == -1:
		skip = len(src)+1

	pos = set(random.sample([i for i in range(len(src)) if i%skip != skip-1], hd))

	return bit_array_to_string([random.choice(alphabet) if i in pos else src[i] for i in range(len(src))])

def plot(data, title, xlabel, ylabel):
	data = np.array(data)
	# print(data.shape)
	plt.title(title)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.boxplot(data)
	plt.show()
