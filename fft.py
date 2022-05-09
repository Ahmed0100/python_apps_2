import numpy as np
import matplotlib.pyplot as plt

time_axis = np.linspace(-2*np.pi,2*np.pi,num=1024)
sin_axis = np.sin(time_axis)
plt.plot(time_axis,sin_axis)
plt.title("Sin -Size 1024")

sin_fft=np.fft.fft(sin_axis,n=1024)
plt.figure()
plt.plot(time_axis,sin_fft)
plt.title("FFT(SIN) - Size 1024")

plt.figure()
time_axis = np.linspace(-2*np.pi,2*np.pi,num=16)
sin_axis = np.sin(time_axis)
plt.plot(time_axis,sin_axis)
plt.title("Sin - Size 16")

for x in sin_axis:
	print(x)

sin_fft=np.fft.fft(sin_axis,n=16)
plt.figure()
plt.plot(time_axis,sin_fft)
plt.title("FFT(SIN) - Size 16")

print()
for x in sin_fft:
	print(x)

plt.show()