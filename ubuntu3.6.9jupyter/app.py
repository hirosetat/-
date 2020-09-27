import MeCab

m_t = MeCab.Tagger('-Ochasen')

text = '機械学習が好きです。'

print(m_t.parse(text))
