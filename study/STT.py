import speech_recognition as sr

# 마이크로부터 음성 듣기
r = sr.Recognizer()
# 마이크를 통해 들려오는 음성을 저장
with sr.Microphone() as source:
    print("말해주세요!!")
    audio = r.listen(source) # 마이크로부터 음성 듣기

# 녹음된 데이터를 구글에 보내고 구글에서 음성인식된 데이터를 다시 보내줌
# 따라서 네트워크가 연결 되어야함.

# 파일로부터 음성 듣기   wav, aiff/aiff-c, flac 가능, mp3는 불가
with sr.AudioFile('./study/sample.wav') as source:
    audio = r.record(source)


try:
    ### recognize_google--> 구글 API로 인식(하루 50회)
    # 영어 인식
    text = r.recognize_google(audio, language='en-US') #영어 인식
    print(text)
    # 한국어 인식
    text = r.recognize_google(audio, language='ko') #한국어 인식
    print(text)

except sr.UnknownValueError: # 음성인식 실패한 경우
    print('음성 인식 실패')
except sr.RequestError as e:
    print(f'요청 실패 : {e}') # API Key 오류, 네트워크 단절 등
