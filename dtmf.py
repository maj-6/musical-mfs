#!/usr/bin/env python

import sys
import math
import pyaudio
import binascii
import numpy as np

def sine(freq, length, rate):
    length = int(length * rate)
    factor = float(freq) * (math.pi * 2) / rate
    return np.sin(np.arange(length) * factor)

def tone(f1, f2, length, rate):
    tone1=sine(f1,length,rate)
    tone2=sine(f2,length,rate)
    dual=tone1+tone2
    return dual

def play(s, sequence, length=0.6, rate=44100):

    base = 427.00 

    unison = base * 1.0000 ; octave = base * 2.0000
    min2nd = base * 1.0417 ; maj2nd = base * 1.1250
    min3rd = base * 1.2000 ; maj3rd = base * 1.2500
    fourth = base * 1.3333 ; fifth_ = base * 1.5000
    min6th = base * 1.6000 ; maj6th = base * 1.6667
    min7th = base * 1.8000 ; maj7th = base * 1.8750
                  
    tones = {'0': (fourth,maj6th), '1': (fourth, fifth_), '2': (fourth, maj3rd), '3': (fourth, maj2nd),
             '4': (unison,maj6th), '5': (unison, fifth_), '6': (unison, maj3rd), '7': (unison, maj2nd),
             '8': (octave,maj6th), '9': (octave, fifth_), 'a': (octave, maj3rd), 'b': (octave, maj2nd),
             'c': (maj7th,maj6th), 'd': (maj7th, fifth_), 'e': (maj7th, maj3rd), 'f': (maj7th, maj2nd)}

    print(" ")


    for j in sequence:

        samples = []
        samples.append(tone(tones[j][0], tones[j][1], length, rate))

        s.write(np.float32(np.concatenate(samples)) / 2)

        sys.stdout.write(j)
    sys.stdout.flush()


    print("\n")

##################################################################

p = pyaudio.PyAudio()
s = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, output=1)
sequence = binascii.hexlify(raw_input("\033c" + "Input: "))
play(s, sequence)
s.close()
p.terminate()