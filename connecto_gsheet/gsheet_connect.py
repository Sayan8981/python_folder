import pygsheets
  

# file in service_account_file
client = pygsheets.authorize(service_account_file="connecto_gsheet/rock-partition-267907-57ff29cf07ed.json")

# account
print(client.spreadsheet_titles())