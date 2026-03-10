# RadarSimNb

<img src="https://raw.githubusercontent.com/radarsimx/.github/refs/heads/main/profile/radarsimnb.svg" alt="logo" width="200"/>

`RadarSimNb` is a collection of Jupyter Notebooks providing hands-on examples for [`RadarSimPy`](https://radarsimx.com) — a Python radar simulation library with a C++ back-end. The notebooks cover the full simulation workflow: waveform design, scene simulation, RCS computation, signal processing, and system characterization. Explore the [online examples](https://radarsimx.com/category/examples/) to dive in.

## Notebooks

### Waveform Design

| Notebook | Description |
|---|---|
| [waveform_fmcw_radar](notebooks/waveform_fmcw_radar.ipynb) | FMCW radar range-Doppler processing |
| [waveform_pulsed_radar](notebooks/waveform_pulsed_radar.ipynb) | Pulsed radar fundamentals |
| [waveform_pulsed_radar_range_ambiguous](notebooks/waveform_pulsed_radar_range_ambiguous.ipynb) | Range-ambiguous pulsed radar |
| [waveform_pulse_doppler](notebooks/waveform_pulse_doppler.ipynb) | Pulse Doppler waveform |
| [waveform_pmcw_radar](notebooks/waveform_pmcw_radar.ipynb) | Phase-modulated CW (PMCW) radar |
| [waveform_tdm_mimo_fmcw_radar](notebooks/waveform_tdm_mimo_fmcw_radar.ipynb) | TDM-MIMO FMCW radar |
| [waveform_doppler_radar](notebooks/waveform_doppler_radar.ipynb) | Continuous-wave Doppler radar |
| [waveform_interferometric_radar](notebooks/waveform_interferometric_radar.ipynb) | Interferometric radar |
| [waveform_non_linear_chirp](notebooks/waveform_non_linear_chirp.ipynb) | Non-linear chirp waveform |
| [waveform_fmcw_interference](notebooks/waveform_fmcw_interference.ipynb) | FMCW inter-radar interference |
| [waveform_sfmcw_radar](notebooks/waveform_sfmcw_radar.ipynb) | Stepped FMCW (SFMCW) radar |

### Scene Simulation

| Notebook | Description |
|---|---|
| [scene_fmcw_car](notebooks/scene_fmcw_car.ipynb) | Automotive FMCW car detection |
| [scene_fmcw_corner_reflector](notebooks/scene_fmcw_corner_reflector.ipynb) | FMCW with a corner reflector target |
| [scene_fmcw_imaging_radar](notebooks/scene_fmcw_imaging_radar.ipynb) | FMCW imaging radar |
| [scene_fmcw_plate](notebooks/scene_fmcw_plate.ipynb) | FMCW with a flat plate target |
| [scene_doppler_turbine](notebooks/scene_doppler_turbine.ipynb) | Doppler signature of a rotating turbine |
| [scene_micro_doppler](notebooks/scene_micro_doppler.ipynb) | Micro-Doppler effects |
| [scene_multi_path](notebooks/scene_multi_path.ipynb) | Multi-path propagation effects |
| [scene_mounting_heights](notebooks/scene_mounting_heights.ipynb) | Radar mounting height effects |
| [scene_pulse_radar_altimeter](notebooks/scene_pulse_radar_altimeter.ipynb) | Pulsed radar altimeter |
| [scene_radar_motion_plan](notebooks/scene_radar_motion_plan.ipynb) | Radar with motion planning |

### Radar Cross Section (RCS)

| Notebook | Description |
|---|---|
| [rcs_corner_reflector](notebooks/rcs_corner_reflector.ipynb) | RCS of a trihedral corner reflector |
| [rcs_car](notebooks/rcs_car.ipynb) | RCS of a vehicle mesh model |
| [rcs_plate](notebooks/rcs_plate.ipynb) | RCS of a flat plate |
| [rcs_polarization](notebooks/rcs_polarization.ipynb) | Polarization effects on RCS |

### Signal Processing

| Notebook | Description |
|---|---|
| [processing_cfar](notebooks/processing_cfar.ipynb) | CA-CFAR and OS-CFAR detection |
| [processing_fmcw_doa](notebooks/processing_fmcw_doa.ipynb) | Direction of arrival (DOA) estimation |

### System Characterization

| Notebook | Description |
|---|---|
| [characterization_roc](notebooks/characterization_roc.ipynb) | ROC curves and Swerling target models |
| [characterization_link_budget_point_target](notebooks/characterization_link_budget_point_target.ipynb) | Link budget for point targets |
| [characterization_link_budget_mesh_target](notebooks/characterization_link_budget_mesh_target.ipynb) | Link budget for 3D mesh targets |
| [characterization_phase_noise](notebooks/characterization_phase_noise.ipynb) | Phase noise characterization |

### Other

| Notebook | Description |
|---|---|
| [lidar](notebooks/lidar.ipynb) | Lidar point cloud simulation |
| [ground_speed_example](notebooks/ground_speed_example.ipynb) | Ground speed measurement |

## Exporting to HTML

Pre-built HTML versions of all notebooks are available in the [`html/`](html/) folder. To regenerate them locally, run the provided export script:

**Windows:**
```bat
export_html.bat
```

**Linux / macOS:**
```sh
./export_html.sh
```
