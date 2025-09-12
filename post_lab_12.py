# --------------------------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# (a) Two sine waves added together
fs = 1000  # Sampling frequency
t = np.linspace(0, 1, fs, endpoint=False)  # 1 second duration
sine_5 = np.sin(2 * np.pi * 5 * t)   # 5 Hz sine
sine_10 = np.sin(2 * np.pi * 10 * t) # 10 Hz sine
sum_signal = sine_5 + sine_10

plt.figure(figsize=(10,4))
plt.plot(t, sum_signal, label="5Hz + 10Hz Sine")
plt.title("(a) Addition of 5Hz and 10Hz Sine Waves")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)


# (b) Multiply sine and cosine
fs = 500
t = np.linspace(0, 2, 2*fs, endpoint=False)  # 2 sec
sine_5 = np.sin(2 * np.pi * 5 * t)
cosine_10 = np.cos(2 * np.pi * 10 * t)
mult_signal = sine_5 * cosine_10

plt.figure(figsize=(10,4))
plt.plot(t, mult_signal, label="5Hz Sine × 10Hz Cosine")
plt.title("(b) Multiplication of 5Hz Sine and 10Hz Cosine")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# (c) Time-shifted sine
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
sine_5 = np.sin(2 * np.pi * 5 * t)
shift = 0.1  # 0.1s shift
sine_shifted = np.sin(2 * np.pi * 5 * (t - shift))

plt.figure(figsize=(10,4))
plt.plot(t, sine_5, label="Original 5Hz Sine")
plt.plot(t, sine_shifted, label="Shifted by 0.1s")
plt.title("(c) Time Shifted 5Hz Sine")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

# (d) Amplitude scaling
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
sine_10 = np.sin(2 * np.pi * 10 * t)
scaled_sine = 3 * sine_10

plt.figure(figsize=(10,4))
plt.plot(t, sine_10, label="Original 10Hz Sine")
plt.plot(t, scaled_sine, label="Scaled by 3")
plt.title("(d) Amplitude Scaling of 10Hz Sine")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)


# (e) Time reversal
fs = 1000
t = np.linspace(0, 1, fs, endpoint=False)
sine_5 = np.sin(2 * np.pi * 5 * t)
sine_reversed = sine_5[::-1]  # Reverse array

plt.figure(figsize=(10,4))
plt.plot(t, sine_5, label="Original 5Hz Sine")
plt.plot(t, sine_reversed, label="Time-Reversed 5Hz Sine")
plt.title("(e) Time Reversal of 5Hz Sine")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)

plt.show()

