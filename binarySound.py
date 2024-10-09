import numpy as np
import sounddevice as sd

#turn the input to binary
def input_to_binary(message):
    binary_list = [format(ord(char), '08b') for char in message]
    return ' '.join(binary_list)

#input
message = input("Enter message: ")
binary_result = input_to_binary(message)
print(binary_result)

duration = 0.5
sample_rate = 44100
#take each 0 bit and play as chosen frequency
for bit in binary_result:
    if bit == '0':
        frequency = 220 #edit here

    else:
        frequency = 400 #edit here
        
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)

    sd.play(tone, samplerate=sample_rate)
    sd.wait()