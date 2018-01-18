# -*- coding: utf-8 -*-
import dateutil.parser
from datetime import datetime
from pytz import timezone
import os
import urllib

def aversinv_convertdate(isodate):
    date = dateutil.parser.parse(isodate)
    return date.strftime("%Y-%m-%d %H:%M")

def add_timezone_to_date(date_str):
    new_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    TZ = timezone(os.environ['TZ'] if 'TZ' in os.environ else 'Europe/Kiev')
    new_date_timezone = TZ.localize(new_date)
    return new_date_timezone.strftime("%Y-%m-%d %H:%M:%S%z")

def convert_aversinv_date_to_iso_format(date_time_from_ui):
    new_timedata = datetime.strptime(date_time_from_ui, '%d-%m-%Y\n%H:%M')
    new_date_time_string = new_timedata.strftime("%Y-%m-%d %H:%M:%S.%f")
    return new_date_time_string

def aversinv_download_file(url, file_name, output_dir):
    urllib.urlretrieve(url, ('{}/{}'.format(output_dir, file_name)))

def convert_aversinv_string(string):
    return {
            'True':                                                 '1',
            'False':                                                '0',
            u"Так":                                                 True,
            u"Hi":                                                  False,
            u'Очікування пропозицій':                               'active.tendering',
            u'Період аукціону':                                     'active.auction',
            u'Кваліфікація переможця':                              'active.qualification',
            u'Пропозиції розглянуто':                               'active.awarded',
            u'Аукціон не відбувся':                                 'unsuccessful',
            u'Аукціон завершено':                                   'complete',
            u'Аукціон відмінено':                                   'cancelled',
            u'Чорновик':                                            'draft',
            u'Майна банків':                                        'dgfOtherAssets',
            u'Прав вимоги за кредитами':                            'dgfFinancialAssets',
            u'Голландський аукціон':                                'dgfInsider',
            u'Вперше':                                              1,
            u'Вдруге':                                              2,
            u'Втретє':                                              3,
            u'Вчетверте':                                           4,
            u'Грн.':                                                'UAH',
            u'(включно з ПДВ)':                                     True,
            u'(без ПДВ)':                                           False,
            u'[переможець розглядається кваліфікаційною комісією]': 'pending',
            u'[Oчікування кінця кваліфікації переможця]':           'pending.waiting',
            u'[Учасник достроково забрав гарантійний внесок]':      'cancelled',
            u'[Очікується протокол]':                               'pending.verification',
            u'[Очікується оплата]':                                 'pending.payment',
            u'[Оплачено, очікується підписання договору]':          'active',
            u'[Кваліфікаційна комісія відмовила переможцю]':        'unsuccessful',
            }.get(string, string)
