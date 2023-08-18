import numpy as np
from glob import glob
import os

y = glob(f"C:\\Users\\scrat\\OneDrive\\Documents\\Dev\\Python_Projects\\Impromptu\\data\\stutter\\mel_spectrograms\\*.npz")

for f in y:
    g = np.load(f, 'r', allow_pickle=True)['mel_spec']
    if g.shape[1] != 130:
        title = f.split('.')[0].split('/')[-1].split('\\')[-1]
        subpath =f"C:\\Users\\scrat\\OneDrive\\Documents\\Dev\\Python_Projects\\Impromptu\\data\\stutter\\"
        if os.path.exists(f"{subpath}audio_files\\{title}.wav"):
            os.remove(f"{subpath}audio_files\\{title}.wav")
        if os.path.exists(f"{subpath}mel_spectrograms\\{title}.npz"):
            os.remove(f"{subpath}mel_spectrograms\\{title}.npz")
        if os.path.exists(f"{subpath}labels\\{title}.npz"):
            os.remove(f"{subpath}labels\\{title}.npz")
        print("removed")