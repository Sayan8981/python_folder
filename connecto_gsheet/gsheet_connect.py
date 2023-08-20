#ref_url : https://understandingdata.com/posts/the-comprehensive-guide-to-google-sheets-with-python/

import pandas as pd
import json
import csv
from google.oauth2 import service_account
import pygsheets


spreadsheet_url = "https://docs.google.com/spreadsheets/d/1E359gupjzD2Il34zm01ZXxt3QwfRn7aSxdBlIrQEpmM/edit#gid=260456629"

#previously obtained local .json file you can authenticate to your google service account.
with open('rock-partition-267907-152fe545045c.json') as source:
    info = json.load(source)
credentials = service_account.Credentials.from_service_account_info(info)

#You can successfully authenticate to google sheets with a .json key like so:
client = pygsheets.authorize(service_account_file='rock-partition-267907-152fe545045c.json')

#we will extract the spreadsheet ID which can be located in the URL above between /d/ and /edit?
sheet = client.open_by_url(spreadsheet_url)
sheet_data = client.sheet.get(sheet.id)

print (sheet_data)
print (sheet.title)
wk1 = sheet[0] # first worksheet
df = wk1.get_as_df() # create the dataframe
print (df.head(2))
print (df[["Netflix_Id", "Title"]])


 # To view the number of columns