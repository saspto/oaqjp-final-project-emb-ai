import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } } # dictionary for text to be analyzed
    response = requests.post(url, json = myobj, headers = header) # send POST request to API
    #return response.text # return from API
    if response.status_code == 200:
        formatted_response = json.loads(response.text)['emotionPredictions'][0]['emotion']
        dominant_emotion = max(formatted_response, key=formatted_response.get)
        formatted_response['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        formatted_response = {'anger': None, 'disgust': None, 'fear': None, 
        'joy': None, 'sadness': None, 'dominant_emotion': None}
    else:
        formatted_response = {'anger': None, 'disgust': None, 'fear': None, 
        'joy': None, 'sadness': None, 'dominant_emotion': None}  
    return formatted_response # returns json in the specified format
