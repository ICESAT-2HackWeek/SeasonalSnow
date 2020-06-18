## IceSat-2 to LAZ

Steps to convert a IceSat-2 HDF granule file to a LAZ file using PDAL

## Convert the HDF
In order to use the `signal_conf_ph` quality flag, we need to convert the mulitdimensional array of the HDF file to a single integer value. Also,
since the 'UserData' flag of the LAS file specification does not allow negative
values, all '-1' values will be set to 127.
For that, use the prepare_hdf_to_laz.py to process each beam.

Example:
```bash
prepare_hdf_to_laz.py --input-file processed_ATL03_20191008182255_01810506_003_01.h5 --beam gt1r
```

ATL 03 spec: https://icesat-2.gsfc.nasa.gov/sites/default/files/u71/ICESat2_ATL03_ATBD_r003_v2.pdf
PDAL dimensions: https://pdal.io/dimensions.html

## Use PDAL pipeline to convert form HDF to LAZ
Example:
```bash
bin/pdal pipeline ~/SeasonalSnow/contributors/jomey/hdf_to_laz.json --readers.hdf.filename=/home/jovyan/shared/data-aragon/ATL03_CA/processed_ATL03_20191008182255_01810506_003_01_gt1r_xyz_conf.h5 --writers.las.filename=/home/jovyan/shared/data-aragon/ATL03_CA/processed_ATL03_20191008182255_01810506_003_01_gt1r_xyz_conf.laz
```
## Use PDAL pipeline to convert from LAZ to GeoTiff
Example:
```bash
bin/pdal pipeline ~/SeasonalSnow/contributors/jomey/laz_to_tiff.json --readers.las.filename=/home/jovyan/shared/data-aragon/ATL03_CA/processed_ATL03_20191008182255_01810506_003_01_gt1r_xyz_conf.laz --writers.gdal.filename=/home/jovyan/shared/data-aragon/ATL03_CA/processed_ATL03_20191008182255_01810506_003_01_gt1r_xyz_conf.tif
```
