import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from googleapiclient.discovery import build
  
api_key = 'AIzaSyD45uV4Dc98yOech5UjmLky0HpwlcY_Szk'
comments_array = []
app = Flask(__name__)
model = pickle.load(open('tfidf.pickle', 'rb'))
model_2= pickle.load(open('finalized_model.sav','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    feat=request.form.get("rate")
    print(type(feat))
    features= video_comments(feat)
    
    print(features)
    print("yes")
    #final_features = [np.array(features)]
    vectors= model.transform(features)
    prediction = model_2.predict(vectors)
    total= len(prediction)

    percent=[0,0,0]
    g=0;m=0;t=0

    print(prediction)

    for i in prediction:

        if i<0.2:
            g+=1
        elif 0.2<i<0.8:
            m+=1
        else:
            t+=1
    percent[0]= (int)(g/total *100)
    percent[1]=(int)(m/total *100)
    percent[2]=(int)(t/total *100)


    
    #return render_template('index.html', prediction_text='Score {}'.format(prediction))
    #data= [20,20,60]

    

    return render_template('index.html', prediction_text=f"{percent[0]},{percent[1]},{percent[2]}")


def video_comments(video_id):
    # empty list for storing reply

    
  
    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=api_key)
  
    # retrieve youtube video results
    video_response=youtube.commentThreads().list(
    part='snippet',
    videoId=video_id
    ).execute()
  
    # iterate video response
    while video_response:
        
        # extracting required info
        # from each result object 
        for item in video_response['items']:
            
            # Extracting comments
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
              
            # counting number of reply of comment

            #print(comment)
            comments_array.append(comment)
            
  
        # Again repeat
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                    part = 'snippet,replies',
                    videoId = video_id
                ).execute()
        else:
            break

    #print("Inside youtube"+" "+len(comments_array))

    return comments_array
if __name__ == "__main__":
    app.run(debug=False)