import numpy as np
import csv
from glob import glob
import os
import shutil

sample_rate = 22050
duration = 3
h_step = 512
length = 130
data_type = "mfcc"
target_type = "stuttered_words"

if not os.path.exists(f"C:/Users/scrat/OneDrive/Documents/Dev/Python_Projects/Impromptu/data/stutter/{data_type}/labels/{target_type}"):
    os.mkdir(f"C:/Users/scrat/OneDrive/Documents/Dev/Python_Projects/Impromptu/data/stutter/{data_type}/labels/{target_type}")

with open('fluencybank_labels.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    print("reading csv")
    for row in csvreader:
        unsure = int(row['Unsure'])
        poor_qual = int(row['PoorAudioQuality'])
        prolongation = int(row['Prolongation'])
        block = int(row['Block'])
        sound_rep = int(row['SoundRep'])
        word_rep = int(row['WordRep'])
        difficult_to_understand = int(row['DifficultToUnderstand'])
        interjection = int(row['Interjection'])
        no_stuttered_words = int(row['NoStutteredWords'])
        natural_pause = int(row['NaturalPause'])
        music = int(row['Music'])
        no_speech = int(row['NoSpeech'])
        
        if unsure != 0 or no_speech != 0 or difficult_to_understand != 0:
            continue
        
        path = f"D:/Documents/Python_Files/fluency_dataset_clips/{row['Show']}/{row['EpId']}/{row['Show']}_{row['EpId']}_{row['ClipId']}.wav"
        
        if os.path.exists(path):
            # shutil.copy(path, "C:/Users/scrat/OneDrive/Documents/Dev/Python_Projects/Impromptu/data/stutter/audio_files")
            # prolongation = np.ones(shape=(length,)) * (prolongation > 0)
            # block = np.ones(shape=(length,)) * (block > 0)
            # sound_rep = np.ones(shape=(length,)) * (sound_rep > 0)
            # word_rep = np.ones(shape=(length,)) * (word_rep > 0)
            # interjection = np.ones(shape=(length,)) * (interjection > 0)
            # no_stuttered_words = np.ones(shape=(length,)) * (no_stuttered_words > 1)
            # natural_pause = np.ones(shape=(length,)) * (natural_pause > 0)
            # music = np.ones(shape=(length,)) * (music > 0)
            # out_val = np.array([
            #     prolongation,
            #     block,
            #     sound_rep,
            #     word_rep,
            #     interjection,
            #     no_stuttered_words,
            #     natural_pause,
            #     music
            # ]).T
            stuttered_words = np.ones(shape=(length,)) * ((sound_rep > 0) + (word_rep > 1) > 0)
            out_val = np.array([stuttered_words]).T
            np.savez_compressed(f"C:/Users/scrat/OneDrive/Documents/Dev/Python_Projects/Impromptu/data/stutter/{data_type}/labels/{target_type}/{row['Show']}_{row['EpId']}_{row['ClipId']}.npz", labels=out_val)


with open('SEP-28k_labels.csv', 'r') as csvfile:
    csvreader = csv.DictReader(csvfile)
    print("reading csv")
    for row in csvreader:
        unsure = int(row['Unsure'])
        poor_qual = int(row['PoorAudioQuality'])
        prolongation = int(row['Prolongation'])
        block = int(row['Block'])
        sound_rep = int(row['SoundRep'])
        word_rep = int(row['WordRep'])
        difficult_to_understand = int(row['DifficultToUnderstand'])
        interjection = int(row['Interjection'])
        no_stuttered_words = int(row['NoStutteredWords'])
        natural_pause = int(row['NaturalPause'])
        music = int(row['Music'])
        no_speech = int(row['NoSpeech'])
        
        if unsure != 0 or no_speech != 0 or difficult_to_understand != 0:
            continue
        
        path = f"D:/Documents/Python_Files/stuttering_dataset_clips/{row['Show']}/{row['EpId']}/{row['Show']}_{row['EpId']}_{row['ClipId']}.wav"
        
        if os.path.exists(path):
            # shutil.copy(path, "C:/Users/scrat/OneDrive/Documents/Dev/Python_Projects/Impromptu/data/stutter/audio_files")
            # prolongation = np.ones(shape=(length,)) * (prolongation > 0)
            # block = np.ones(shape=(length,)) * (block > 0)
            # sound_rep = np.ones(shape=(length,)) * (sound_rep > 0)
            # word_rep = np.ones(shape=(length,)) * (word_rep > 0)
            # interjection = np.ones(shape=(length,)) * (interjection > 0)
            # no_stuttered_words = np.ones(shape=(length,)) * (no_stuttered_words > 1)
            # natural_pause = np.ones(shape=(length,)) * (natural_pause > 0)
            # music = np.ones(shape=(length,)) * (music > 0)
            # out_val = np.array([
            #     prolongation,
            #     block,
            #     sound_rep,
            #     word_rep,
            #     interjection,
            #     no_stuttered_words,
            #     natural_pause,
            #     music
            # ]).T
            stuttered_words = np.ones(shape=(length,)) * ((sound_rep > 0) + (word_rep > 1) > 0)
            out_val = np.array([stuttered_words]).T
            np.savez_compressed(f"C:/Users/scrat/OneDrive/Documents/Dev/Python_Projects/Impromptu/data/stutter/{data_type}/labels/{target_type}/{row['Show']}_{row['EpId']}_{row['ClipId']}.npz", labels=out_val)