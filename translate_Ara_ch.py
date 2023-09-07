from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

mode_name = 'Helsinki-NLP/opus-mt-ar-en' 
model = AutoModelForSeq2SeqLM.from_pretrained(mode_name)
# Model was saved using *save_pretrained('./test/saved_model/')* (for example purposes, not runnable).
tokenizer = AutoTokenizer.from_pretrained(mode_name)
translation = pipeline("translation", model=model, tokenizer=tokenizer)
x="إسمي ساره وأسكن في لندن"
re = translation(x, max_length=512)
print('翻译为：' ,re)


