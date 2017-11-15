y
##########################################################################
# Data Visualization report 
# by Ghicheon Lee
##########################################################################

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# '****' and '***' mean missing data.
df = pd.read_csv('ExcelFormattedGISTEMPDataCSV.csv', na_values=['****','***'])

#get only monthly data 
df = df.ix[:,:13]

#I added new field to get the decade data easily.
df['groupid'] = df.ix[:,0]//10

#make groups with groupid
groups = df.groupby('groupid')

#get the means for each decade.
result = groups.agg('mean')

#well.. just restore index. it's not needed though.
result = result.reset_index()

#let's draw.
plt.figure()


#result.shape[0] is the number of records.
for i in range(result.shape[0]):
        #eliminate groupid and index
        out =  result.ix[i,2:]
        out2 = list(out)

        #last data is for 2015 not 2019.
        if i == (result.shape[0]-1):
                plt.plot(out2, label=str(188+i) + "0 ~ " + str(188+i) +'5')
        else:
                plt.plot(out2, label=str(188+i) + "0 ~ " + str(188+i) +'9')


plt.legend(loc=1)           #on the right side.

#some useful text.
plt.xlabel("from 1880 to 2015 per decade")
plt.ylabel("Deviation")
plt.title("Global and Hemispheric Monthly Means")

#draw it!
plt.show()



