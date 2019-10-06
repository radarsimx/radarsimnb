# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # Receiver Operating Characteristic (ROC)
# 
# Calculate the receiver operation characteristic in a radar.
# 
# >`RadarSimPy` is a radar simulation package built with python. **[Contact me](https://zpeng.me/#contact) if you are interested in this module.**
# 
# This notebook is available on my [GitHub](https://github.com/rookiepeng/fmcw-radar-simulation).
# 
# #### Requires
# 
# - numpy
# - scipy
# - plotly (*visualization*)
# 
# ---
# ## Calculate $P_d$ from $SNR$ and $P_{fa}$
# 
# ### Swerling 3 targets without integration

#%%
from radarsimpy import roc_pd, roc_snr
import numpy as np

snr = np.arange(-10, 30, 0.1)
pfa = np.array([1e-4, 1e-6, 1e-8])
pd = roc_pd(pfa, snr, 1, 'Swerling 3')


#%%
import plotly.graph_objs as go
it_pfa = np.nditer(pfa, flags=['f_index'])


data = []
while not it_pfa.finished:
    data.append(go.Scatter(
        x=snr, y=pd[it_pfa.index, :], name=r'$P_{fa} = '+str(it_pfa[0])+', N = 1$'))
    it_pfa.iternext()

layout = go.Layout(
    title='Swerling 3',
    yaxis=dict(title=r'$\text{Probability of detection } P_d$'),
    xaxis=dict(title=r'$\text{SNR (dB)}$'),
)
go.Figure(data=data, layout=layout)

#%% [markdown]
# ### Swerling 3 targets with 20-channel non-coherent integration

#%%
pd = roc_pd(pfa, snr, 20, 'Swerling 3')


#%%
it_pfa = np.nditer(pfa, flags=['f_index'])
data = []
while not it_pfa.finished:
    data.append(go.Scatter(
        x=snr, y=pd[it_pfa.index, :], name=r'$P_{fa} = '+str(it_pfa[0])+', N = 20$'))
    it_pfa.iternext()


layout = go.Layout(
    title='Swerling 3',
    yaxis=dict(title=r'$\text{Probability of detection } P_d$'),
    xaxis=dict(title=r'$\text{SNR (dB)}$'),
)
go.Figure(data=data, layout=layout)

#%% [markdown]
# ### Different target types

#%%
snr = np.arange(-10, 30, 0.1)
pfa = 1e-6
N = 5
pd_sw1 = roc_pd(pfa, snr, N, 'Swerling 1')
pd_sw2 = roc_pd(pfa, snr, N, 'Swerling 2')
pd_sw3 = roc_pd(pfa, snr, N, 'Swerling 3')
pd_sw4 = roc_pd(pfa, snr, N, 'Swerling 4')
pd_sw5 = roc_pd(pfa, snr, N, 'Swerling 5')
pd_coherent = roc_pd(pfa, snr, N, 'Coherent')
pd_real = roc_pd(pfa, snr, N, 'Real')


#%%
data = []
data.append(go.Scatter(x=snr, y=pd_sw1, name='Swerling 1'+', N = '+str(N)))
data.append(go.Scatter(x=snr, y=pd_sw2, name='Swerling 2'+', N = '+str(N)))
data.append(go.Scatter(x=snr, y=pd_sw3, name='Swerling 3'+', N = '+str(N)))
data.append(go.Scatter(x=snr, y=pd_sw4, name='Swerling 4'+', N = '+str(N)))
data.append(go.Scatter(x=snr, y=pd_sw5, name='Swerling 5'+', N = '+str(N)))
data.append(go.Scatter(x=snr, y=pd_coherent, name='Coherent'+', N = '+str(N)))
data.append(go.Scatter(x=snr, y=pd_real, name='Real'+', N = '+str(N)))


layout = go.Layout(
    title=r'$P_{fa} = '+str(pfa)+'$',
    yaxis=dict(title=r'$\text{Probability of detection } P_d$'),
    xaxis=dict(title=r'$\text{SNR (dB)}$'),
)
go.Figure(data=data, layout=layout)

#%% [markdown]
# ## Calculate minimal required $SNR$ from $P_d$ and $P_{fa}$

#%%
pfa = 1e-5
pd = np.arange(0.1, 0.9, 0.01)
N = 10
snr_real = roc_snr(1e-4, pd, N, 'Real')

snr_sw1 = roc_snr(pfa, pd, N, 'Swerling 1')
snr_sw2 = roc_snr(pfa, pd, N, 'Swerling 2')
snr_sw3 = roc_snr(pfa, pd, N, 'Swerling 3')
snr_sw4 = roc_snr(pfa, pd, N, 'Swerling 4')
snr_sw5 = roc_snr(pfa, pd, N, 'Swerling 5')
snr_coherent = roc_snr(pfa, pd, N, 'Coherent')
snr_real = roc_snr(pfa, pd, N, 'Real')


#%%
data = []
data.append(go.Scatter(x=pd, y=snr_sw1, name='Swerling 1'+', N = '+str(N)))
data.append(go.Scatter(x=pd, y=snr_sw2, name='Swerling 2'+', N = '+str(N)))
data.append(go.Scatter(x=pd, y=snr_sw3, name='Swerling 3'+', N = '+str(N)))
data.append(go.Scatter(x=pd, y=snr_sw4, name='Swerling 4'+', N = '+str(N)))
data.append(go.Scatter(x=pd, y=snr_sw5, name='Swerling 5'+', N = '+str(N)))
data.append(go.Scatter(x=pd, y=snr_coherent, name='Coherent'+', N = '+str(N)))
data.append(go.Scatter(x=pd, y=snr_real, name='Real'+', N = '+str(N)))


layout = go.Layout(
    title=r'$P_{fa} = '+str(pfa)+'$',
    xaxis=dict(title=r'$\text{Probability of detection } P_d$'),
    yaxis=dict(title=r'$\text{Minimal SNR (dB)}$'),
)
go.Figure(data=data, layout=layout)

#%% [markdown]
# ## Generate a look-up table

#%%
snr_sw1 = np.zeros(256)
snr_sw2 = np.zeros(256)
snr_sw3 = np.zeros(256)
snr_sw4 = np.zeros(256)
snr_sw5 = np.zeros(256)
snr_ci = np.zeros(256)
pd = 0.5
pfa = 1e-4

for N in range(1, 257):
    snr_sw1[N-1] = roc_snr(pfa, pd, N, 'Swerling 1')
    snr_sw2[N-1] = roc_snr(pfa, pd, N, 'Swerling 2')
    snr_sw3[N-1] = roc_snr(pfa, pd, N, 'Swerling 3')
    snr_sw4[N-1] = roc_snr(pfa, pd, N, 'Swerling 4')
    snr_sw5[N-1] = roc_snr(pfa, pd, N, 'Swerling 5')
    snr_ci[N-1] = roc_snr(pfa, pd, N, 'Coherent')


mat = np.zeros((256, 6))
mat[:, 0] = snr_sw1
mat[:, 1] = snr_sw2
mat[:, 2] = snr_sw3
mat[:, 3] = snr_sw4
mat[:, 4] = snr_sw5
mat[:, 5] = snr_ci

np.savetxt("snr.csv", mat, delimiter=",")


