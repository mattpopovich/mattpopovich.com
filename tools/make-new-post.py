# Quick little script for creating a new post
#   It will create a new post in _posts/, auto-populate it with some basic
#   text, and create a folder in assets/img/posts/
# TOOD: Clean up this mess
#       Create a main function
#       Must be run from the tools folder
#       Show --help even if there is no api_key.txt file


# Imports
import argparse
import urllib.parse
import urllib.request
import json
import os               # Finding if folder exists
import datetime         # For parsing date strings
import re               # Regex
import sys              # To exit script on error

from pathlib import Path

# For reading Google's YouTube API
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Constants
API_KEY_FILENAME = "api_key.txt"

# Get API key: https://console.cloud.google.com/project/_/google/maps-apis/credentials
if os.path.exists(API_KEY_FILENAME):
    print("API key file found: " + API_KEY_FILENAME)
else:
    sys.exit("ERROR: API key file not found: " + API_KEY_FILENAME)

with open(API_KEY_FILENAME, 'r') as api_key_file:
    api_key = api_key_file.read().strip()
    if api_key:
        print("API key found: " + api_key)
    else:
        sys.exit("ERROR: Nothing found in API key file: " + API_KEY_FILENAME)

# Set up the YouTube API client
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

# Via: https://www.thepythoncode.com/article/get-youtube-data-python
#      https://github.com/x4nth055/pythoncode-tutorials/blob/master/web-scraping/youtube-extractor/extract_video_info.py
def get_video_info(video_id):

    # Request the video resource
    video_request = youtube.videos().list(
        # part="snippet,contentDetails,statistics",
        part="snippet",
        id=video_id
    )

    # Execute the request and extract relevant information
    response = video_request.execute()
    video = response["items"][0]

    # initialize the result
    result = {}
    # video title
    result["title"] = video["snippet"]["title"]
    # video views
    # result["views"] = video["statistics"]["viewCount"]
    # video description
    result["description"] = video["snippet"]["description"]
    # date published
    result["date_published"] = video["snippet"]["publishedAt"]
    # get the duration of the video
    # result["duration"] = video["contentDetails"]["duration"]
    # get the video tags
    result["tags"] = video["snippet"]["tags"]

    # number of likes
    # result["likes"] = video["statistics"]["likeCount"]
    result['dislikes'] = 'UNKNOWN'

    return result

# ---- Main part of script ----

# Make sure we are running the script from the correct directory
if not os.path.exists('make-new-post.py'):
    print("ERROR: make-new-post.py is being ran from the wrong location")
    print("       Please cd to tools/ then run the script from there")
    sys.exit()

# Parse arguments
parser = argparse.ArgumentParser(description="Automatically create some basic files for a new blog post")
parser.add_argument('--youtube-link', '-y', type=str,
                    help='Link to the YouTube video that the blog post is based '
                         'upon, will auto-populate a few fields from here')
parser.add_argument('--title', '-t', type=str,
                    help="Title of the article if not using a predefined title "
                         "from YouTube")

args = parser.parse_args()

# Grab title, dates, and text that should be pre-populated based on the argument
#   specified
if not (args.youtube_link or args.title):
    parser.error("ERROR: You must specify either a '-y' YouTube link or a "
                                                  "'-t' custom title for the post")
    sys.exit()  # Probably unnecessary

elif args.youtube_link:
    # For debugging
    # args.youtube_link = 'https://youtu.be/JuFTTGWe_HQ' # tesla swerve
    # args.youtube_link = "https://www.youtube.com/watch?v=Hv6EMd8dlQk" #joma
    # args.youtube_link = "https://youtu.be/ALsLiy4sLIQ" #airpods
    # args.youtube_link = "https://www.youtube.com/watch?v=L2Pp3c7fN3E" #853 likes Renee Ritchie

    # Get video ID from YouTube Link (string parsing)
    print(f"Received YouTube video link: {args.youtube_link}")
    url_parts = urllib.parse.urlparse(args.youtube_link)
    if 'watch' not in url_parts.path:
        # Ex. 'https://youtu.be/xxxxx'
        video_id = url_parts.path.rsplit('/', 1)[-1]
    else:
        # Ex. 'https://www.youtube.com/watch?v=xxxxx'
        video_id = url_parts.query.replace('v=', '')
    print(f"Identified the YouTube video ID as: {video_id}")

    # Get video's date of publish and title
    params = get_video_info(video_id)
    date_published = params['date_published']
    date_time_obj = datetime.datetime.strptime(date_published, '%Y-%m-%dT%H:%M:%SZ')
    date_for_folder = date_time_obj.strftime("%Y-%m-%d")    # YYYY-MM-DD

    title = params['title']

    # Make template post with header
    with open('post_middle_youtube.txt', 'r') as f:
        post_middle = f.read()

    with open('post_ending_youtube.txt', 'r') as f:
        post_ending = f.read()

    finish_post = post_middle + video_id + post_ending

elif args.title:
    title=args.title
    date_for_folder = datetime.datetime.now().strftime("%Y-%m-%d")  # YYYY-MM-DD
    with open('post_title.txt', 'r') as f:
        finish_post = f.read()

    print("Using a custom title for this post: " + title)

else:
    print("ERROR: Something funky's going on with the arguments specified")
    sys.exit()


# By this point, title, date_for_folder, and finish_post should all be set

title_no_space = title.lower().replace(' ', '-')
title_for_folder = ''.join(c for c in title_no_space if c.isalnum() or c == '-')

folder_name = date_for_folder + '-' + title_for_folder
folder_path = '../assets/img/posts/' + folder_name

# Create folder for images
if os.path.exists(folder_path):
    print("WARNING: folder path was already created: " + folder_path)
else:
    os.makedirs(folder_path)
    print("Created folder: " + folder_path)

post_path = '../_posts/' + folder_name + '.md'
print("Creating text post: " + post_path)

# Make sure the post isn't already created before we overwrite it
if os.path.exists(post_path):
    print("ERROR: Text post was already created. ")
    print("       Check to ensure that you do not need the text post, then "
                 "delete it and run this script again for the text post to be "
                 "populated with template text")
    sys.exit()  # Not necessary but safe
else:
    with open(post_path, 'w') as f:
        f.write('---\n')
        f.write('title: "' + title + '"\n')
        f.write('author: matt_popovich           # Reference author_id in _data/authors.yml\n')
        f.write('# Can also use `authors: [<author1_id>, <author2_id>]` for multiple entries\n')
        # -0600 if in summer, -0700 if in winter
        # TODO: Make this automatic?
        f.write('date: ' + date_for_folder + datetime.datetime.now().strftime(" %H:%M:%S") + ' -0600\n')
        f.write(finish_post)

print("Finished successfully!")
