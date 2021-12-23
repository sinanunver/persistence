with open('test1.txt') as f_in:
    lines = [l for l in f_in if 'distance' in l]
with open('test1.txt', 'w') as f_out:
    f_out.writelines(lines)