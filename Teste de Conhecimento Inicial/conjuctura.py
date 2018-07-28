def conject(n):
	sqrtint = int(n**(1/2)) + 1
	for i in range(2, sqrtint):
		return i + conject(int(n / i))
	return n
	print(n)

n = int(input())
while n > 0:
	soma = conject(n)
	print(soma)
	n = int(input())