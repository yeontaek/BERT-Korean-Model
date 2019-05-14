import sentencepiece as spm

input_file = 'corpus.txt'

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