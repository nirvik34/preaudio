import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from glob import glob
import librosa
import librosa.display
from itertools import cycle

# Set plot theme
sns.set_theme(style="whitegrid")
color_pal = plt.rcParams['axes.prop_cycle'].by_key()['color']
color_cycle = cycle(color_pal)

def get_audio_files(pattern='*.wav'):
    """Return list of audio files matching the given pattern."""
    return glob(pattern)

def load_audio(file_path):
    """Load audio file using librosa."""
    y, sr = librosa.load(file_path)
    return y, sr

def plot_waveform(y, title='Audio Signal', color_idx=0, zoom_range=None):
    """Plot waveform of audio signal."""
    data = y if zoom_range is None else y[zoom_range[0]:zoom_range[1]]
    pd.Series(data).plot(figsize=(10, 5), lw=1, title=title, color=color_pal[color_idx])
    plt.show()

def trim_audio(y, top_db=20):
    """Trim silence from audio signal."""
    y_trimmed, _ = librosa.effects.trim(y, top_db=top_db)
    return y_trimmed

def compute_spectrogram(y):
    """Compute and return log-scaled spectrogram."""
    D = librosa.stft(y)
    S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
    return S_db

def plot_spectrogram(S_db, title='Spectrogram'):
    """Plot the given spectrogram."""
    fig, ax = plt.subplots(figsize=(10, 5))
    img = librosa.display.specshow(S_db, x_axis='time', y_axis='log', ax=ax)
    ax.set_title(title, fontsize=20)
    fig.colorbar(img, ax=ax, format=f'%0.2f')
    plt.show()

def compute_mel_spectrogram(y, sr, n_mels=256):
    """Compute and return log-scaled mel spectrogram."""
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=n_mels)
    S_db_mel = librosa.amplitude_to_db(S, ref=np.max)
    return S_db_mel
