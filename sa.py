from snownlp import SnowNLP
s = SnowNLP(u'这个东西真心很赞')

print(s.words)
print(s.tags)
print(s.sentiments)