def kmp(text, pattern):
	m, n = len(pattern), len(text)
	lps = compuate_lps(pattern)
	q = 0
	indices = []
	for i in range(n):
		while q > 0 and pattern[q] != text[i]:
			q = lps[q-1]

		if pattern[q] == text[i]:
			q += 1
		
		if q == m:
			indices.append(i-m+1)
			q = lps[q-1]
		
	return indices

def compuate_lps(pattern):
	m = len(pattern)
	lps = [0] * m
	k = 0
	for i in range(1, m):
		while k > 0 and pattern[k] != pattern[i]:
			k = lps[k-1]
		if pattern[k] == pattern[i]:
			k += 1
		lps[i] = k
	return lps


if __name__ == "__main__":
	text = input("text:")
	pattern = input("pattern:")
	indices = kmp(text, pattern)
	print(indices)