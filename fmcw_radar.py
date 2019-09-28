# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
#  # FMCW Radar
# 
#  This is a basic FMCW radar simulation example based on `RadarSimPy`.
# 
#  >`RadarSimPy` is a radar simulation package built with python. **[Contact me](https://zpeng.me/#contact) if you are interested in this module.**
# 
#  This notebook is available on my [GitHub](https://github.com/rookiepeng/fmcw-radar-simulation).
# 
# 
#  ## Radar Model
#  ### Transmitter
# 
#  The following table lists the basic parameters of the radar transmitter.
# 
#  | Parameter                       | Variable in `RadarSimPy` | Value      |
#  |---------------------------------|--------------------------|------------|
#  | Center frequency ($f_c$)        | fc                       | 24.125 GHz |
#  | Bandwidth ($B$)                 | bandwidth                | 100 MHz    |
#  | Transmitted power ($P_t$)       | tx_power                 | 10 dBm     |
#  | Rising or falling chirp         | slop_type                | rising     |
#  | Chirp repetition period ($CRP$) | repetition_period        | 100 us     |
#  | Chirp length ($T$)              | pulse_length             | 80 us      |
#  | Number of chirps                | pulses                   | 256        |
#  | Chirp start delay               | delay                    | 0 s        |
# 
#  The radiation pattern os the transmitter antenna is $\cos{\theta}$. The gain of the antenna is 6 dB.
# 

#%%
import numpy as np
from radarsimpy import Radar, Transmitter, Receiver

angle = np.arange(-90, 91, 1)
pattern = 20 * np.log10(np.cos(angle / 180 * np.pi) + 0.01) + 6

tx_channel = dict(
    location=(0, 0, 0),
    azimuth_angle=angle,
    azimuth_pattern=pattern,
    elevation_angle=angle,
    elevation_pattern=pattern,
)

tx = Transmitter(fc=24.125e9,
                 pulse_length=80e-6,
                 bandwidth=100e6,
                 tx_power=10,
                 slop_type='rising',
                 repetition_period=100e-6,
                 pulses=256,
                 channels=[tx_channel])

#%% [markdown]
#  ### Receiver
#  The parameters of the receiver are listed in the table below.
# 
#  | Parameter                        | Variable in `RadarSimPy` | Value        |
#  |----------------------------------|--------------------------|--------------|
#  | Sampling rate ($f_s$)            | fs                       | 2 Msps       |
#  | Noise figure ($NF$)              | noise_figure             | 12 dB        |
#  | RF gain/loss ($G_{rf}$)          | rf_gain                  | 20 dB        |
#  | Load resistor ($R_L$)            | load_resistor            | 500 $\Omega$ |
#  | Baseband voltage gain ($G_{BB}$) | baseband_gain            | 30 dB        |
# 
#  The radiation pattern os the receiver antenna is $\cos{\theta}$. The gain of the antenna is 6 dB.

#%%
rx_channel = dict(
    location=(0, 0, 0),
    azimuth_angle=angle,
    azimuth_pattern=pattern,
    elevation_angle=angle,
    elevation_pattern=pattern,
)

rx = Receiver(fs=2e6,
              noise_figure=12,
              rf_gain=20,
              load_resistor=500,
              baseband_gain=30,
              channels=[rx_channel])

#%% [markdown]
#  Create the FMCW radar model based on all the parameters defined above.

#%%
radar = Radar(transmitter=tx, receiver=rx, type='FMCW')

#%% [markdown]
#  Calculate the characteristics of the FMCW radar:
# 
#  - Maximum range (*with I/Q baseband*): $$R_{max}=\frac{c f_s T}{2B}$$
# 
#  - Maximum range (*without I/Q baseband*): $$R_{max}=\frac{c f_s T}{4B}$$
# 
#  - Unambiguous velocity: $$v_{ua}=\frac{c}{2 CRP \times f_c}$$ or $$v_{ua}=\pm \frac{c}{4 CRP \times f_c}$$
# 
#  - Range resolution: $$\delta_r=\frac{c}{2B}$$
# 

#%%
print('Maximum range: ', radar.max_range, ' m')
print('Maximum unambiguous speed: ', radar.unambiguous_speed, ' m/s')
print('Range_resolution: ', radar.range_resolution, ' m')

#%% [markdown]
#  ### Targets
#  The propertities of targets are defined here. There are 3 targets in this simulation. The locations of the targets are defined through $(x, y, z)$ coordinates in meters, and the speeds of the targets are defined trough $(v_x, v_y, v_z)$ in $m/s$. The propertites of the targets also includes radar cross-section (RCS (dBsm)) and phase (radian).

#%%
target_1 = dict(location=(0, 200, 0), speed=(0, -5, 0), rcs=20, phase=0)
target_2 = dict(location=(20, 95, 0), speed=(0, -50, 0), rcs=15, phase=0)
target_3 = dict(location=(-5, 30, 0), speed=(0, -22, 0), rcs=5, phase=0)

targets = [target_1, target_2, target_3]


#%%
import plotly.graph_objs as go

rx_locations = radar.receiver.locations
tx_locations = radar.transmitter.locations

rx_axis = go.Scatter3d(
    x=rx_locations[:, 0],
    y=rx_locations[:, 1],
    z=rx_locations[:, 2],
    mode='markers',
    name='Receiver',
    marker=dict(color='rgb(17, 157, 255)',
                size=8,
                opacity=0.8,
                symbol='square'),
)

