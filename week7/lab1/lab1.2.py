import sys
from PySide6.QtWidgets import (QWidget, QApplication, QLabel, QVBoxLayout, QDial, QPushButton)
from PySide6.QtCore import Slot
import numpy as np
from scipy.io.wavfile import write

app = QApplication([])

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        
        self.dial = QDial()
        self.dial.setRange(0, 100)
        self.dial.setValue(0)
        self.dial.valueChanged.connect(self.on_dial_value_changed)
        
        self.label = QLabel("Dial Value: 0")
        self.button = QPushButton('Create Frequency')
        self.button.clicked.connect(self.create_freq)
        
        layout.addWidget(self.dial)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        self.resize(500, 500)

    @Slot()
    def on_dial_value_changed(self, value):
        self.label.setText(f"Dial Value: {value}")
        
    @Slot()
    def create_freq(self):
        print("button")
        dial_value = self.dial.value()
        # Samples per second (standard for CD quality audio)
        samples_s = 44100

        # Define the frequencies of the sine waves in Hertz
        frequencies = dial_value  # Example frequencies

        # Duration of each note in seconds
        duration_s = 3.0

        # Generate an array of sample indices for the duration of one note
        sample_nums = np.arange(duration_s * samples_s)

        # Initialize an empty array to hold the complete waveform
        complete_waveform = np.array([])

        # Loop through each frequency

        # Create the waveform for the current frequency
        waveform = np.sin(2 * np.pi * sample_nums * dial_value / samples_s)

        # Reduce the amplitude of the waveform to prevent clipping
        waveform_quiet = waveform * 0.3

        # Append the current waveform to the complete waveform
        complete_waveform = np.concatenate((complete_waveform, waveform_quiet))

        # Convert the complete waveform to 16-bit integers for WAV file format
        waveform_integers = np.int16(complete_waveform * 32767)

        # Write the complete waveform to a single WAV file
        write('gui_created_freq.wav', samples_s, waveform_integers)

        print('Saved: gui_created_freq.wav')

my_win = MyWindow()
my_win.show()
sys.exit(app.exec())
