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

It uses a delay to make sure that the API will not block it.

## Performance
I made a test using a profile with 1072 posts. The program downloaded it in less than 50 seconds. It makes 36 API calls (1072/30), so the real processing time is 14 seconds.

The program also checks if a partial file exists. Now it is not used, but with a few changes you should make it to download N posts every execution, so it won't run for long periods of time for larger profiles.

## Possible improvements
* CLI
* add more customizations
* web interface
* GUI

## How can I check it worked correctly
In a Unix terminal you can use the following command, replacing `PROFILE` to the desired downloaded profile:
> grep '"type": "post"' PROFILE.json | wc -l

The command will output the number of downloaded posts. Then you can compare it to the number of posts from the profile, and it should be the same.

Note: if the user response a question when the download is started, it 