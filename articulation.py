import json
import syllables
import random
import soundfile
import sounddevice as sd
import os
from scipy.io.wavfile import write
mysp = __import__('my-voice-analysis')

f = open('paragraphs.txt', 'r')
paragraphs = f.read().split('\n')

def articulation():
    speed = 0
    status = 'n'
    while status == 'n':
        # Generate word
        paragraph = random.choice(paragraphs)
        print('Read the following paragraph out loud: {}'.format(paragraph))

        fs = 44000 # kHz
        duration = 12 # seconds
        myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()
        write('output.wav', fs, myrecording)

        # Convert to 16-bit
        data, samplerate = soundfile.read('output.wav')
        soundfile.write('output.wav', data, samplerate, subtype='PCM_16')

        # Check articulation
        p = "output" # Audio File title
        c = r"{}".format(os.getcwd()) # Path to the Audio_File directory (Python 3.7)
        mysp.mysptotal(p,c)

        # Check if user is tired
        status = input('Are you tired? Enter (y/n): ')
        if status == 'y':
            break

if __name__ == "__main__":
    articulation()
