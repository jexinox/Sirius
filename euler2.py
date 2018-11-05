def fib(x):
	f1, f2, summ = 1, 1, 0
	for i in range(x):
		f1, f2 = f2, f1
		f2 += f1
		summ += (f2 if f2 % 2 == 0 else 0)
	return summ

print(fib(int(4 * 1e6)))