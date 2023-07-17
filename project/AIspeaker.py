import time, os
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# 음성 인식 (STT)
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='ko') #한국어 인식
        print(text)
        print("[doothegee] : "+text)
        answer(text)
    except sr.UnknownValueError: # 음성인식 실패한 경우
        print('음성 인식 실패')
    except sr.RequestError as e:
        print(f'요청 실패 : {e}') # API Key 오류, 네트워크 단절 등



# 대답 --> 이 부분을 딥러닝 part로 대체하여 대화 유도 가능
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        answer_text = '오늘의 날씨는 우중충하며, 습하고, 한강공원이 잠겨있어요'
    elif '환율' in input_text:
        answer_text = '원 달러 환율이 1000원이였음 좋겠어요'
    elif '종료' in input_text:
        answer_text = '안뇽~~~~~~~~~'
        stop_listening(wait_for_stop=False)
    else:
        answer_text = '아직 그말은 배우지 못하였어요 '
    speak(answer_text)

# 소리내어 읽기 (TTS)
def speak(text):
    print('[인공지능] : '+text)
    file_name = 'voice.mp3'
    tts = gTTS(text=text, lang='ko')
    tts.save('./study/'+file_name)
    playsound('./study/'+file_name)
    if os.path.exists('./study/'+file_name): # voice.mp3 파일 삭제
        os.remove('./study/'+file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen) # 계속해서 프로그램 실행
# stop_listening(wait_for_stop=False) # 더이상 듣지 않음

while True:
    time.sleep(0.1)
