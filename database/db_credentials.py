# To actually have your app use this file, you need to RENAME the file to db_credentials.py
# You will find details about your CS340 database credentials on Canvas.

# the following will be used by the webapp.py to interact with the database
# You can also use environment variables

import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())



# For OSU Flip Servers

host = os.getenv("MYSQL_HOST")
user = os.getenv("MYSQL_USER")
passwd = os.getenv("MYSQL_PASSWORD")
db = os.getenv("MYSQL_DB") 

# host = 'classmysql.engr.oregonstate.edu'      # MUST BE THIS
# user = 'cs340_aljehanl'       # don't forget the CS_340 prefix
# passwd = '8321'               # should only be 4 digits if default
# db = 'cs340_aljehanl'                                  