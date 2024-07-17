import numpy as np
from scipy.io.wavfile import write

samples_s = 44100

frequencies = [45, 320, 390]  # C major chord: C4, E4, G4

duration_s = 5.0

sample_nums = np.arange(duration_s * samples_s)

chord_waveform = np.zeros_like(sample_nums, dtype=float)

for freq_hz in frequencies:
    waveform = np.sin(2 * np.pi * sample_nums * freq_hz / samples_s)
    chord_waveform += waveform

chord_waveform /= len(frequencies)

chord_waveform_quiet = chord_waveform * 0.3

waveform_integers = np.int16(chord_waveform_quiet * 32767)

write('chord.wav', samples_s, waveform_integers)

print('Saved: my_chord.wav')
