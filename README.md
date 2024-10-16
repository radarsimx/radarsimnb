[![Documentations](https://img.shields.io/github/v/tag/radarsimx/radarsimpy?label=Documentation&logo=read-the-docs)](https://radarsimx.github.io/radarsimpy/)
[![Download](https://img.shields.io/github/v/tag/radarsimx/radarsimpy?label=Download&logo=python)](https://radarsimx.com/product/radarsimpy/)

# Jupyter Notebook Examples of RadarSimPy

<img src="https://github.com/radarsimx/radarsimpy/blob/master/assets/radarsimnb.svg" alt="logo" width="200"/>

Jupyter notebooks of radar systems simulation based on `RadarSimPy` & `RadarSimCpp`.

- [`RadarSimPy`](https://radarsimx.com/radarsimx/radarsimpy/) is a radar simulation package built with python
- [`RadarSimCpp`](https://radarsimx.com/radarsimx/radarsimcpp/) is the C++/CUDA backend of `RadarSimPy`

## Dependence

- numpy
- scipy
- [PyMeshLab](https://github.com/cnr-isti-vclab/PyMeshLab)

## Installation

To use the module, please put the radarsimpy folder within your project folder as shown below.

---

- ### Windows

  - your_project.py
  - your_project.ipynb
  - radarsimpy
    - \_\_init__.py
    - radarsimcpp.dll
    - scene.xxx.pyd
    - ...

---

- ### Linux

  - your_project.py
  - your_project.ipynb
  - radarsimpy
    - \_\_init__.py
    - libradarsimcpp.so
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

Check [Jupyter notebooks](./notebooks) or visit [radarsimx.com](https://radarsimx.com/category/examples/).
