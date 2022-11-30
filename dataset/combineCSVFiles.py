import pandas as pd
import glob


csv_files = glob.glob('*.{}'.format('csv'))
df_concat = pd.concat([pd.read_csv(f) for f in csv_files ])
df_concat.to_csv("combined.csv")
