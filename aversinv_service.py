# -*- coding: utf-8 -*-
import dateutil.parser
from datetime import datetime
from pytz import timezone
import os
import urllib

def avirsinv_convertdate(isodate):
    date = dateutil.parser.parse(isodate)
    return date.strftime("%d.%m.%Y %H:%M")
	
def avirsinv_remove_space(value):
    return value.replace(" ", "").replace(u' ', '')

def avirsinv_replace_todot(value):
    return value.replace(",", ".")
	
def avirsinv_convert_usnumber(value):
    return avirsinv_replace_todot(avirsinv_remove_space(value))
	
def avirsinv_contains(value1, value2):
	if value2 in value1:
		return 1
	else:
		return 0
		
def avirsinv_replace(value, strfrom, strto):
    return value.replace(strfrom, strto)
	
def avirsinv_remove(value, str):
    return avirsinv_replace(value, str, "")
	
def get_upload_file_path():
    return os.path.join(os.getcwd(), 'src/robot_tests.broker.avirsinv/eTestFileForUpload.txt')
	
def set_procuringEntity_name(tender_data, name):
   tender_data['data']['procuringEntity']['name'] = name
   return tender_data
	
def convert_avirsinv_date_to_iso_format(date_time_from_ui):
    if date_time_from_ui.strip() == "":
       return date_time_from_ui.strip()
    new_timedata = datetime.strptime(date_time_from_ui, '%d.%m.%Y %H:%M')
    new_date_time_string = new_timedata.strftime("%Y-%m-%d %H:%M:%S.%f")
    return new_date_time_string
	
def convert_avirsinv_sdate_to_iso_format(date_time_from_ui):
    if date_time_from_ui.strip() == "":
       return date_time_from_ui.strip()
    new_timedata = datetime.strptime(date_time_from_ui, '%d.%m.%Y')
    new_date_time_string = new_timedata.strftime("%Y-%m-%d %H:%M:%S.%f")
    return new_date_time_string
	
def convert_avirsinv_sdate_to_iso_sdate_format(date_time_from_ui):
    if date_time_from_ui.strip() == "":
       return date_time_from_ui.strip()
    new_timedata = datetime.strptime(date_time_from_ui, '%d.%m.%Y')
    new_date_time_string = new_timedata.strftime("%Y-%m-%d")
    return new_date_time_string

def add_timezone_to_date(date_str):
    if date_str.strip() == "":
       return date_str.strip()
    new_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    TZ = timezone(os.environ['TZ'] if 'TZ' in os.environ else 'Europe/Kiev')
    new_date_timezone = TZ.localize(new_date)
    return new_date_timezone.strftime("%Y-%m-%d %H:%M:%S%z")

def split_descr(str):
    return str.split(' - ')[1];

def avirsinv_download_file(url, file_name, output_dir):
    urllib.urlretrieve(url, ('{}/{}'.format(output_dir, file_name)))

def convert_avirsinv_string(string):
    return {
            'True': '1',
            'False': '0',
            u"Так": True,
            u"Hi":  False,
            u"Yes": True,
            u"No":  False,
            u"Да": True,
            u"Нет":  False,
            u'Очікування пропозицій':  'active.tendering',
            u'Період аукціону':        'active.auction',
            u'Кваліфікація переможця': 'active.qualification',
            u'Пропозиції розглянуто':  'active.awarded',
            u'Аукціон не відбувся':    'unsuccessful',
            u'Аукціон завершено':      'complete',
            u'Аукціон відмінено':      'cancelled',
            u'Чернетка':               'draft',
            u'Майна банків':           'dgfOtherAssets',
            u'Прав вимоги за кредитами': 'dgfFinancialAssets',
            u'Голландський аукціон':   'dgfInsider',
            u'Грн.': 'UAH',
            u'(включно з ПДВ)': True,
            u'(без ПДВ)': False,
            u'вперше': 1,
            u'вдруге': 2,
            u'третій раз': 3,
            u'четвертий раз': 4,
            u'не відомо': '',
            }.get(string, string)
			
def convert_documentType_string(string):
    return {
            'technicalSpecifications': '3',
            'commercialProposal': '22',
            'eligibilityDocuments': '24',
            'tenderNotice': '28',
            'virtualDataRoom': '29',
            'illustration': '30',
            'financialLicense': '31',
            'x_dgfPublicAssetCertificate': '33',
            'x_presentation': '34',
            'x_nda': '35',
            'x_dgfAssetFamiliarization': '37',
            }.get(string, string)
