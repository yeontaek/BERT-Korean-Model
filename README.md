# BERT with SentencePiece for Korean text
This is a repository of Korean BERT model with SentencePiece tokenizer.

## SentencePiece tokenizer
 한국어 전용 BERT 모델을 만들기 위해서 한국어에 적합한 tokenization 변경할 필요가 있었습니다. 이를 위해 Google의 [SentencPiece](https://github.com/google/sentencepiece)를 사용 하였습니다. 총 1400만 문장(위키피디아, 나무위키, 뉴스 데이터)을 이용하여 32,000개의 vocabulary (subwords)를 학습하였습니다.

```python
parameter = '--input={} --model_prefix={} --vocab_size={}'

input_file = 'corpus.txt'
vocab_size = 32000
prefix = 'bert_kor'
cmd = parameter.format(input_file, prefix, vocab_size)

spm.SentencePieceTrainer.Train(cmd)
```   
<br>
BERT 모델에 사용하기 위해서는 사전에 해당 [PAD], [CLS], [SEP], [MASK]를 추가하는 옵션을 적용해야 합니다.

```python
parameter = '--input={} --model_prefix={} --vocab_size={}'

input_file = 'corpus.txt'
vocab_size = 32000
prefix = 'bert_kor'
cmd = parameter.format(input_file, prefix, vocab_size)

spm.SentencePieceTrainer.Train(cmd)
```   

## 사전 학습 데이터 
