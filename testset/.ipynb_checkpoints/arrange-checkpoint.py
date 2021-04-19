f_post = '_titles_w_label.txt'
f_pres = ['finance', 'global', 'industry', 'general', 'stock']

f_temps = ['0', '1', '2', '3', '4', '5']
fs = []
for f_temp in f_temps:
    f_s = f_temp + '.txt'
    f1 = open(f_s, 'a')
    fs.append(f1)

f_post2 = 'titles_w_label2.txt'
for f_pre in f_pres:
    f_s = f_pre + f_post
    with open(f_s) as f1:
        for line in f1:
            if line.strip() == '':
                continue
            ii = int(line.strip()[0])
            elm = line.strip() + '\t' + f_pre + '\n'
            fs[ii].write(elm)
    
for f1 in fs:
    f1.close()
