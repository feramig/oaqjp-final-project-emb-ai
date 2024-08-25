import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = obj, headers=header)

    if response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
    else:

        formatted = json.loads(response.text)

        emotions = formatted['emotionPredictions'][0]

        anger = emotions['emotion']['anger']
        disgust = emotions['emotion']['disgust']
        fear = emotions['emotion']['fear']
        joy = emotions['emotion']['joy']
        sadness = emotions['emotion']['sadness']
        dominant_emotion = max(emotions['emotion'], key=emotions['emotion'].get)

    return {'anger':anger,'disgust':disgust,'fear':fear,'joy':joy,'sadness':sadness,'dominant_emotion':dominant_emotion}
