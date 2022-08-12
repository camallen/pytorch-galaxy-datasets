from pytorch_galaxy_datasets.prepared_datasets import dr5
import os
import pdb

# first download is basically just a convenient way to get the images and canonical catalogs
catalog, label_cols = dr5.decals_dr5_setup(
    root=os.path.join('data', 'decals_dr5'),
    train=True,
    download=True
)
pdb.set_trace()
adjusted_catalog = catalog.sample(1000)
