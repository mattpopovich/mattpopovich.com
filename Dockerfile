# This image is a bit of a mess with regards to its owner
#   but it is updated (ruby 3.4) and it works again
FROM jekyll/jekyll:4.4.1

# This image is for "easy CLI"
# FROM bretfisher/jekyll

# Updated Jekyll image built on Debian
# FROM bretfisher/jekyll-serve:stable-20240915-2119a31
# TODO: This uses ruby 3.1... Should update to 3.3 before April 2025

# Install python3, pip, and python virtual environment
RUN apt-get update && apt-get upgrade -y
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv

# Create a venv at /opt/venv and put it first on PATH
# Any later python3/pip3 calls automatically use the venv without needing to activate it manually
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# For pulling data from YouTube's API in tools/make-new-post.py
RUN pip3 install google-auth-oauthlib google-api-python-client

# Required to run `bundle exec htmlproofer`
RUN apt-get update && apt-get install -y \
    libcurl4-gnutls-dev
