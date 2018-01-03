##########################################################################
# simple Data Visualization 
##########################################################################

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('ExcelFormattedGISTEMPData2CSV.csv')


# 'F -> 'C
glob = (df['Glob'] -32) /1.8
north = (df['NHem'] -32)/1.8
south = (df['SHem'] -32)/1.8

year = df['Year']


#let's draw.
plt.figure()

plt.plot(year,glob, color='g')
plt.plot(year,north, color='r')
plt.plot(year,south,  color='b')

plt.legend(loc=0)           

plt.xlabel("Year")
plt.ylabel("Temperature('C)")
plt.title("Global Temperature trend from" + str(year[0]))

plt.show()



