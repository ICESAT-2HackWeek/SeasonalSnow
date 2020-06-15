# Convert ICESat-2 HDF5 to EPT

## Requirements

### Install PDAL

See https://pdal.io/quickstart.html, however note...

...you need the ensure the [HDF Reader](https://github.com/PDAL/PDAL/blob/ept/doc/stages/readers.hdf.rst) installed which doesn't come "out of the box". To get the HDF plugin working, I installed pdal using the OSX scripts for conda installation: [PDAL/scripts/conda](https://github.com/PDAL/PDAL/tree/master/scripts/conda). This installation includes the [HDF plugin](https://github.com/PDAL/PDAL/blob/master/scripts/conda/osx.sh#L23). See `osx-setup.sh` and `osx.sh`.

Important note: set the `PDAL_DRIVER_PATH` to the location of your conda-build installation, for example `export PDAL_DRIVE_PATH=~/PDAL/conda-build/lib`.

### Install entwine

https://entwine.io/quickstart.html

### Get earthdata credentials (and export them as environment variables)

* Create an account if you don't have one already https://urs.earthdata.nasa.gov/
* Export those credentials as environment variables

```bash
export EARTHDATA_USERNAME=XXX
export EARTHDATA_PASSWORD=XXX
```

## Run the conversion

1. Download the ATL03 product

```bash
wget --user=$EARTHDATA_USERNAME --password=$EARTHDATA_PASSWORD https://n5eil01u.ecs.nsidc.org/ATLAS/ATL03.003/2018.10.13/ATL03_20181013235645_02340114_003_01.h5
```

2. Generate las file

```bash
pdal pipeline atl03-pipeline.json
```

3. Generate the EPT

```bash
entwine build -i output.las -o entwine/atl03
```

