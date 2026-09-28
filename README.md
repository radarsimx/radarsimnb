# RadarSimNb

<img src="https://raw.githubusercontent.com/radarsimx/.github/refs/heads/main/profile/radarsimnb.svg" alt="logo" width="200"/>

`RadarSimNb` is a collection of Jupyter Notebooks providing hands-on examples for [`RadarSimPy`](https://radarsimx.com) — a Python radar simulation library with a C++ back-end. The notebooks cover the full simulation workflow: waveform design, MIMO and imaging, scene simulation, RCS computation, detection, and hardware impairments. Explore the [online examples](https://radarsimx.com/category/examples/) to dive in.

## Setup

Install the Python dependencies:

```sh
pip install -r requirements.txt
```

`RadarSimPy` itself is not on the list. Download it from [radarsimx.com](https://radarsimx.com) and unzip the `radarsimpy` folder into `notebooks/` so the notebooks can `import radarsimpy`.

## Notebooks

Each notebook's filename starts with its category key (`waveform_`, `mimo_`, `imaging_`, `scene_`, `rcs_`, `detection_`, `impairment_`, `lidar_`), which matches the categories on [radarsimx.com](https://radarsimx.com/category/examples/).

<!-- index:start -->
<!-- Generated from catalog.yml by scripts/build_index.py. Do not edit by hand. -->

### Radar Waveforms

Waveform design and the processing chain that goes with it.

| Notebook | Title | Post |
|---|---|---|
| [waveform_fmcw_radar](notebooks/waveform_fmcw_radar.ipynb) | FMCW Radar: Complete Range-Doppler Processing | [radarsimx.com](https://radarsimx.com/2018/10/11/fmcw-radar/) |
| [waveform_pulsed_radar](notebooks/waveform_pulsed_radar.ipynb) | Pulsed Radar: Range Measurement with Matched Filtering | [radarsimx.com](https://radarsimx.com/2024/09/13/pulsed-radar/) |
| [waveform_pulsed_radar_range_ambiguous](notebooks/waveform_pulsed_radar_range_ambiguous.ipynb) | Pulsed Radar: Range Ambiguity | — |
| [waveform_pulse_doppler](notebooks/waveform_pulse_doppler.ipynb) | Pulse-Doppler Radar: Long-Range Detection with Doppler Processing | — |
| [waveform_doppler_radar](notebooks/waveform_doppler_radar.ipynb) | Doppler Radar: Continuous Wave Velocity Measurement | [radarsimx.com](https://radarsimx.com/2019/05/16/doppler-radar/) |
| [waveform_pmcw_radar](notebooks/waveform_pmcw_radar.ipynb) | PMCW Radar: Phase-Modulated Continuous Wave | [radarsimx.com](https://radarsimx.com/2019/05/24/pmcw-radar/) |
| [waveform_ofdm_radar](notebooks/waveform_ofdm_radar.ipynb) | OFDM Radar: Orthogonal Frequency Division Multiplexing | [radarsimx.com](https://radarsimx.com/2026/09/14/ofdm-radar/) |
| [waveform_otfs_radar](notebooks/waveform_otfs_radar.ipynb) | OTFS Radar: Orthogonal Time Frequency Space | — |
| [waveform_interferometric_radar](notebooks/waveform_interferometric_radar.ipynb) | Interferometric Radar: Phase-Based Motion Detection | [radarsimx.com](https://radarsimx.com/2023/08/31/interferometric-radar/) |

### MIMO & Array Processing

Multi-channel radars, virtual arrays, and direction-of-arrival estimation.

| Notebook | Title | Post |
|---|---|---|
| [mimo_tdm_fmcw_radar](notebooks/mimo_tdm_fmcw_radar.ipynb) | TDM MIMO FMCW Radar: Virtual Array Beamforming | [radarsimx.com](https://radarsimx.com/2019/04/07/tdm-mimo-fmcw-radar/) |
| [mimo_fmcw_doa](notebooks/mimo_fmcw_doa.ipynb) | Direction of Arrival (DoA) Estimation with FMCW Radar | [radarsimx.com](https://radarsimx.com/2022/12/12/doa-estimation/) |

### Radar Imaging (SAR & MIMO)

Forming radar images with synthetic apertures and MIMO arrays.

| Notebook | Title | Post |
|---|---|---|
| [imaging_pulse_sar](notebooks/imaging_pulse_sar.ipynb) | Pulse Radar SAR Imaging: Strip-Map SAR via Back-Projection | [radarsimx.com](https://radarsimx.com/2026/06/30/pulse-radar-sar-imaging/) |
| [imaging_sar_parking_lot](notebooks/imaging_sar_parking_lot.ipynb) | SAR Survey of a Parking Lot | [radarsimx.com](https://radarsimx.com/2026/07/22/sar-survey-of-a-parking-lot/) |
| [imaging_mimo_fmcw](notebooks/imaging_mimo_fmcw.ipynb) | MIMO Imaging Radar | [radarsimx.com](https://radarsimx.com/2022/12/02/imaging-radar/) |

### 3D Scenes & Ray Tracing

Ray-traced mesh targets, moving platforms, and propagation effects.

| Notebook | Title | Post |
|---|---|---|
| [scene_fmcw_car](notebooks/scene_fmcw_car.ipynb) | FMCW Automotive Radar: Vehicle Detection and Tracking | [radarsimx.com](https://radarsimx.com/2021/05/10/fmcw-radar-with-a-car/) |
| [scene_fmcw_plate](notebooks/scene_fmcw_plate.ipynb) | FMCW Radar RCS Measurement: Rotating Flat Plate | [radarsimx.com](https://radarsimx.com/2021/05/10/fmcw-radar-with-a-plate/) |
| [scene_fmcw_corner_reflector](notebooks/scene_fmcw_corner_reflector.ipynb) | FMCW Radar with Corner Reflector and CFAR Detection | [radarsimx.com](https://radarsimx.com/2021/05/10/fmcw-radar-with-a-corner-reflector/) |
| [scene_doppler_turbine](notebooks/scene_doppler_turbine.ipynb) | Doppler Signature of a Rotating Wind Turbine | [radarsimx.com](https://radarsimx.com/2021/05/10/doppler-of-a-turbine/) |
| [scene_micro_doppler](notebooks/scene_micro_doppler.ipynb) | Micro-Doppler Signatures: Rotating Turbine | [radarsimx.com](https://radarsimx.com/2021/05/10/micro-doppler/) |
| [scene_multi_path](notebooks/scene_multi_path.ipynb) | Multipath Effect in Radar: Ground Reflection Analysis | [radarsimx.com](https://radarsimx.com/2021/05/10/multi-path-effect/) |
| [scene_mounting_heights](notebooks/scene_mounting_heights.ipynb) | Vertical Multipath Effect at Different Mounting Heights | — |
| [scene_radar_motion_plan](notebooks/scene_radar_motion_plan.ipynb) | FMCW Radar with Motion Planning | [radarsimx.com](https://radarsimx.com/2025/11/20/fmcw-radar-with-motion-planning/) |
| [scene_pulse_radar_altimeter](notebooks/scene_pulse_radar_altimeter.ipynb) | Pulse Radar Altimeter: Altitude Measurement over Terrain | [radarsimx.com](https://radarsimx.com/2025/11/21/pulse-radar-altimeter-altitude/) |
| [scene_state_visualization](notebooks/scene_state_visualization.ipynb) | Scene State Visualization and Retrieval | — |

### Radar Cross Section (RCS)

Monostatic, bistatic, and polarimetric RCS of mesh targets.

| Notebook | Title | Post |
|---|---|---|
| [rcs_car](notebooks/rcs_car.ipynb) | Radar Cross Section (RCS) of a Car | [radarsimx.com](https://radarsimx.com/2021/05/10/car-rcs/) |
| [rcs_plate](notebooks/rcs_plate.ipynb) | Radar Cross Section (RCS) of a 5 m × 5 m Flat Plate | [radarsimx.com](https://radarsimx.com/2021/05/10/plate-rcs/) |
| [rcs_corner_reflector](notebooks/rcs_corner_reflector.ipynb) | Radar Cross Section (RCS) of a Corner Reflector | [radarsimx.com](https://radarsimx.com/2021/05/10/corner-reflector-rcs/) |
| [rcs_polarization](notebooks/rcs_polarization.ipynb) | RCS Polarimetry: Co-Pol vs. Cross-Pol | [radarsimx.com](https://radarsimx.com/2024/04/19/cross-polarization-and-co-polarization-rcs/) |

### Detection & Link Budget

Detection theory, CFAR, and end-to-end SNR analysis.

| Notebook | Title | Post |
|---|---|---|
| [detection_cfar](notebooks/detection_cfar.ipynb) | CFAR Detection | [radarsimx.com](https://radarsimx.com/2021/01/10/cfar/) |
| [detection_roc](notebooks/detection_roc.ipynb) | Receiver Operating Characteristic (ROC) Analysis | [radarsimx.com](https://radarsimx.com/2019/10/06/receiver-operating-characteristic/) |
| [detection_link_budget_point_target](notebooks/detection_link_budget_point_target.ipynb) | FMCW Radar Link Budget Analysis (Point Target) | [radarsimx.com](https://radarsimx.com/2024/10/11/fmcw-radar-link-budget-point-target/) |
| [detection_link_budget_mesh_target](notebooks/detection_link_budget_mesh_target.ipynb) | FMCW Radar Link Budget Analysis (Mesh Target) | [radarsimx.com](https://radarsimx.com/2025/06/05/fmcw-radar-link-budget-mesh-target/) |

### Impairments & Interference

Hardware non-idealities and mutual interference.

| Notebook | Title | Post |
|---|---|---|
| [impairment_phase_noise](notebooks/impairment_phase_noise.ipynb) | Phase Noise Simulation | [radarsimx.com](https://radarsimx.com/2021/01/13/phase-noise/) |
| [impairment_non_linear_chirp](notebooks/impairment_non_linear_chirp.ipynb) | Chirp Non-Linearity in FMCW Radar: Impact on Performance | [radarsimx.com](https://radarsimx.com/2021/05/10/arbitrary-waveform/) |
| [impairment_fmcw_interference](notebooks/impairment_fmcw_interference.ipynb) | FMCW Radar Mutual Interference: Victim and Interferer Analysis | [radarsimx.com](https://radarsimx.com/2023/01/13/interference/) |

### LiDAR Simulation

Ray-traced LiDAR point clouds.

| Notebook | Title | Post |
|---|---|---|
| [lidar_point_cloud](notebooks/lidar_point_cloud.ipynb) | Lidar Point Cloud Simulation with RadarSimPy | [radarsimx.com](https://radarsimx.com/2020/02/05/lidar-point-cloud/) |

<!-- index:end -->

## Exporting to HTML

Pre-built HTML versions of the notebooks, used for the website posts, are in the [`html/`](html/) folder. To regenerate them:

```sh
python scripts/export_html.py                     # all notebooks
python scripts/export_html.py imaging_pulse_sar   # one notebook (names or globs, e.g. "rcs_*")
python scripts/export_html.py --changed           # only notebooks newer than their HTML
```

The `export_html.bat` (Windows) and `export_html.sh` (Linux/macOS) wrappers run the same script and pass all arguments through, e.g. `export_html.bat --changed`. `build_index.bat` and `build_index.sh` do the same for `scripts/build_index.py`.

## Adding or recategorizing a notebook

1. Name the notebook `<category>_<name>.ipynb` and put it in `notebooks/`.
2. Add an entry to [`catalog.yml`](catalog.yml) with its category, title, and website post URL (`null` if unpublished).
3. Run `python scripts/build_index.py` to regenerate the table above. `--check` validates the catalog without writing.
