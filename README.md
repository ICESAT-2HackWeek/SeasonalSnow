# SeasonalSnow
IceSat-2 Snowdepth and SWE over mountains: a workflow using satellite laser altimetry to resolve topography/SWE(snow water equivalent) over complex terrain.

### General Objective
Compare and evaluate ICESat-2 data with high resolution DEMs (airborne lidar/satellite stereo) collected at lower latitudes, charecterize accuracy and explore potential of seasonal SWE estimation. We will be building upon 2019 ICESat-2 HackWeek projects, namely [topohack](https://github.com/ICESAT-2HackWeek/topohack) and []().

## Collaborators
- David Hill
- Friedrich Knuth
- Jawaria Ahmad
- Michelle Hu
- Aimee Barciauskas
- Rosemary Willatt
- Isobel Lawrence

### Team Lead 
Nina Argon

### Data Science Leads
Joachim Meyer

Shashank Bhushan

### DataSets
- ICESat-2 [ATL06](https://nsidc.org/data/atl06?qt-data_set_tabs=3#qt-data_set_tabs) (20 m resolution)
- ICESat-2 [ATL03](https://nsidc.org/data/atl03) (geolocated points along track)
- ICESat-2 [ATL08] (surface classification)
- Bareground data ([LULC for US](https://www.mrlc.gov/data/legends/national-land-cover-database-2011-nlcd2011-legend) 
- [ASO Lidar](https://nsidc.org/data/aso)
- [WADNR Lidar](http://lidarportal.dnr.wa.gov/)
- [C-SNOW](https://ees.kuleuven.be/apps/project-c-snow-data/)


### Tools
- Python Scientific Analysis Stack, Geospatial Stack
- [pdal](https://pdal.io/)
- [icepyx](https://github.com/icesat2py/icepyx)

### High-level Goals (Tentative)
- Learn how to access ICESat-2 data efficiently with icepyx.
- Evaluate/Compare the topography resolved by ICESat-2 ATLO6 and ATL03 profiles along steep mountains with topographic profiles returned from high-resolution DEMs.
- Classify IceSat-2 ATL06 or ATL03 measurements as snow-on or snow-off using remote sensing product such as C-SNOW.
- Get a sense of snow accumulation (depth) by comparing Snow-off DEM over Grand Mesa and other ASO sites with winter (October to February) IceSat-2 collects.
- Snow-depth to SWE conversion.
- Evaluate the accuaracy of the derived SWE.
- Compare ATL03 with ATL06. Quantify uncetainty in snow volume estimates using snow depth derived using ATL03 vs ATL06.
- Breakdown/analyse/process ATLO3 pointcloud using pdal.
- Explore ATL03 and ATL07/ATL06 products over Sea-ice
- Seasonal snow over sea-ice
- Convert ATL03 data to entwine (cloud-optimised point cloud format) and visualise on potree
- Bulk snodas download scripts
- Compare ATL06 elevations with raster DEM

### Study Sites:
- Areas with ground truth LiDAR/SWE estimates avalible (eg. Airborne Snow Observatory(ASO) sites)
- TBD

### Team Contribution Workflow:
We will strive to follow the [workflow](https://icesat-2hackweek.github.io/learning-resources/projects/example_workflow/) proposed by the Hackweek team. This should make our life easier, free of any *merge* conflicts.
