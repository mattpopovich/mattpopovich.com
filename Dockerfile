# Current version as of 11/9/22
# This image is stale
# FROM jekyll/jekyll:4.2.2

# This image is for "easy CLI"
# FROM bretfisher/jekyll

# Updated Jekyll image built on Debian
FROM bretfisher/jekyll-serve

# Install python3 and pip
RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

# For pulling data from YouTube in tools/make-new-post.py
RUN pip3 install requests-html

# Required to run `bundle exec htmlproofer`
RUN apt-get update && apt-get install -y \
    libcurl4-gnutls-dev
