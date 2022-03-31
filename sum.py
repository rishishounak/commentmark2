from googleapiclient.discovery import build
  
api_key = 'AIzaSyAm_kIHI257c6Kb3Wyu1bu0wh1nAvchmqw'
comments_array = []

def video_comments(video_id):
    # empty list for storing reply

    
  
    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=api_key)
  
    # retrieve youtube video results
    video_response=youtube.commentThreads().list(
    part='snippet',
    videoId=video_id,
    
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

    print(len(comments_array))

    return comments_array
def video_comment(video_id):
    # empty list for storing reply
    replies = []

    comments=[]
  
    # creating youtube resource object
    youtube = build('youtube', 'v3',
                    developerKey=api_key)
  
    # retrieve youtube video results
    video_response=youtube.commentThreads().list(
    part='snippet,replies',
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
            replycount = item['snippet']['totalReplyCount']
  
            # if reply is there
            if replycount>0:
                
                # iterate through all reply
                for reply in item['replies']['comments']:
                    
                    # Extract reply
                    reply = reply['snippet']['textDisplay']
                      
                    # Store reply is list
                    replies.append(reply)
  
            # print comment with list of reply
            #print(comment+' \n\n')
  
            # empty reply list
            replies = []
  
        # Again repeat
        if 'nextPageToken' in video_response:
            video_response = youtube.commentThreads().list(
                    part = 'snippet,replies',
                    videoId = video_id
                ).execute()
        else:
            break
    print(len(comments))
    
       
# Enter video id
#video_id = "N--0rmo0ctA"
  

# Call function
#"BILxV_vrZO0"

#"oNRr1WjJgw4" count=20
a=video_comments("37s1_xBiqH0")
