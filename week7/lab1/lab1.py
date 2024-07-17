import numpy as np
from scipy.io.wavfile import write

# Samples per second (standard for CD quality audio)
samples_s = 44100

# Define the frequencies of the sine waves in Hertz
frequencies = [60.0, 200.0]  # Example frequencies

# Duration of each note in seconds
duration_s = 3.0

# Generate an array of sample indices for the duration of one note
sample_nums = np.arange(duration_s * samples_s)

# Initialize an empty array to hold the complete waveform
complete_waveform = np.array([])

# Loop through each frequency
for freq_hz in frequencies:
    # Create the waveform for the current frequency
    waveform = np.sin(2 * np.pi * sample_nums * freq_hz / samples_s)
    
    # Reduce the amplitude of the waveform to prevent clipping
    waveform_quiet = waveform * 0.3
    
    # Append the current waveform to the complete waveform
    complete_waveform = np.concatenate((complete_waveform, waveform_quiet))

# Convert the complete waveform to 16-bit integers for WAV file format
waveform_integers = np.int16(complete_waveform * 32767)

# Write the complete waveform to a single WAV file
write('my_song_sequential.wav', samples_s, waveform_integers)

print('Saved: my_song_sequential.wav')
