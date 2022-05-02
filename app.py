import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from googleapiclient.discovery import build
from hero import get_comment_authors
from urllib.request import urlopen
from urllib.parse import urlencode
import json
#'maxResults': 100, 
# api_key = 'AIzaSyDhSLkfSCIyu8qRF24Z_SOKgBLOhiiQBy4'
api_key = 'AIzaSyDKg47ps5CnObV7JVV3p4fi90wP3uuaVbQ'
# comments_array = []

app = Flask(__name__)
model = pickle.load(open('tfidf.pickle', 'rb'))
model_2= pickle.load(open('finalized_model.sav','rb'))

mod = pickle.load(open('insultfidf2.pickle', 'rb'))
mod_2= pickle.load(open('insult_model.sav','rb'))



@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    # fuck()
    s=request.form.get("rate")
    new=""
    st=0
    end=0
    for i in range (0,len(s)):

        if s[i]=='=':
            st=i
        if s[i] == '&':
            end=i
            break

    if end ==0:
        new=s[st+1:]
    else:
        new=s[st+1:end]
    # features= video_comments(feat)
    featu= get_comment_authors(api_key,new)
    print(featu[:10])
    
    
    #print(features)
    print("yes")
    #final_features = [np.array(features)]
    vect= model.transform(featu)
    predict = model_2.predict(vect)

    vectors= mod.transform(featu)
    prediction = mod_2.predict(vectors)
    total= len(prediction)

    percent1=[0,0,0]
    percent2=[0,0,0]
    g1=0;m1=0;t1=0
    g2=0;m2=0;t2=0

    print(prediction[:10])
    print(predict[:10])

    for i in prediction:

        if i<0.2:
            g1+=1
        elif 0.2<i<0.6:
            m1+=1
        else:
            t1+=1
    percent1[0]= (int)(g1/total *100)
    percent1[1]=(int)(m1/total *100)
    percent1[2]=(int)(t1/total *100)

    for i in predict:

        if i<0.2:
            g2+=1
        elif 0.2<i<0.6:
            m2+=1
        else:
            t2+=1
    percent2[0]=(int)(g2/total *100)
    percent2[1]=(int)(m2/total *100)
    percent2[2]=(int)(t2/total *100)
    if percent1[2]/percent1[1]>0.1:
        # print('hiiiiiiiiiiii')
        return render_template('index.html', prediction_text=f"{percent1[0]},{percent1[1]},{percent1[2]}")
    else:
        print('hiiiiii')
        return render_template('index.html', prediction_text=f"{percent2[0]},{percent2[1]},{percent2[2]}")


    
    #return render_template('index.html', prediction_text='Score {}'.format(prediction))
    #data= [20,20,60]

    

    return render_template('index.html', prediction_text=f"{percent1[0]},{percent1[1]},{percent1[2]}")


# def video_comments(video_id):
#     # empty list for storing reply

    
  
#     # creating youtube resource object
#     youtube = build('youtube', 'v3',
#                     developerKey=api_key)
  
#     # retrieve youtube video results
#     video_response=youtube.commentThreads().list(
#     part='snippet',
#     videoId=video_id
#     ).execute()
  
#     # iterate video response
#     while video_response:
        
#         # extracting required info
#         # from each result object 
#         for item in video_response['items']:
            
#             # Extracting comments
#             comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
              
#             # counting number of reply of comment

#             #print(comment)
#             comments_array.append(comment)
            
  
#         # Again repeat
#         if 'nextPageToken' in video_response:
#             video_response = youtube.commentThreads().list(
#                     part = 'snippet,replies',
#                     videoId = video_id
#                 ).execute()
#         else:
#             break

#     #print("Inside youtube"+" "+len(comments_array))

#     return comments_array
if __name__ == "__main__":
    app.run(debug=True)