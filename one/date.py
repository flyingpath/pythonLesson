#%%
from datetime import datetime, timedelta

A=datetime.now().strftime('%Y/%m/%d%H%M')
print(A)
 #2017/11/012253
#%%
A=datetime.strptime("201701012330", "%Y%m%d%H%M%S")   
print(A.strftime('%Y/%m/%d %H%M'))
 #2017/01/01 2303

#%%
A = A - timedelta(days =1)
print((datetime.now() - timedelta(days = 1)).strftime('%Y/%m/%d %H%M'))
 #2017/10/31 2253