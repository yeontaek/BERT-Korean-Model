# BERT with SentencePiece for Korean text
This is a repository of Korean BERT model with SentencePiece tokenizer.

## SentencePiece tokenizer 학습
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
추가로 BERT 모델에 해당 사전을 사용하기 위해서 [PAD], [CLS], [SEP], [MASK]를 추가하는 옵션 <code>--user_defined_symbols</code> 을 적용하였습니다.
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
 <code>[create_pretraining_data.py](https://github.com/google-research/bert/blob/master/create_pretraining_data.py)</code>를 사용하여 ㅠBERT pre-training에 적합한 <code>.tfrecord</code>형식으로 변환하였습니다. 학습 데이터는 IsNext 정보 작성을 위해 문장이면서 document 사이에 빈 줄을 삽입 할 것을 권장하고 있습니다. 
 
 
 그러나이 스크립트는 모든 데이터를 메모리에로드 사양으로되어 있기 때문에, 대량의 데이터가 메모리 부족하게되어 버립니다. 후 pre-training에서 여러 파일을 학습 데이터와 있기 때문에 여기에서는 1/10 씩 .tf_record을 만들었습니다 (하나의 파일이 약 2 GB). 얼마나 데이터를 복제하거나 등의 각종 매개 변수는 공식 저장소의 것으로 갖추고 있습니다.



