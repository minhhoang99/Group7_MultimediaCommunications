import numpy as np
import wave
import struct
import matplotlib.pyplot as plt

# Tạo sóng 
sampling_rate = 44100       # là tốc độ lấy mẫu = 2 * 22050 = 2 * tần số nghe đươc
num_samples = 88200         # là số lượng mẫu sẽ lấy
amplitude = 8000            # là biên độ
sine_wave = []              # là list lưu các mẫu

############ Tạo sóng âm thanh nốt Đồ  ############
frequency = 440 / ((2**(1/12))**8)            # là tần số sóng nốt Đồ
for x in range(num_samples): 
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
# Với giá trị x chạy từ 0 đến num_samples - 1= 88200 - 1, ta thêm các giá trị được lấy mẫu sin(2*pi*f*n*T) vào list sine_wave


# Lưu sóng vào file âm thanh .wav:
#Mở file
file = "Đồ.wav"         
wav_file=wave.open(file, 'w')

nframes=num_samples         # Số lượng mẫu --> num_samples = 88200
comptype="NONE"             # compression type, dữ liệu không được nén --> "NONE"
compname="not compressed"   # compression name, dữ liệu của ta không được nén --> "not compressed"
nchannels=1                 # Số kênh của âm thanh --> 1 - mono audio
sampwidth=2                 # Chiều dài mẫu đơn vị là bytes --> 2
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))

# Viết vào file
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
# Đóng file
wav_file.close()

# Thêm bước kiểm tra đồ thị sóng
plt.plot(sine_wave[:300])
plt.show()



#Tương tự với các nốt khác:

############ Tạo sóng âm thanh nốt Đồ# ############
frequency = 440 / ((2**(1/12))**7)          # là tần số sóng nốt Đồ# , theo đề bài em lấy tần số nốt Fa làm chuẩn 440Hz
sine_wave = []                              # Khởi tạo lại list
for x in range(num_samples): 
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
file = "Đồ#.wav"     
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()

############ Tạo sóng âm thanh nốt Rê  ############
frequency = 440 / ((2**(1/12))**6)        
sine_wave = []
for x in range(num_samples): 
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
file = "Rê.wav"     
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()

############ Tạo sóng âm thanh nốt Mi  ############
frequency = 440 / ((2**(1/12))**5)        
sine_wave = []
for x in range(num_samples): 
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
file = "Mi.wav"     
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()

############ Tạo sóng âm thanh nốt Fa  ############
frequency = 440 / ((2**(1/12))**4)        
sine_wave = []
for x in range(num_samples): 
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
file = "Fa.wav"     
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()

############ Tạo sóng âm thanh nốt Fa# ############
frequency = 440 / ((2**(1/12))**3)        
sine_wave = []
for x in range(num_samples): 
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
file = "Fa#.wav"     
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()

############ Tạo sóng âm thanh nốt Son ############
frequency = 440 / ((2**(1/12))**2)        
sine_wave = []
for x in range(num_samples): 
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
file = "Son.wav"     
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()

############ Tạo sóng âm thanh nốt Son# ############
frequency = 440 / (2**(1/12))      
sine_wave = []
for x in range(num_samples): 
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
file = "Son#.wav"     
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()

############ Tạo sóng âm thanh nốt La  ############
frequency = 440       
sine_wave = []
for x in range(num_samples): 
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
file = "La.wav"     
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()

############ Tạo sóng âm thanh nốt Si ############
frequency = 440 * (2**(1/12))
sine_wave = []
for x in range(num_samples): 
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
file = "Si.wav"     
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()

############ Tạo sóng âm thanh nốt Si# ############
frequency = 440 * ((2**(1/12))**2)        
sine_wave = []
for x in range(num_samples): 
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
file = "Si#.wav"     
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()

############ Tạo sóng âm thanh nốt Đô  ############
frequency = 440 * ((2**(1/12))**3)        
sine_wave = []
for x in range(num_samples): 
    sine_wave.append(np.sin(2 * np.pi * frequency * x * 1/sampling_rate))
file = "Đô.wav"     
wav_file=wave.open(file, 'w')
wav_file.setparams((nchannels, sampwidth, int(sampling_rate), nframes, comptype, compname))
for s in sine_wave:
    wav_file.writeframes(struct.pack('h', int(s*amplitude)))
wav_file.close()







