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
