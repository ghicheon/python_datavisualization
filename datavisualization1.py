import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('ExcelFormattedGISTEMPDataCSV.csv', na_values=['****','***'])

df = df.ix[:,:13]

df['groupid'] = df.ix[:,0]//10

groups = df.groupby('groupid')

result = groups.agg('mean')

result = result.reset_index()

plt.figure()



years=[]

for i in range(result.shape[0]):
        years.append(188+i)

for i in range(result.shape[0]):
        out =  result.ix[i,2:]
        out2 = list(out)
        if i == (result.shape[0]-1):
                plt.plot(out2, label=str(188+i) + "0 ~ " + str(188+i) +'5')
        else:
                plt.plot(out2, label=str(188+i) + "0 ~ " + str(188+i) +'9')


plt.legend(loc=1)
plt.show()






















#df.replace(22122,'English', inplace=True)
#
#stack = df.stack()
#stack[ stack == '****'] = 0
#stack[ stack == '***'] = 0
#stack.unstack()
plt.xlabel("years")
plt.ylabel("temperature")
plt.title("temperature")
plt.axis([1880,2015,-100,100])
plt.grid(True)

