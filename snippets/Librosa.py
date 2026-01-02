"""
LIBROSA — Music and Audio Analysis in Python
Comprehensive Snippets for Learning & Test Prep
"""

import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

# =====================================================================
# 1. Loading and Basic I/O
# =====================================================================

# Load an audio file (returns audio as a NumPy array and the sample rate)
# By default, librosa resamples to 22050 Hz and converts to mono
y, sr = librosa.load("audio.wav")

# Load with specific sample rate (sr=None preserves native rate)
y, sr = librosa.load("audio.wav", sr=44100)

# Load only a segment (first 5 seconds)
y, sr = librosa.load("audio.wav", duration=5.0)

# Get duration in seconds
duration = librosa.get_duration(y=y, sr=sr)

# =====================================================================
# 2. Visualizations
# =====================================================================

# Waveform plot
plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")

# Spectrogram (STFT -> Power -> dB)
D = librosa.stft(y)                 # Short-time Fourier Transform
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

plt.figure(figsize=(10, 4))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title("Spectrogram (Log Frequency)")

# =====================================================================
# 3. Feature Extraction (Core for MIR)
# =====================================================================

# MFCCs (Mel-frequency cepstral coefficients)
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# Chromagram (Pitch classes: C, C#, D...)
chroma = librosa.feature.chroma_stft(y=y, sr=sr)

# Spectral Centroid (Indicates where the "center of mass" of spectrum is)
cent = librosa.feature.spectral_centroid(y=y, sr=sr)

# Zero Crossing Rate (Measure of noisiness)
zcr = librosa.feature.zero_crossing_rate(y)

# Mel-scaled Spectrogram
melspec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
melspec_db = librosa.power_to_db(melspec, ref=np.max)

# =====================================================================
# 4. Rhythmic Analysis
# =====================================================================

# Beat tracking (Estimate tempo and detected beat events)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print(f"Estimated Tempo: {tempo:.2f} BPM")

# Convert beat frames to time stamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Onset detection (Picking out the starts of notes/events)
onsets = librosa.onset.onset_detect(y=y, sr=sr, units='time')

# =====================================================================
# 5. Audio Effects & Manipulation
# =====================================================================

# Time Stretching (Change speed without changing pitch)
# rate > 1.0 is faster, rate < 1.0 is slower
y_fast = librosa.effects.time_stretch(y, rate=1.5)

# Pitch Shifting (Change pitch without changing speed)
# n_steps is in semitones
y_shifted = librosa.effects.pitch_shift(y, sr=sr, n_steps=4)

# Harmonic-Percussive Separation
# Separates melody/instruments from drums/rhythm
y_harmonic, y_percussive = librosa.effects.hpss(y)

# =====================================================================
# 6. Conversions & Utilities
# =====================================================================

# Frequency to Note Name
note = librosa.hz_to_note(440.0)      # 'A4'

# Note Name to Frequency
freq = librosa.note_to_hz('C#5')      # 554.37

# Time to Samples
samples = librosa.time_to_samples(1.5, sr=sr)

# Frames to Time
times = librosa.frames_to_time(np.arange(10), sr=sr)

# =====================================================================
# 7. ADVANCED: Spectrogram Parameters
# =====================================================================

# Controlling the window/hop size (crucial for time/freq resolution)
# n_fft: Window size
# hop_length: Distance between windows (stride)
D_custom = librosa.stft(y, n_fft=2048, hop_length=512)

# Normalizing audio
y_norm = librosa.util.normalize(y)