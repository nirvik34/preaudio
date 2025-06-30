from preaudio import (
    get_audio_files,
    load_audio,
    plot_waveform,
    trim_audio,
    compute_spectrogram,
    plot_spectrogram,
    compute_mel_spectrogram
)
files = get_audio_files('audio2.wav') 
y, sr = load_audio(files[0])
plot_waveform(y, title='Raw Audio')
y_trimmed = trim_audio(y)
plot_waveform(y_trimmed, title='Trimmed Audio', color_idx=1)
plot_waveform(y, title='Zoomed In Audio', color_idx=2, zoom_range=(30000, 30500))
S_db = compute_spectrogram(y)
plot_spectrogram(S_db, title='Spectrogram')
S_db_mel = compute_mel_spectrogram(y, sr)
plot_spectrogram(S_db_mel, title='Mel Spectrogram')

