# Current version as of 11/9/22
FROM jekyll/jekyll:4.2.2

# For pulling data from YouTube in tools/make-new-post.py
RUN python3 -m ensurepip --upgrade
RUN pip3 install requests-html
