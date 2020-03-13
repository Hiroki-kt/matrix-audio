import pyaudio

audio = pyaudio.PyAudio()
device_num = audio.get_device_count()

for i in range(device_num):
    print(audio.get_device_info_by_index(i))
