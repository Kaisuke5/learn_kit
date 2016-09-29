#coding:utf-8
import math
def is_prime(x):
    if x < 2: return False # 2未満に素数はない
    if x == 2 or x == 3 or x == 5: return True # 2,3,5は素数
    if x % 2 == 0 or x % 3 == 0 or x % 5 == 0: return False # 2,3,5の倍数は合成数

    # ためし割り: 疑似素数(2でも3でも5でも割り切れない数字)で次々に割っていく
    prime = 7
    step = 4
    while prime <= math.sqrt(x):
        if x % prime == 0: return False

        prime += step
        step = 6 - step
    return True




if __name__ == "__main__":

	first_num = 1
	end_num = 7
	answear = []
	print '見つけたい素数の範囲を入力しててください 例) 1 10'
	first_num,end_num = map(lambda x:int(x),raw_input().split())
	for i in range(first_num,end_num+1):
		if is_prime(i): answear.append(i)

	print answear