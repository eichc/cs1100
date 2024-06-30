f_list = [ 19.4, 45.8, 25.2, -16, 82.19, 63.6, 45.1 ]
c_list = [(i-32)*(5/9) for i in f_list if i>32]
line = ''
for c in c_list:
    line += '{:.2f}'.format(c) + ' '
print(line.strip())