# post lab 20
# -------------------------------------------------------------------------------------------------------------------
# 1 code :
import soundfile as sf

# Load audio file
audio, sample_rate = sf.read(r'D:\python programming\python_pizza\pizza_audio.mp3') # Write audio file
sf.write('new_audio_file.wav', audio, sample_rate) 
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
 # Load audio file
#audio, sample_rate = sf.read('audio_file.wav') # Create time axis
time = np.arange(0, len(audio)) / sample_rate # Plot audio signal
plt.plot(time, audio)
plt.xlabel('Time (s)') 
plt.ylabel('Amplitude')
plt.show()

# 2 code 
# pip install pydub
from pydub import AudioSegment
 
# Load audio file
audio = AudioSegment.from_file('D:\python programming\python_pizza\pizza_audio.mp3')

# Add fade in effect
audio_fade_in = audio.fade_in(2000) # 2 seconds

# Export audio file with fade in effect audio_fade_in.export('audio_file_fade_in.wav', format='wav')
