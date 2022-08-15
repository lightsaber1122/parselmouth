import os
import parselmouth

audio_data_path = './data/'
sound_folder_list = sorted(os.listdir(audio_data_path))
example_sound_list = sorted(os.listdir(audio_data_path+sound_folder_list[0]))

sound = parselmouth.Sound('data/' + sound_folder_list[0] + '/' + example_sound_list[0])
pitch = sound.to_pitch()
# pitch = parselmouth.praat.call(sound, "To Pitch")
pulse = parselmouth.praat.call([sound, pitch], "To PointProcess (cc)")

voice_report = parselmouth.praat.call([sound, pitch, pulse], "Voice report", 0.0, 0.0, 75, 600, 1.3, 1.6, 0.03, 0.45)

voice_report_list = voice_report.split('\n')

duration_str_list = voice_report_list[0]
pitch_str_list = voice_report_list[1:7]
pulse_str_list = voice_report_list[7:12]
voicing_str_list = voice_report_list[12:16]
jitter_str_list = voice_report_list[16:22]
shimmer_str_list = voice_report_list[22:29]
harmonicity_str_list = voice_report_list[29:33]
