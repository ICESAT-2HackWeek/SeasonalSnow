## IceSat-2 to LAZ

Steps to convert a IceSat-2 HDF granule file to a LAZ file using PDAL

## Convert the HDF
In order to use the `signal_conf_ph` quality flag, we need to convert the mulitdimensional array of the HDF file to a single integer value.
For that, use the prepare_hdf_to_laz.py to process each beam.

Example:
```bash
prepare_hdf_to_laz.py --input-file processed_ATL03_20191008182255_01810506_003_01.h5 --beam gt1r
```

## Use PDAL pipeline to convert to LAZ
Example:
```bash
bin/pdal pipeline ~/SeasonalSnow/contributors/jomey/hdf_to_laz.json --readers.hdf.filename=/home/jovyan/shared/data-aragon/ATL03_CA/processed_ATL03_20191008182255_01810506_003_01_gt1r_xyz_conf.h5 --writers.las.filename=/home/jovyan/shared/data-aragon/ATL03_CA/processed_ATL03_20191008182255_01810506_003_01_gt1r_xyz_conf.laz
```
