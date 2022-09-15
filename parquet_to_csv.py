import pandas as pd
import os
import pdb

pdb.set_trace()

input_file_path = os.path.join('data', 'decals_dr5', 'decals_dr5_ortho_test_catalog.parquet')
out_file_path = os.path.join('data', 'decals_dr5', 'decals_dr5_ortho_test_catalog.csv')

df = pd.read_parquet(input_file_path)
df.to_csv(out_file_path)

csv_input_file_path = 'data/workflow-3598-2022-07-06T155315+0000.csv'
csv_df = pd.read_csv(csv_input_file_path)

# join data frames but only include the common columns in both (outer would set missing entries to NaN)
pd.concat([df, csv_df], ignore_index=True, join="inner")

# write a dataframe to parquet
train_catalog.to_parquet('/home/walml/repos/pytorch-galaxy-datasets/roots/decals_dr5/decals_dr5_ortho_train_catalog.parquet', index=False)

# original parquet file
orig_parquet_file = os.path.join('data', 'decals_dr5', 'decals_dr5_ortho_catalog.parquet.orig')
zoobot_parquet_file = os.path.join('data', 'decals_dr5', 'decals_dr5_ortho_catalog.parquet')
kade_file = os.path.join('data', 'workflow-3598-2022-07-06T155315+0000.csv')
# csv_file = os.path.join('data', 'decals_dr5', 'decals_dr5_ortho_catalog.csv')

df = pd.read_parquet(orig_parquet_file)
kdf = pd.read_csv(kade_file)

# extract only the kade manifest column data from the larger mission catalog
# this allows us to modify the kade manifest and automatically include the mission column data
# as we progress with adding new mission data (e.g. decals 1&2 etc)
# mission_catalog = df[kdf.columns]

# note we want to operate on the whole decals 12, 5, 8 df so we can easily subset them at zoobot runtime

# change the file location paths to match our blob storage system
df['file_loc'] = df['file_loc'].str.replace('/share/nas/walml/galaxy_zoo/decals/dr5/png/dr5', '/mnt/batch/tasks/fsmounts/training/catalogues/decals_dr5/images')

# find the png files in the mission catalogue (all existing files are png apparently!?)
df["file_loc"].count()
df["file_loc"].str.endswith('.png').value_counts()
# replace the /png extensions with .jpg
df['file_loc'] = df['file_loc'].str.replace('\.png', '.jpg')
df["file_loc"].str.endswith('.png').value_counts()
df["file_loc"].str.endswith('.jpg').value_counts()

# write the mission catalog to parquet
df.to_parquet(zoobot_parquet_file, index=False)

# combine the dataframes into one catalog
# catalog = pd.concat([kdf, mission_catalog], ignore_index=True)
