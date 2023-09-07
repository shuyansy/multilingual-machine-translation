from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

mode_name = 'DDDSSS/translation_en-zh'
model = AutoModelForSeq2SeqLM.from_pretrained(mode_name)
# Model was saved using *save_pretrained('./test/saved_model/')* (for example purposes, not runnable).
tokenizer = AutoTokenizer.from_pretrained(mode_name)
translation = pipeline("translation", model=model, tokenizer=tokenizer)
# x="GitHub is an online software source code hosting service platform, using Git as version control software, written by developers Chris Wanstrath, P. J. Hyett and Tom Preston Werner using Ruby on Rails. In 2018, GitHub was acquired by Microsoft Corporation. GitHub offers both paid and free accounts."
x="NEWYORK"
re = translation(x, max_length=512)
print('翻译为：' ,re)


