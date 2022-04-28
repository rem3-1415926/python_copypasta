import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

FILE = "output voltages.csv"

str_data = np.loadtxt(FILE, dtype=str, delimiter= ',')
data = str_data[2:].astype(float)
t = data[:,0]
a = data[:,1]
b = data[:,2]
c = data[:,3]

fig, ax = plt.subplots(tight_layout=True, figsize=(21,7))
ax.plot(t, a, alpha=1)
ax.plot(t, b, alpha=0.7)
ax.plot(t, c, alpha=0.5)
ax.set_ylabel("V / V")
ax.set_xlabel("t / ms")

fs = len(t)/(t[-1]-t[0]) * 1e3
print(f"{fs/1e6:.2f}MSa/s")


# -----------------------------------------------------------------------------
# frequency analysis A

t_ = t[12000:22000]
meas = b[12000:22000]
fft = np.fft.fft(meas)[:500]
fft[0] = 0
freq = np.arange(len(t_))/(t_[-1]-t_[0]) * 1e3
freq = freq[:500]

max_idx = list(abs(fft)).index(max(abs(fft)))

fig, ax = plt.subplots(tight_layout=True, figsize=(18,6))
ax.set_title("FFT of switching interval")
ax.plot(freq / 1e3, abs(fft))
ax.plot(freq[max_idx]/1e3, abs(fft[max_idx]), marker="x", markersize=10, c="k")
ax.text(freq[max_idx]/1e3, abs(fft[max_idx]), f" {freq[max_idx]/1e3:.1f}kHz", fontsize=16)
ax.set_xlabel("freq / kHz")
# fig, ax = plt.subplots()
# ax.plot(t_, meas)


# -----------------------------------------------------------------------------
# measuring period analysis A

t_ = t[5340:10910]
meas = b[5340:10910]
but = signal.butter(4, 600e3, 'low', False, 'sos', fs)
meas = signal.sosfilt(but, meas)

x = np.arange(len(meas))
m, c = np.polyfit(x, meas, 1)
linear = x*m + c

diff = meas - linear

fig, ax = plt.subplots()
# ax.plot(t_, meas)
# ax.plot(t_, linear)
# ax.plot(t_, diff)
ax.plot(meas)
ax.plot(linear)
ax.plot(diff)
ax.plot()
ax.grid()
plt.show()