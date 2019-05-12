# BERT with SentencePiece for Korean text
This is a repository of Korean BERT model with SentencePiece tokenizer.

## SentencePiece tokenizer 학습
 한국어 전용 BERT 모델을 만들기 위해서는 한국어에 적합한 tokenizer로 수정할 필요가 있었습니다. 이를 위해 Google의 [SentencePiece](https://github.com/google/sentencepiece)을 사용하였습니다. 총 1400만 문장(위키피디아, 나무위키, 뉴스 데이터)을 이용하여 32,000개의 vocabulary (subwords)를 학습하였습니다.
 <br>
 
```python
parameter = '--input={} --model_prefix={} --vocab_size={}'

input_file = 'corpus.txt'
vocab_size = 32000
prefix = 'bert_kor'
cmd = parameter.format(input_file, prefix, vocab_size)

spm.SentencePieceTrainer.Train(cmd)
```   
<br>
BERT 모델에 SentencePiece 사전을 사용하기 위해서 [PAD], [CLS], [SEP], [MASK]등의 token을 추가해줘야 합니다. 이를 위해 <code>--user_defined_symbols</code> 옵션을 적용하였습니다.
<br>
<br>
 
```python
parameter = '--input={} --model_prefix={} --vocab_size={} --user_defined_symbols={}'

input_file = 'corpus.txt'
vocab_size = 32000
prefix = 'bert_kor'
user_defined_symbols = [PAD],[CLS],[SEP],[MASK]
cmd = parameter.format(input_file, prefix, vocab_size,user_defined_symbols)

spm.SentencePieceTrainer.Train(cmd)
```   
<br>

## 사전 학습 데이터 준비
 <code>[create_pretraining_data.py](https://github.com/google-research/bert/blob/master/create_pretraining_data.py)</code>를 사용하여 BERT pre-training에 적합한 <code>.tfrecord</code> 파일 형식으로 변환하였습니다. 학습 데이터의 구성은 "Next sentence prediction" Task을 위해 한 줄에 한 문장씩 구성하고 Document 사이에는 빈 줄을 삽입할 것을 권장하고 있습니다.
 
~~~
이것은 
코드 블럭
입니다
~~~
<br>

## BERT pre-training
모델 매개 변수는 <code>learning_rate=5e-5</code>, <code>train_batch_size=32</code>, <code>max_seq_length=128</code>로 학습했습니다.


