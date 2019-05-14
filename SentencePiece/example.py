import sentencepiece as spm

input_file = 'corpus.txt'

templates = '--input={} --model_prefix={} --vocab_size={} --user_defined_symbols={} --input_sentence_size={} --shuffle_input_sentence={}'

vocab_size = 32000
prefix = 'bert_kor_vocab'
user_defined_symbols = '[PAD],[UNK],[CLS],[SEP],[MASK]'
input_sentence_size = 20000000
cmd = templates.format(input_file, prefix, vocab_size, user_defined_symbols, input_sentence_size)

spm.SentencePieceTrainer.Train(cmd)