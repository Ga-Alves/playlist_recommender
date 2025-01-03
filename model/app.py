from fpgrowth_py import fpgrowth
import pandas as pd
import  pickle
from datetime import datetime, timezone, timedelta
import ssl
import os

DATASET = os.environ.get('DATASET')

ssl._create_default_https_context = ssl._create_unverified_context

df = pd.read_csv(DATASET, usecols=[6, 7])

playlists = df.groupby('pid')['track_name'].apply(list).tolist()

freqItemSet, rules = fpgrowth(playlists, minSupRatio=0.07, minConf=0.1)

brasil_timezone = timezone(timedelta(hours=-3))

store = {
    'createdAt': datetime.now(brasil_timezone).isoformat(),
    'rules': rules
}

FILE = open('/data/model_rules', 'wb')

pickle.dump(store, FILE)

FILE.close()