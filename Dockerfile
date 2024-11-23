# Current version as of 11/9/22
# This image is stale
# FROM jekyll/jekyll:4.2.2

# This image is for "easy CLI"
# FROM bretfisher/jekyll

# Updated Jekyll image built on Debian
FROM bretfisher/jekyll-serve:stable-20240915-2119a31
# TODO: This uses ruby 3.1... Should update to 3.3 before April 2025

# Install python3 and pip
RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# For pulling data from YouTube's API in tools/make-new-post.py
RUN pip3 install google-auth-oauthlib google-api-python-client

# Required to run `bundle exec htmlproofer`
RUN apt-get update && apt-get install -y \
    libcurl4-gnutls-dev
