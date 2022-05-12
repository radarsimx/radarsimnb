<a href="https://radarsimx.github.io/radarsimpy/" target="_blank" rel="nofollow"><img src="https://img.shields.io/badge/Documentation-latest-brightgree?style=flat&logo=read-the-docs" height="20"></a>

# Jupyter Notebook Examples for RadarSimPy

<img src="https://github.com/radarsimx/radarsimpy/blob/master/assets/radarsimnb.svg" alt="logo" width="200"/>

Jupyter notebooks for radar systems simulation based on `RadarSimPy` & `RadarSimC`.

- [`RadarSimPy`](https://radarsimx.com/radarsimx/radarsimpy/) is a radar simulation package built with python
- [`RadarSimC`](https://radarsimx.com/radarsimx/radarsimc/) is the C++/CUDA backend of `RadarSimPy`

## Dependence

- numpy
- scipy
- [PyMeshLab](https://github.com/cnr-isti-vclab/PyMeshLab)
- [Visual C++ Runtime](https://aka.ms/vs/16/release/vc_redist.x64.exe/) (*Windows only*)

## Installation

To use the module, please put the radarsimpy folder within your project folder as shown below.

---

- ### Windows
  - your_project.py
  - your_project.ipynb
  - radarsimpy
    - \_\_init__.py
    - radarsimc.dll
    - scene.xxx.pyd
    - ...

---

- ### Linux
  - your_project.py
  - your_project.ipynb
  - radarsimpy
    - \_\_init__.py
    - libradarsimc.so
    - scene.xxx.so
    - ...

---

## Coordinate Systems

- ### Scene Coordinate

  - axis (m): `[x, y, z]`
  - phi (deg): angle on x-y plane. Positive x-axis is 0 deg, positive y-axis is 90 deg
  - theta (deg): angle on z-x plane. Positive z-axis is 0 deg, x-y plane is 90 deg
  - azimuth (deg): azimuth -90 ~ 90 deg equal to phi -90 ~ 90 deg
  - elevation (deg): elevation -90 ~ 90 deg equal to theta 180 ~ 0 deg

- ### Object's Local Coordinate

  - axis (m): `[x, y, z]`
  - yaw (deg): rotation along z-axis. Positive yaw rotates object from positive x-axis to positive y-axis
  - pitch (deg): rotation along y-axis. Positive pitch rotates object from positive x-axis to positive z-axis
  - roll (deg): rotation along x-axis. Positive roll rotates object from positive z-axis to negative y-axis
  - origin (m): `[x, y, z]`
  - rotation (deg): `[yaw, pitch, roll]`
  - rotation (deg/s): rate `[yaw rate, pitch rate, roll rate]`

## Usage Examples

- ### Radar modeling and point target simulation
  - [Doppler radar](./notebooks/doppler_radar.ipynb)
  - [FMCW radar](./notebooks/fmcw_radar.ipynb)
  - [TDM MIMO FMCW radar](./notebooks/tdm_mimo_fmcw_radar.ipynb)
  - [PMCW radar](./notebooks/pmcw_radar.ipynb)
  - [Arbitrary waveform](./notebooks/arbitrary_waveform.ipynb)
  - [Phase noise](./notebooks/phase_noise.ipynb)
  - [CFAR](./notebooks/cfar.ipynb)

- ### Radar modeling and 3D scene simulation with raytracing
  - [Imaging radar](./notebooks/rt_fmcw_imaging_radar.ipynb)
  - [FMCW radar with a corner reflector](./notebooks/rt_fmcw_corner_reflector.ipynb)
  - [FMCW radar with a plate](./notebooks/rt_fmcw_plate.ipynb)
  - [FMCW radar with a car](./notebooks/rt_fmcw_car.ipynb)
  - [Doppler of a turbine](./notebooks/rt_doppler_turbine.ipynb)
  - [Micro-Doppler](./notebooks/rt_micro_doppler.ipynb)
  - [Multi-path effect](./notebooks/rt_multi_path.ipynb)

- ### 3D modeled target's RCS simulation
  - [Corner reflector RCS](./notebooks/rcs_corner_reflector.ipynb)
  - [Plate RCS](./notebooks/rcs_plate.ipynb)
  - [Car RCS](./notebooks/rcs_car.ipynb)

- ### LiDAR point cloud
  - [LIDAR point cloud](./notebooks/lidar.ipynb)

- ### Characterization
  - [Receiver operating characteristic (ROC)](./notebooks/roc.ipynb)
