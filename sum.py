from googleapiclient.discovery import build
  
api_key = 'AIzaSyD45uV4Dc98yOech5UjmLky0HpwlcY_Szk'
comments_array = []

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

    return comments_array
       
# Enter video id
#video_id = "N--0rmo0ctA"
  

# Call function
#a=video_comments(video_id)
