""" Writer: Saayan """

#Set up
import os, logging, sys, pandas as pd
from datetime import datetime

class portfolio_id_checking(object):
    
    #----------------------- initialization -------------------
    def __init__(self):
        self.total_files = 0
        self.file_empty = 0
        self.file_is_not_empty = 0
        self.portfolio_id_missing_count = 0
        self.no_portfolio_name_without_id_count = 0
        self.no_portfolio_name_with_id_count = 0
        self.portfolio_id_list = list()
        self.unique_portfolio_names = list()
        self.folder_wise_file_count = dict()
        self.dict_with_no_portfolio_id = dict()
        self.dict_with_no_portfolio_name_without_id = dict()
        self.dict_no_portfolio_name_with_portfolio_id = dict()
        self.flag_no_portfolio_name_with_id = False
        self.flag_no_portfolio_id_with_portfolio_name = False
        self.flag_with_no_portfolio_name_without_id = False
        self.files = list()
        self.table_column = ["Folder", "File Name", "Csv file with unique portfolio id", "Csv file_no_portfolio_id_with_portfolio_name", "Csv file_with_no_portfolio_name_without_id", "Csv file_no_portfolio_name_with_portfolio_id"]
    
    #----------- Cleanup initialize variables -----------------    
    def cleanup(self):
        self.portfolio_id_list = list()
        self.dict_with_no_portfolio_id = dict()    
        self.dict_with_no_portfolio_name_without_id = dict()
        self.dict_no_portfolio_name_with_portfolio_id = dict()
        self.flag_no_portfolio_name_with_id = False
        self.flag_with_no_portfolio_name_without_id = False
        self.flag_no_portfolio_id_with_portfolio_name = False
        self. flag_with_portfolio_name_with_portfolio_id = False

    #--------------------  log module --------------------------
    def create_log(self, log_file):
        try:
            if os.getcwd() + log_file:
                os.remove(os.getcwd() + log_file)
        except FileNotFoundError:
            pass         
        logger = logging.getLogger()
        logging.basicConfig(filename=os.getcwd() + log_file,format=[],filemode='w')
        logger.setLevel(logging.INFO)
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)
        return logger
    
    #------------ main module -----------
    def main(self):
        self.logger = self.create_log('/log/AMS_log_report_portfolio_ID_%s.txt'%datetime.now().strftime('%y-%m-%d'))
        self.input_dir = os.getcwd() + r"/input"
        self.ams_files = os.listdir(self.input_dir)
        if os.path.exists(os.getcwd() + "/output/portfolio_validation_%s.csv"%datetime.now().strftime('%y-%m-%d')):
            os.remove(os.getcwd() + "/output/portfolio_validation_%s.csv"%datetime.now().strftime('%y-%m-%d'))
        #calling the ams_files_folder to iterate ---------------
        for file in self.ams_files:
            self.report_files = os.listdir(self.input_dir + "/" + file)
            self.folder_wise_file_count[file] = len(self.report_files)
            #calling the CSV files from report ------------------
            for files in self.report_files:
                self.total_files += 1
                csv_file =  "{}{}{}{}{}".format(self.input_dir , "/" , file , "/" , files)
                csv_data = pd.read_csv(csv_file)
                #checking the empty CSV files -----------------
                if len(csv_data) == 0:
                    self.file_empty += 1
                    self.logger.info ("\n")
                    self.logger.info ("** Csv file empty %s "%csv_file)
                else:
                    #look upon not empty files ----------------
                    self.file_is_not_empty += 1
                    try:
                        for index, row  in csv_data.iterrows():
                            portfolio_id = str(row['Portfolio ID'])
                            portfolio_name = str(row['Portfolio name'])
                            if portfolio_name not in self.unique_portfolio_names:
                                self.unique_portfolio_names.append(portfolio_name)
                            #Checking the following conditions in the csv  ----------------------
                            if portfolio_id != 'nan' and portfolio_id not in self.portfolio_id_list and str(row['Portfolio name']) != 'No portfolio':
                                self.portfolio_id_list.append(portfolio_id)
                            elif portfolio_id == 'nan' and str(row['Portfolio name']) != 'No portfolio':
                                self.flag_no_portfolio_id_with_portfolio_name = True
                                if str(file+'/'+files) not in self.dict_with_no_portfolio_id:
                                    self.dict_with_no_portfolio_id[str(file+'/'+files)] = []
                                self.dict_with_no_portfolio_id[str(file+'/'+files)].append({str(row['campaignName']):{str(row['Portfolio name']):portfolio_id}})
                            elif portfolio_id == 'nan' and str(row['Portfolio name']) == 'No portfolio':
                                self.flag_with_no_portfolio_name_without_id = True  
                                if str(file+'/'+files) not in self.dict_with_no_portfolio_name_without_id:
                                    self.dict_with_no_portfolio_name_without_id[str(file+'/'+files)] = []
                                self.dict_with_no_portfolio_name_without_id[str(file+'/'+files)].append({str(row['campaignName']):{str(row['Portfolio name']):portfolio_id}})
                            elif portfolio_id != 'nan' and str(row['Portfolio name']) == 'No portfolio': 
                                self.flag_no_portfolio_name_with_id = True
                                if str(file+'/'+files) not in self.dict_no_portfolio_name_with_portfolio_id:
                                    self.dict_no_portfolio_name_with_portfolio_id[str(file+'/'+files)] = []
                                self.dict_no_portfolio_name_with_portfolio_id[str(file+'/'+files)].append({str(row['campaignName']):{str(row['Portfolio name']):portfolio_id}})
    
                        #track count for corresponding flags true --------------------- 
                        if self.flag_no_portfolio_id_with_portfolio_name == True: 
                            self.portfolio_id_missing_count += 1
                        if self.flag_with_no_portfolio_name_without_id == True:
                            self.no_portfolio_name_without_id_count += 1 
                        if self.flag_no_portfolio_name_with_id == True:
                            self.no_portfolio_name_with_id_count += 1

                        #print the result of CSV files as per portfolio ID ---------------
                        self.logger.info ("\n")    
                        self.logger.info ("%s:\n 1. Csv file with unique portfolio id : %s,\n 2. Csv file_no_portfolio_id_with_portfolio_name : %s,\n 3. Csv file_with_no_portfolio_name_without_id : %s,\n 4. Csv file_no_portfolio_name_with_portfolio_id : %s "%(csv_file,self.portfolio_id_list,self.dict_with_no_portfolio_id,self.dict_with_no_portfolio_name_without_id,self.dict_no_portfolio_name_with_portfolio_id))
                        self.files.append([file, files, str(self.portfolio_id_list), str(self.dict_with_no_portfolio_id), str(self.dict_with_no_portfolio_name_without_id), str(self.dict_no_portfolio_name_with_portfolio_id)]) 
                        
                        self.csv_file = pd.DataFrame(self.files, columns = self.table_column)    
                        self.csv_file.to_csv(os.getcwd() + "/output/portfolio_validation_%s.csv"%datetime.now().strftime('%y-%m-%d'), index=True, sep=',' , header=True)
                        self.cleanup()                                     
                    except Exception as error:
                        self.logger.info("\n")
                        self.logger.info(error)
                    
        #-------------------------  report generate -------------------------------------------
        self.logger.info("\n")
        self.logger.info("Note : Report generated base on unique portfolio name : \n %s" %self.unique_portfolio_names)
        self.logger.info("\n")
        self.logger.info("Folder wise csv file count {folder_name : csv file count}")
        self.logger.info("\n")
        self.logger.info(self.folder_wise_file_count)
        self.logger.info("\n")
        self.logger.info("Report: ")
        self.logger.info({"total_csv_files tested count " : self.total_files})
        self.logger.info({"csv_file_empty count  " : self.file_empty})
        self.logger.info({"csv_file_is_not_empty count " : self.file_is_not_empty})
        self.logger.info({"Csv_file_with_portfolio_name_with_portfolio_id_count " : self.file_is_not_empty - (self.portfolio_id_missing_count + self.no_portfolio_name_without_id_count + self.no_portfolio_name_with_id_count)})
        self.logger.info({"csv_file portfolio_id_missing with portfolio name count " :  self.portfolio_id_missing_count})
        self.logger.info({"Csv file_with_no_portfolio_name_without_portfolio_id count ": self.no_portfolio_name_without_id_count})
        self.logger.info({"Csv file_no_portfolio_name_with_portfolio_id count ": self.no_portfolio_name_with_id_count}) 
                    
if __name__ == '__main__':
    obj_ = portfolio_id_checking()
    obj_.main()