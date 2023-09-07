


# Load model directly
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM,pipeline


tokenizer = AutoTokenizer.from_pretrained("yeeunlee/long-ke-t5-base-translation-aihub-ko2en-finetuned")
model = AutoModelForSeq2SeqLM.from_pretrained("yeeunlee/long-ke-t5-base-translation-aihub-ko2en-finetuned")
translation = pipeline("translation", model=model, tokenizer=tokenizer)
x=" IBM 왓슨X는 AI 및 데이터 플랫폼이다. 신뢰할 수 있는 데이터, 속도, 거버넌스를 갖고 파운데이션 모델 및 머신 러닝 기능을 포함한 AI 모델을 학습시키고, 조정해, 조직 전체에서 활용하기 위한 전 과정을 아우르는 기술과 서비스를 제공한다."
re = translation(x, max_length=512)
print('翻译为：' ,re)



