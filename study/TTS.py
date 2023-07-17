from gtts import gTTS

# # 영어 문장
# text1 = 'can i help you?'
# file_name1 = 'sample1.mp3'
# # 영어로 인식해서 text를 음성으로 바꾼 결과를 tts_en에 담기
# tts_en = gTTS(text=text1, lang='en')
# # 파일 저장
# tts_en.save("./study/"+file_name1)

from playsound import playsound

# #mp3 파일 재생(저장된 파일 재생)
# playsound("./study/"+file_name1)

# # 한글 문장
# text_kor = '쉬리를 넘고 싶어요. 나쁘지 않아요'
# file_name2 = 'sample2.mp3'
# tts_kor = gTTS(text=text_kor, lang='ko')
# tts_kor.save("./study/"+file_name2)
# playsound("./study/"+file_name2)

# 긴 문장(파일에서 불러와서 처리)
with open('./study/sample.txt', 'r', encoding='utf-8') as f:
    text_txt = f.read()
file_name3 = 'sample3.mp3'
tts_kor = gTTS(text=text_txt, lang='ko')
tts_kor.save("./study/"+file_name3)
playsound("./study/"+file_name3)


