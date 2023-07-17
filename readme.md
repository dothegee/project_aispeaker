## 기술 설명
- TTS - Text To Speech
- STT - Speech to Text

pip install gTTS
- 구글에서 제공하는 tts 파일

pip install playsound==1.2.2

pip install SpeechRecognition
- 음성 인식 모듈

pip install PyAudio
- 마이크 사용을 위한 모듈

### ./study/AIspeaker.py
- answer 함수 내부에 딥러닝 (gpt등 NLP 관련 모델)을 넣게 되면 AIspeaker 완성 가능
- V1 은 chatgpt와 같은 대화 형식 보다는 내가 기존에 설정해 놓은 keyword가 문장안에 포함되어있으면 그거에 맞는 문장을 내뱉기