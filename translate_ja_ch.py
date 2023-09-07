from transformers import pipeline
import re

pipe = pipeline(model="larryvrh/mt5-translation-ja_zh")

def translate_sentence(sentence):
    return pipe(f'<-ja2zh-> {sentence}')[0]['translation_text']


def translate_paragraph(paragraph):
    sentences = []
    cursor = 0
    for i, c in enumerate(paragraph):
        if c == '。':
            sentences.append(paragraph[cursor:i + 1])
            cursor = i + 1
    if paragraph[-1] != '。':
        sentences.append(paragraph[cursor:])
    return ''.join(translate_sentence(s) for s in sentences)


def translate_article(article):
    paragraphs = re.split(r'([\r\n]+)', article)
    for i, p in enumerate(paragraphs):
        if len(p.strip()) == 0:
            continue
        paragraphs[i] = translate_paragraph(p)
    return ''.join(paragraphs)

article = "あいでぃあ"

print(translate_sentence(article))