tx_axis = go.Scatter3d(
    x=tx_locations[:, 0],
    y=tx_locations[:, 1],
    z=tx_locations[:, 2],
    mode='markers',
    name='Transmitter',
    marker=dict(color='rgb(233, 30, 99)', size=8, opacity=0.8,
                symbol='square'),
)

data = [rx_axis, tx_axis]

for target_idx, target in enumerate(targets):
    target_loc = go.Scatter3d(
        x=[target['location'][0]],
        y=[target['location'][1]],
        z=[target['location'][2]],
        mode='markers',
        name='Target ' + str(target_idx),
        marker=dict(size=6, opacity=0.8),
    )
    data = data + [target_loc]

camera = dict(
    up=dict(x=0, y=0, z=1),
    center=dict(x=0, y=0, z=0),
    eye=dict(x=0, y=-1.5, z=1.8),
)

layout = go.Layout(
    title='Radar Scene',
    scene=dict(xaxis=dict(title='X (m)'),
               yaxis=dict(title='Y (m)'),
               zaxis=dict(title='Z (m)'),
               camera=camera,
               aspectmode='cube'),
    margin=dict(l=0, r=0, b=120, t=120),
    height=800,
)
fig = go.Figure(data=data, layout=layout)
fig.show()

#%% [markdown]
#  ## Simulate Baseband Signals
#%% [markdown]
#  Calculate baseband signal matrix:
#  $$[channel, slow~time, fast~time]$$

#%%
import radarsimpy.simulator as sim

data = sim.run_simulator(radar, targets)
timestamp = data['timestamp']
baseband = data['baseband']


#%%
data = []
for idx in range(0, 10):
    chirp = go.Scatter(
        x=timestamp[0, idx, :] * 1e6,
        y=np.linspace(
            radar.transmitter.fc - radar.transmitter.bandwidth / 2,
            radar.transmitter.fc + radar.transmitter.bandwidth / 2,
            radar.samples_per_pulse,
            endpoint=False,
        ) / 1e9,
        name='Chirp ' + str(idx),
    )
    data = data + [chirp]

layout = go.Layout(
    title='Transmitter chirps',
    yaxis=dict(tickformat='.2f', title='Frequency (GHz)'),
    xaxis=dict(tickformat='.2f', title='Time (µs)'),
)

fig = go.Figure(data, layout=layout)
fig.show()


#%%
beat_I = go.Scatter(
    x=timestamp[0, 0, :] * 1e6,
    y=np.real(baseband[0, 0, :]),
    name='I',
)
beat_Q = go.Scatter(
    x=timestamp[0, 0, :] * 1e6,
    y=np.imag(baseband[0, 0, :]),
    name='Q',
)
data = [beat_I, beat_Q]

layout = go.Layout(
    title='I/Q Beat Signals for the First Chirp',
    yaxis=dict(tickformat='.2f', title='Amplitude (V)'),
    xaxis=dict(tickformat='.2f', title='Time (µs)'),
)

fig = go.Figure(data, layout=layout)
fig.show()

#%% [markdown]
#  ## Radar Signal Processing
#  ### Range profile

#%%
from scipy import signal
import radarsimpy.processing as proc

range_window = signal.chebwin(radar.samples_per_pulse, at=60)
range_profile = proc.cal_range_profile(radar, baseband, range_window)


#%%
temp = np.abs(range_profile[0, :, :])
temp = 20 * np.log10(temp + 0.001)

range_axis = np.linspace(
    0, radar.max_range, radar.samples_per_pulse, endpoint=False)

doppler_axis = np.linspace(
    0, radar.transmitter.pulses, radar.transmitter.pulses, endpoint=False)

data = [go.Surface(x=range_axis, y=doppler_axis, z=temp, colorscale='Rainbow')]

layout = go.Layout(
    title='Range Profile',
    height=800,
    scene=dict(
        xaxis=dict(title='Range (m)'),
        yaxis=dict(title='Chirp'),
        zaxis=dict(title='Amplitude (dB)'),
        aspectmode='cube',
    ),
    margin=dict(l=0, r=0, b=60, t=100),
    legend=dict(orientation='h'),
)

fig = go.Figure(data=data, layout=layout)
fig.show()

#%% [markdown]
#  ### Range-Doppler processing

#%%
doppler_window = signal.chebwin(radar.transmitter.pulses, at=60)
range_doppler = proc.cal_range_doppler(
    radar, range_profile, doppler_window, fft_shift=False)


#%%
temp = np.abs(range_doppler[0, :, :])
temp = 20 * np.log10(temp)

range_axis = np.linspace(
    0, radar.max_range, radar.samples_per_pulse, endpoint=False)

doppler_axis = np.linspace(
    -radar.unambiguous_speed, 0, radar.transmitter.pulses, endpoint=False)

data = [go.Surface(x=range_axis, y=doppler_axis, z=temp, colorscale='Rainbow')]

layout = go.Layout(
    title='Range Doppler',
    height=800,
    scene=dict(
        xaxis=dict(title='Range (m)'),
        yaxis=dict(title='Velocity (m/s)'),
        zaxis=dict(title='Amplitude (dB)'),
        aspectmode='cube',
    ),
    margin=dict(l=0, r=0, b=60, t=100),
    legend=dict(orientation='h'),
)

fig = go.Figure(data=data, layout=layout)
fig.show()


