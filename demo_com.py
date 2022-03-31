from googleapiclient.discovery import build
from urllib.request import urlopen
from urllib.parse import urlencode
import json
#'maxResults': 100, 
api_key = 'AIzaSyAm_kIHI257c6Kb3Wyu1bu0wh1nAvchmqw'
comments_array = []

def progress(page_count):
    if page_count > 1:
        print('')

    print(f'Getting comments for page {page_count}...')

    return page_count + 1

def get_comments(api_params):
    api_endpoint = 'https://www.googleapis.com/youtube/v3/commentThreads'
    #api=urlencode('utf-8')
    print(api_params)
    encoded_params = urlencode(api_params,encoding="utf-8",doseq=True)

    with urlopen(f'{api_endpoint}?{encoded_params}') as response:
        print("Inside comments")
        return json.load(response)

def get_comment_authors(api_token, video_id):
    authors = []
    page_count = 1

    api_params = {
        'key': api_token,
        'part': 'snippet',
        'videoId': video_id,
    }

    results = get_comments(api_params)
    print("yes")
    print(results)

    #comments_array.append(results)
    page_count = progress(page_count)
    #authors.append(display_names(results, is_verbose))


    next_page_token = results.get('nextPageToken')
    print("Now")

    

    while next_page_token:
        print("Inside")
        page_count = progress(page_count)
        print("Yes")

        api_params['pageToken'] = next_page_token
        results = get_comments(api_params)
        #authors.append(display_names(results, is_verbose))
        #comments_array.append(results)


        next_page_token = results.get('nextPageToken')

    return comments_array

a=get_comment_authors(api_key, "BILxV_vrZO0")
#print(a)
#BILxV_vrZO0
#Sxxw3qtb3_g



