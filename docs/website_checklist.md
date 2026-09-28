# radarsimx.com checklist

Manual website changes that bring the Examples categories in line with [`catalog.yml`](../catalog.yml). Keep post slugs unchanged so existing URLs keep working.

## Categories

| Category | Action | Slug |
|---|---|---|
| Radar Waveforms | Rename from "Radar Systems & Waveforms" | `radar-systems-waveforms` (keep) |
| MIMO & Array Processing | Rename from "MIMO & Multi-Channel Systems" | `mimo-multi-channel-systems` (keep) |
| Radar Imaging (SAR & MIMO) | **Create** | `radar-imaging` |
| 3D Scenes & Ray Tracing | Rename from "3D Scene Simulation & Ray Tracing" | `3d-scene-simulation-ray-tracing` (keep) |
| Radar Cross Section (RCS) | Rename from "Radar Cross Section (RCS) Analysis" (optional) | `radar-cross-section-rcs-analysis` (keep) |
| Detection & Link Budget | Rename from "Signal Processing & Detection" | `signal-processing-detection` (keep) |
| Impairments & Interference | **Create** | `impairments-interference` |
| LiDAR Simulation | No change | `lidar-simulation` |
| System Performance & Characterization | **Retire** once empty; redirect to Detection & Link Budget | `system-performance-characterization` |

## Move posts

| Post | From | To |
|---|---|---|
| Pulse Radar SAR Imaging | Signal Processing & Detection | Radar Imaging |
| SAR Survey of a Parking Lot | Signal Processing & Detection | Radar Imaging |
| Imaging Radar | MIMO & Multi-Channel | Radar Imaging |
| Interference | System Performance | Impairments & Interference |
| Phase Noise | System Performance | Impairments & Interference |
| Arbitrary Waveform | Radar Systems & Waveforms | Impairments & Interference |
| Receiver Operating Characteristic | System Performance | Detection & Link Budget |
| FMCW Radar Link Budget (Point Target) | System Performance | Detection & Link Budget |
| FMCW Radar Link Budget (Mesh Target) | System Performance | Detection & Link Budget |

## Retitle posts (keep slugs)

- "Arbitrary Waveform" → "Chirp Non-Linearity in FMCW Radar" (the content is about chirp non-linearity)
- "Interference" → "FMCW Mutual Interference"
- "Imaging Radar" → "MIMO Imaging Radar"
- "LIDAR Point Cloud" → "LiDAR Point Cloud"

## Unpublished notebooks

These notebooks have no post yet (`post: null` in `catalog.yml`):

- `waveform_otfs_radar`: OTFS Radar
- `waveform_pulse_doppler`: Pulse-Doppler Radar
- `waveform_pulsed_radar_range_ambiguous`: Pulsed Radar: Range Ambiguity
- `scene_mounting_heights`: Vertical Multipath at Different Mounting Heights
- `scene_state_visualization`: Scene State Visualization

`html/waveform_sfmcw_radar.html` exists, but its source notebook was never committed. Add `notebooks/waveform_sfmcw_radar.ipynb` (and a `catalog.yml` entry) or delete the HTML.

## Notebook content backlog

- `scene_doppler_turbine` and `scene_micro_doppler` use the same turbine model and have nearly the same titles. Consider merging them into one micro-Doppler notebook (range-Doppler + STFT) and one post.
- `waveform_pulsed_radar_range_ambiguous` has no H1 title, intro, or section headings.
- `scene_state_visualization` is missing the RadarSimPy version cell and a Summary.
- `scene_mounting_heights` has only two sections, so add an introduction and an explanation of the results.

## Future notebook ideas

- MIMO & Array Processing has only 2 notebooks. Candidates: DDMA or BPM MIMO, 2D (azimuth + elevation) DoA.
- Detection & Link Budget: multi-frame tracking, or clustering after CFAR.
