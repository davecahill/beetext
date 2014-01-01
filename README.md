beetext.py
-------------
This is a small script which does a wordcount of a given file and posts the data points to your beeminder goal, so that you can easily track how often you're adding to the file.

It is intended to be run on a cron.

Usage
---------

Copy default_config.ini to config.ini and fill in the path to the file and your beeminder credentials.

Your beeminder auth token can be found at this URL when logged in:
https://www.beeminder.com/api/v1/auth_token.json

To run:
```
python beetext.py
```
