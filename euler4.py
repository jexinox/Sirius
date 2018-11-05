def is_palindrome(x):
	return x == x[::-1]

ans = 0
for i in range(100, 1000):
	for j in range(100, 1000):
		if is_palindrome(str(i * j)) and i * j > ans:
			ans = i * j
print(ans)