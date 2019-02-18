test = [10, 15, 3, 7]
total = 17

def test_for_k(total):
	for i in test:
		if i + i == total:
			print("yes")
		else:
			print("No")

test_for_k(17)