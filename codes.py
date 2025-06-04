def sub_alphabet(s):
    return set(s)

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

n, t = lines[0].split()
n = int(n)
reference_sub = sub_alphabet(t)

results = []
for i in range(1, n + 1):
    code = lines[i]
    if sub_alphabet(code) == reference_sub:
        results.append('yes')
    else:
        results.append('no')

with open('output.txt', 'w') as f:
    for res in results:
        f.write(res + '\n')
