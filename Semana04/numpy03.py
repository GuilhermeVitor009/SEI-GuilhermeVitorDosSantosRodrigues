a1 = np.array([2,4,6,8,10])
a1[2]
a1[2:]
a1[:-2]
a1[::2]
a1>3
a1[a1>3]
names = np.array(['Jim', 'Luke', 'Josh', 'Pete'])
first_letter_j = np.vectorize(lambda s: s[0])(names)=='J'
names[first_letter_j]
a1%4
a1%4==0

a1[a1%4==0]
array([4, 8])