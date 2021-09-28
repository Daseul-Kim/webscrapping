from wordcloud import WordCloud
from PIL import Image
import numpy as np


text = ''
with open("kakaotalk2.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines[5:]:
        if '] [' in line:
            text += line.split('] ')[2].replace('ㅋ','').replace('ㅠ','').replace('ㅎ','').replace('ㅜ','').replace('이모티콘','').replace('사진','').replace('근데','').replace('아','').replace('진짜','').replace('나','').replace('니','').replace('샵검색','').replace('야','').replace('너','').replace('걍','').replace('저거','').replace('다','').replace('그럼','').replace('내가','').replace('왜','').replace('도','').replace('는','').replace('은','').replace('그닌깐','').replace('진심','').replace('와','').replace('우리','').replace('오늘','').replace('후우','').replace('그','').replace('하','').replace('맞','').replace('뭐','').replace('난','').replace('이','').replace('무','').replace('오','').replace('또','').replace('더','').replace('아','').replace('거','').replace('렇게','').replace('래','').replace('같','').replace('뉘','').replace('저','').replace('서','').replace('면','').replace('후','').replace('기','').replace('가','')


print(text)
# ctrl  + / = 주석처리

# 워드클라우드 이미지 생성
# wc = WordCloud(font_path='C:/Users/김다슬/AppData/Local/Microsoft/Windows/Fonts/NanumBarunGothicBold.ttf', background_color="white", width=600, height=400)
# wc.generate(text)
# wc.to_file("result2.png")


mask = np.array(Image.open('cloud.png'))
wc = WordCloud(font_path='C:/Users/김다슬/AppData/Local/Microsoft/Windows/Fonts/NanumBarunGothicBold.ttf', background_color="white", mask=mask)
wc.generate(text)
wc.to_file("result_masked.png")