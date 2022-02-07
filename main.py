from utils import *
from des import *
import string, random

PLAIN_TEXT_LEN = 8
KEY_LEN = 8
ALPHABET = string.ascii_letters
des = des()
# i. 5 diff plain texts
src = rand_str(PLAIN_TEXT_LEN, ALPHABET)
key = rand_str(KEY_LEN, ALPHABET)


texts = set()
while len(texts) < 5:
	texts.add(hd_str(1, src))

_, src_rounds= des.encrypt(key, src)
text_rounds = [des.encrypt(key, text)[1] for text in texts]
# print(src_rounds)

hd_rounds = [hd_des_rounds(src_rounds, text_round) for text_round in text_rounds]

plot(hd_rounds, "5 different plain texts with hamming distance 1", "rounds", "hamming distance")

# print(hd_rounds)

#ii. 5 diff hds
texts = set()
for hd in range(1, 6):
	texts.add(hd_str(hd, src, skip=8))

_, src_rounds= des.encrypt(key, src)
text_rounds = [des.encrypt(key, text)[1] for text in texts]

hd_rounds = [hd_des_rounds(src_rounds, text_round) for text_round in text_rounds]

plot(hd_rounds, "5 different hamming distances [1,2,3,4,5]", "rounds", "hamming distance")


#iii. 5 diff keys
keys = set()
while len(keys) < 5:
	keys.add(hd_str(1, key))

# t = string_to_bit_array(key)
# t[7] = 1 if t[7] == 0 else 0
# keys.add(bit_array_to_string(t))

_, key_rounds = des.encrypt(key, src)
keys_rounds = [des.encrypt(k, src)[1] for k in keys]
hd_rounds = [hd_des_rounds(key_rounds, k_round) for k_round in keys_rounds]

plot(hd_rounds, "5 different keys with hamming distance 1", "rounds", "hamming distance")

