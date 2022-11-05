ap = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()
for a in ap:
  word = word.replace(a, '_')

print(len(word))