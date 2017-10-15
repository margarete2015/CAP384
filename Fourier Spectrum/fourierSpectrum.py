import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


#Setting Plots
gs1 = gridspec.GridSpec(2, 1)
fig = plt.figure()
ax1 = fig.add_subplot(gs1[0])
ax2 = fig.add_subplot(gs1[1])

#Deffining Function
N = 256
t = np.linspace(-1, 1, N)
f = np.cos(2*np.pi*t)

#Function Visualization
ax1.plot(t, f, color='black')
ax1.set_title('Function')

#FFT
fhat = np.fft.fft(f)

#Frequency Calc
k = np.linspace(-(N/2), (N/2), N)
freqs = k/N

#FFT shift
fhatshift = np.fft.fftshift(fhat)/N

#Energy Calc
energy = np.abs(fhatshift)**2


#Max energy component
index = energy.argmax()
print("Highest Energy Component is on: ", index)

#Check if function has imaginary part
isImag = np.sum(f.imag)

#Spectrum Visualization
if(isImag):
	#Full spectrum for complex functions
	ax2.plot(freqs, energy, color='black')
	ax2.set_title('Fourier Spectrum')
else:
	#Half spectrum for real functions
	ax2.plot(freqs[int(N/2):N], energy[int(N/2):N], color='black')
	ax2.set_title('Fourier Spectrum')

gs1.tight_layout(fig)

#save Plot to eps format
plt.savefig('fourierSpectrum.eps', format='eps', dpi=1000)
#Show plot
plt.show()