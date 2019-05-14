import sentencepiece as spm

input_file = 'final_corpus_20190515.txt'

templates = '--input={} --model_prefix={} --vocab_size={} --user_defined_symbols={} --input_sentence_size={} --shuffle_input_sentence={}' \
            '--seed_sentencepiece_size={} --hard_vocab_limit={}'

vocab_size = 32000
prefix = 'bert_kor_vocab'
user_defined_symbols = '[PAD],[UNK],[CLS],[SEP],[MASK]'
seed_sentencepiece_size = 100000
hard_vocab_limit = False
input_sentence_size = 20000000
shuffle_input_sentence = True
cmd = templates.format(input_file, prefix, vocab_size, user_defined_symbols, input_sentence_size, shuffle_input_sentence, seed_sentencepiece_size, hard_vocab_limit)

spm.SentencePieceTrainer.Train(cmd)

'''
sp = spm.SentencePieceProcessor()
sp.Load('{}.model'.format(prefix))
token = sp.EncodeAsPieces('나는 오늘 아침밥을 먹었다.')
print(token)

sentence = []
for tk in token:
    if "▁" in tk:
        sentence.append(tk.replace("▁", ""))
    else:
        sentence.append("##"+tk)

with open('{}.vocab'.format(prefix), encoding='utf-8') as f:
    vocabs = [doc.strip() for doc in f]

print('num of vocabs = {}'.format(len(vocabs))) # 2000
'''
