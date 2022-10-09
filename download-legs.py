from pytorch_galaxy_datasets.prepared_datasets import legs
import os
import logging

logging.basicConfig(level=logging.INFO)

# first download is basically just a convenient way to get the images and canonical catalogs
catalog, label_cols = legs.legs_setup(
    root=os.path.join('data', 'all_decals'),
    split='train',
    download=True
)
