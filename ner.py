from stanfordcorenlp import StanfordCoreNLP

nlp = StanfordCoreNLP(r'/home/nlp/lib/stanfordnlp', lang='zh')

fin = open('news.txt', 'r', encoding='utf8')
fner = open('ner.txt', 'w', encoding='utf8')
ftag = open('pos.txt', 'w', encoding='utf8')

for line in fin:
    line = line.strip()
    if len(line) < 1:
        continue
    fner.write(" ".join([each[0] + "/" + each[1] for each in nlp.ner(line) if len(each) == 2]) + "\n")
    ftag.write(" ".join([each[0] + "/" + each[1] for each in nlp.pos_tag(line) if len(each) == 2]) + "\n")

fin.close()
fner.close()
ftag.close()
