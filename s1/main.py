import logging
from logging.handlers import TimedRotatingFileHandler
import pandas as pd
import glob
import time
import pandas as pd
from dateutil.parser import parse
from datetime import datetime, timedelta
import hashlib
import re
import multiprocessing


logHandler = TimedRotatingFileHandler("./log/logfile.log",when="midnight")
logFormatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
logHandler.setFormatter( logFormatter )
logger = logging.getLogger( 'MyLogger' )
logger.addHandler( logHandler )
logger.setLevel( logging.INFO )

def find_all_uppercase_words(name):
    # 使用findall方法和正则表达式来找到所有纯大写的单词
    #return re.findall(r"(Mr\.|Dr\.|Miss\.|Dr\.|Dr\.|)\s+", name)
    if len(name.split(' '))>2:
    	return (name)
    else:
    	return (None)

def clean_title(name):
    title_re = r"Mr\.|Miss|III|MD|Jr\.|PhD|DDS|Mrs\.|Dr\.|DVM|Ms\.|II"
    return (re.sub(title_re, '', name).strip())


def sourceProcessing():

	for file in glob.glob('sourceData/*.csv'):
		filename = file.split('/')[-1].split('.')[0]
		data = pd.read_csv(file)

		data['birthdate'] = data['date_of_birth'].apply(lambda x: parse(x).strftime('%Y%m%d'))

		#today = datetime.today()
		date_str = '2022-01-01'
		date_obj = datetime.strptime(date_str, '%Y-%m-%d')
		data['age'] = (date_obj - pd.to_datetime(data['birthdate'], format='%Y-%m-%d')).astype('<m8[Y]')
		data['above_18'] = data['age'] > 18

		data['name'] = data['name'].apply(clean_title)

		name_not_null = data['name'].notnull()
		data['mobile_no'] = data['mobile_no'].astype(str).str.replace(' ','')
		mobile_valid = data['mobile_no'].astype(str).str.match(r'^\d{8}$')
		age_above_18 = data['age'] > 18
		email_valid = data['email'].str.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.(com|net)$')

		successful_df = data[name_not_null & mobile_valid & age_above_18 & email_valid]
		unsuccessful_df = data[~(name_not_null & mobile_valid & age_above_18 & email_valid)]

		#successful_df['first_name'] = ''
		#successful_df['last_name'] = ''
	
		successful_df[['first_name', 'last_name']] = successful_df['name'].str.split(' ', 1, expand=True)
		successful_df['membership_id'] = successful_df.apply(lambda x: '{}_{}'.format(x['last_name'] if x['last_name']!='' else 'UNKNOWN', hashlib.sha256(str(x['birthdate']).encode()).hexdigest()[:5]), axis=1)

		del successful_df['age']
		del unsuccessful_df['age']

		successful_df.to_csv(f'processedData/successful/{filename}.csv', index=False)
		unsuccessful_df.to_csv(f'processedData/unsuccessful/{filename}.csv', index=False)

	return(1)

if __name__ == "__main__":

	t1 = time.time()

	logger.info(f"Start the processing at {time.strftime('%Y-%m-%d %H:%M:%S',time.gmtime(time.time()))}.")

	for file in glob.glob('sourceData/*.csv'):
		print(file)

	sourceProcessing()

	t2 = time.time()

	logger.info(f"It takes {t2-t1} seconds to complete the processing.")
	


