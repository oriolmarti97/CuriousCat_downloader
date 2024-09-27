# CuriousCat_downloader
CuriousCat will be fully discontinued on the 7th of October 2024. This repository contains a script meant to download all the posts from public profiles

## How to use it:
### If you don't know how to use Python...
You can ask to a friend, who will do it kindly for you

### If you know how to use Python
The simplest usage is editing the [download.py](./download.py) file and setting `PROFILE` to the desired username. Then the code can be run using the command:

> python download.py

You may want to change also `FILENAME` or `DELAY`. The last is specially useful if you want to speed-up the execution, as it is used to wait between calls to the API. 

## How it works
1. set timestamp to now
2. make a request to the API asking 30 posts older than timestamp
3. saves the response (only posts, avoiding reposts)
4. waits 1 second
5. timestamp = minimum_timestamp-1
6. if response was not empty, go to 2
7. write to JSON file

It is meant to make requests without having to calculate numbers of posts nor timestamps. It uses the last timestamp and iterates until the response is empty. 

It uses a delay to make sure that the API will not block it

## Possible improvements
* CLI
* add more customizations
* web interface
* GUI
