import seaborn
import pandas as pd
import os
import matplotlib.pyplot as plt
from tqdm import tqdm




files = ['2366-zeya-blagoveshensk.csv', '1003-zeya-svobodny.csv', '317-zeya-belogorye.csv', '1002-zeya-malayasazanka.csv', '316-zeya-mazanovo.csv']

dirName = 'pointplot'
try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
except FileExistsError:
        print("Directory " , dirName ,  " already exists")

for file in tqdm(files):
    if file.endswith(".csv"):
        df = pd.read_csv(file, sep=';')
        df['Timestamp'] = pd.to_datetime(df["Timestamp"]).dt.strftime("%Y%m%d").astype(int)
        df['Timestamp'] = df['Timestamp'] - (df['Timestamp'].min())
        res = seaborn.pointplot(x='Timestamp', y='Value', data=df)
        #res.savefig('catplot_' + file[:-4] + '.png')
        
        plt.savefig(dirName + '/' + file[:-4] + '.png')
#df = pd.read_csv('1002-zeya-malayasazanka.csv', sep=';')
#res = seaborn.catplot(data=df)
#plt.show()



#print(df.describe())