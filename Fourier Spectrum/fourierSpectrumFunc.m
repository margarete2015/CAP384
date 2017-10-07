'this function produces a fourier power spectrum and also returns
two vectors (Frequency and Energy)
Inputs are two vectors: Function and Time'
function [freq, energy] = fourierSpectrum (f, t)

	subplot(2, 1, 1)
	plot(t,f)

	'FT calc'
	fhat = fft(f);
	'shifting fhat'
	fhatshift = fftshift(fhat)/N;

	'energy calc'
	energy = (abs(fhatshift).^2);


	'frequency calc'
	k = linspace(-(N/2), N/2-1, N);
	freq = (k*2*pi)/N;



	'power spectrum visualization'
	fImg = imag(f);
	checkImg = find(abs(fImg) < eps);

	if(!(length(checkImg) != 0))
	  subplot(2, 1, 2)
	  plot(freq, energia) 
	  title ("Fourier Power Spectrum");
	  xlabel ("Frequency");
	  ylabel ("Energy");
	else
	subplot(2, 1, 2)
	  plot(freq(N/2+1:N), energia(N/2+1:N)) 
	  title ("Fourier Power Spectrum");
	  xlabel ("Frequency");
	  ylabel ("Energy");
	endif


endfunction;