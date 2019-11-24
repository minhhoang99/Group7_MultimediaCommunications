import pyaudio
import wave

print("Mời thầy nhập tên tệp âm thanh")
filename = input()      
# Đồ.wav , Đồ#.wav , Rê.wav , Mi.wav , Fa.wav , Fa#.wav , Son.wav , Son#.wav , La.wav , Si.wav , Si#.wav , Đô.wav

# Set chunk size of 92160 samples per data frame
chunk = 92160

# Open the sound file 
wf = wave.open(filename, 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# Read data in chunksF
data = wf.readframes(chunk)

# Play the sound by writing the audio data to the stream
while data != '':
    stream.write(data)
    data += wf.readframes(chunk)   # Tạo lặp lại
    

# Close and terminate the stream
stream.close()
p.terminate()


    
    
    


