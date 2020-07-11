def test(a,b):
	def test_in(x):
		print(a*x+b)
	return test_in
t = test(2,2)
t(3)
