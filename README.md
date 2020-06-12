# SeasonalSnow
IceSat-2 and SWE over mountains: a workflow using satellite laser altimetry to resolve topography/SWE(snow water equivalent) over complex terrain.

### General Objective
Compare and evaluate ICESat-2 data with high resolution DEMs (airborne lidar/satellite stereo) collected at lower latitudes, charecterize accuracy and explore potential of seasonal SWE estimation. We will be building upon 2019 ICESat-2 HackWeek projects, namely [topohack](https://github.com/ICESAT-2HackWeek/topohack) and []().

## Collaborators
David Hill
Jared Klemm
Shashank Bhushan
Anna Valentine
Charlie Hewitt
Friedrich Knuth
Jawaria Ahmad
Jordi Bolibar
Kar
Lucal Zeller
Michael Loso
Michelle Hu

### Team Lead 
Nina Argon

### Data Science Lead
TBD 

### DataSets
- ICESat-2 [ATL06](https://nsidc.org/data/atl06?qt-data_set_tabs=3#qt-data_set_tabs) (20 m resolution)
- ICESat-2 ATL03 (geolocated points along track)
- Bareground data ([LULC for US](https://www.mrlc.gov/data/legends/national-land-cover-database-2011-nlcd2011-legend) 
- [ASO Lidar](https://nsidc.org/data/aso)
- [WADNR Lidar](http://lidarportal.dnr.wa.gov/)

### Tools
- Python Scientific Analysis Stack, Geospatial Stack
- [pdal](https://pdal.io/)

### High-level Goals (Tentive High Level Goals)
- Learn how to access ICESat-2 data efficiently with icepyx.
- Evaluate/Compare the topography resolved by ICESat-2 ATLO6 profiles along steep mountains with topographic profiles returned from high-resolution DEMs.
- Get a sense of snow accumulation (depth) by comparing Snow-off DEM over Grand Mesa and other ASO sites with winter (October to February) IceSat-2 collects.
- Snow-depth to SWE conversion
- Evaluate the accuaracy of the derived SWE.
- Compare ATL03 with ATL06
- Breakdown/analyse/process ATLO3 pointcloud using pdal.
- Surface classification (snow/non-snow, wet-snow/dry snow) using ICESat-2 ATL03/ATL06 data.

### Study Sites:
- Areas with ground truth LiDAR/SWE estimates avalible (eg. Airborne Snow Observatory(ASO) sites)
- TBD

### Team Contribution Workflow:
    We will strive to follow the [workflow](https://icesat-2hackweek.github.io/learning-resources/projects/example_workflow/) proposed by the Hackweek team. This should makes our life easier, free of any conflicts.
