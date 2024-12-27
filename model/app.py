from fpgrowth_py import fpgrowth
import pandas as pd
import  pickle
from datetime import datetime

df = pd.read_csv('https://homepages.dcc.ufmg.br/~cunha/hosted/cloudcomp-2023s2-datasets/2023_spotify_ds1.csv', usecols=[6, 7])

playlists = df.groupby('pid')['track_name'].apply(list).tolist()

freqItemSet, rules = fpgrowth(playlists, minSupRatio=0.07, minConf=0.1)

store = {
    'createdAt': datetime.now().isoformat(),
    'rules': rules
}

FILE = open('/data/model_rules', 'wb')

pickle.dump(store, FILE)

FILE.close()