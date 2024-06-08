import matplotlib.pyplot as plt
from scipy.io import wavfile

# Path to your .wav file
wav_file_path = '/Users/ca/API/pythonProject/audioBot1/file.wav'

# Read the .wav file
sample_rate, data = wavfile.read(wav_file_path)

# Create time axis in seconds
time = [i / sample_rate for i in range(len(data))]

# Plotting the waveform
plt.figure(figsize=(12, 6))
plt.plot(time, data)
plt.title("Waveform Plot")
plt.ylabel("Amplitude")
plt.xlabel("Time [s]")
plt.show()

