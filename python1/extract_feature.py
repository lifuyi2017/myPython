import pandas as pd
import numpy as np
from datetime import date


off_train = pd.read_csv('F:\data\O2O\ccf_offline_stage1_train.csv',header=None)
off_train.columns = ['user_id','merchant_id','coupon_id','discount_rate','distance','date_received','date']

for row in off_train.date:
    print row

off_test = pd.read_csv('F:\data\O2O\ccf_offline_stage1_test_revised.csv',header=None)
off_test.columns = ['user_id','merchant_id','coupon_id','discount_rate','distance','date_received']

on_train = pd.read_csv('F:\data\O2O\ccf_online_stage1_train.csv',header=None)
on_train.columns = ['user_id','merchant_id','action','coupon_id','discount_rate','date_received','date']

print '==============================================================='

dataset3 = off_test
feature3 = off_train[((off_train.date>='20160315')&(off_train.date<='20160630'))|((off_train.date=='null')&(off_train.date_received>='20160315')&(off_train.date_received<='20160630'))]

for row in feature3.user_id:
    print row


dataset2 = off_train[(off_train.date_received>='20160515')&(off_train.date_received<='20160615')]
feature2 = off_train[(off_train.date>='20160201')&(off_train.date<='20160514')|((off_train.date=='null')&(off_train.date_received>='20160201')&(off_train.date_received<='20160514'))]
dataset1 = off_train[(off_train.date_received>='20160414')&(off_train.date_received<='20160514')]
feature1 = off_train[(off_train.date>='20160101')&(off_train.date<='20160413')|((off_train.date=='null')&(off_train.date_received>='20160101')&(off_train.date_received<='20160413'))]








