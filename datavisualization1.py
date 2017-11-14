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

for i in range(result.shape[0]):
        out =  result.ix[i,2:]
        out2 = list(out)
        plt.plot(out2, label=str(i))

plt.legend(loc=1)
plt.show()





data = {
'1 ':[1,2,3],
'2 ':[1,2,3],
'3 ':[1,2,3],
'4 ':[1,2,3],
'5 ':[1,2,3],
'6 ':[1,2,3],
'7 ':[1,2,3],
'8 ':[1,2,3],
'9 ':[1,2,3],
'10':[1,2,3],
'11':[1,2,3],
'12':[1,2,3],
'13':[1,2,3]}


x = pd.DataFrame(data)
x.groupby('1')



df2 = pd.read_csv('ExcelFormattedGISTEMPData2CSV.csv')

//df.replace(22122,'English', inplace=True)

stack = df.stack()
stack[ stack == '****'] = 0
stack[ stack == '***'] = 0
stack.unstack()
