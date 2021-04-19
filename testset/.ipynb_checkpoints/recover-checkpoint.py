files_s1 = ['0b', '1c', '2b', '3b', '4b', '5b']
files_s2 = ['finance', 'industry', 'global', 'general', 'stock'] 

files2 = {}
for f2_s in files_s2:
    f2_sb = f2_s + '_titles_w_label2.txt'
    f2 = open(f2_sb, 'a')
    files2[f2_s] = f2

for f1_s in files_s1:
    f1_s = f1_s + '.txt'
    with open(f1_s) as f1:
        for line in f1:
            if line.strip() == '':
                continue
            elms = line.strip().split('\t')
            text, subject = elms[:-1], elms[-1]
            if len(text) == 1:
                text = text[0]
            else:
                text = '\t'.join(text)
            files2[subject].write(text + '\n')

for f2 in files2.values():
    f2.close()
