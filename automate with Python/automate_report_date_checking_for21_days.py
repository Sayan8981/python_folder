""" Writer: Saayan """

#Set up
import os, logging, sys, pandas as pd
from datetime import datetime

#----------------------- initialization -------------------------------
total_files = 0
file_empty = 0
file_is_not_empty = 0
date_missing = 0
date_not_missing = 0
folder_wise_file_count = dict()

#--------------------------  forma of dates  ----------------------------
list_dates = list()
start_date = "May %s, 2021"
end_date = "Jun 0%s, 2021"

#--------------------  log module --------------------------------------
try:
    if os.getcwd()+ '\\log\\AMS_log_report_%s.txt'%datetime.now().strftime('%y-%m-%d'):
        os.remove(os.getcwd()+ '\\log\\AMS_log_report_%s.txt'%datetime.now().strftime('%y-%m-%d'))
except FileNotFoundError:
    pass         
logger = logging.getLogger()
logging.basicConfig(filename=os.getcwd()+ '\\log\\AMS_log_report_%s.txt'%datetime.now().strftime('%y-%m-%d'),format=[],filemode='w')
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)

#------------------ list of dates which will be consider for verification ---------------------
for date in range(20, 32):
    list_dates.append(start_date%date)
for date in range(1, 10):
    list_dates.append(end_date%date)    
logger.info ({"consider_dates ": list_dates})

#------------------- source_files --------------------------------------
input_dir = os.getcwd() + r"\\input_reports\\ams_reports"
ams_files = os.listdir(input_dir)

#---------------------- taking folder of ams_files -------------------
for file in ams_files:
    report_files = os.listdir(input_dir + "\\" + file)
    folder_wise_file_count[file] = len(report_files)
    #----------------  Taking csv files from each report folder ------------------------------
    for files in report_files:
        total_files += 1
        reports_date = []
        csv_file =  "{}{}{}{}{}".format(input_dir , "\\" , file , "\\" , files)
        csv_data = pd.read_csv(csv_file)
        missing_dates = []
        if len(csv_data) == 0:
            file_empty += 1
            logger.info ("\n")
            logger.info ("** Csv file empty %s "%csv_file)
        else:
            file_is_not_empty += 1
            for index,row  in csv_data.iterrows():
                date = str(row['Date'])
                reports_date.append(date)        
            for date in list_dates:
                if date in reports_date:
                    pass
                else:
                    missing_dates.append(date)
            if missing_dates:        
                date_missing += 1
                logger.info("\n")
                logger.info ("*** date missing file %s and missing date %s "%(csv_file,str(missing_dates)))
            else:
                date_not_missing +=1       

#-------------------------  report generate -------------------------------------------
logger.info("\n")
logger.info("Folder wise csv file count {folder_name : csv file count}")
logger.info("\n")
logger.info(folder_wise_file_count)
logger.info("\n")
logger.info("Report: ")
logger.info({"total_csv_files count " : total_files})
logger.info({"csv_file_empty count  " : file_empty})
logger.info({"csv_file_is_not_empty count " : file_is_not_empty})
logger.info({"csv_file date_missing count " :  date_missing})
logger.info({"csv_file date_not_missing count " : date_not_missing})

