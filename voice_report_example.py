import os
import parselmouth

audio_data_path = './data/'                             # Audio MNIST 데이터가 있는 경로 설정
sound_folder_list = sorted(os.listdir(audio_data_path)) # 01 ~ 60 폴더명 정리 (정렬)
example_sound_list = sorted(os.listdir(audio_data_path+sound_folder_list[0])) # 01 폴더에 있는 파일 리스트

folder = sound_folder_list[0]
filename = example_sound_list[0]

sound = parselmouth.Sound('data/' + folder + '/' + filename) # 데이터 로드
pitch = sound.to_pitch()                                                                # pitch 계산 (아래 코드와 차이 비교)
# pitch = parselmouth.praat.call(sound, "To Pitch")
pulse = parselmouth.praat.call([sound, pitch], "To PointProcess (cc)")                  # pulses 계산

voice_report = parselmouth.praat.call([sound, pitch, pulse], "Voice report",
                                      0.0, 0.0, 75, 600, 1.3, 1.6, 0.03, 0.45)          # string 형태의 voice report 출력

voice_report_list = voice_report.split('\n')                                            # \n 단위로 분할하여 list로 저장

# voice report 분배
duration = voice_report_list[0]
# pitch
median_pitch_hertz = voice_report_list[2]
mean_pitch_hertz = voice_report_list[3]
standard_deviation_hertz = voice_report_list[4]
minimum_pitch_hertz = voice_report_list[5]
maximum_pitch_hertz = voice_report_list[6]
# pulses
number_of_pulses = voice_report_list[8]
number_of_periods = voice_report_list[9]
mean_period_sec = voice_report_list[10]
standard_deviation_of_period_sec = voice_report_list[11]
# voicing
unvoiced_str = voice_report_list[13] # frame num, entire frame num
number_of_voice_breaks = voice_report_list[14]
voice_breaks = voice_report_list[15] # degree of voice breaks second
# jitter
jitter_local_percent = voice_report_list[17]
jitter_local_absolute_sec = voice_report_list[18]
jitter_rap_percent = voice_report_list[19]
jitter_ppq5_percent = voice_report_list[20]
jitter_ddp_percent = voice_report_list[21]
# shimmer
shimmer_local_percent = voice_report_list[23]
shimmer_local_dB = voice_report_list[24]
shimmer_apq3_percent = voice_report_list[25]
shimmer_apq5_percent = voice_report_list[26]
shimmer_apq11_percent = voice_report_list[27]
shimmer_dda_percent = voice_report_list[28]
# harmonicity of the voiced parts only
mean_autocorrelation = voice_report_list[30]
mean_noise_to_harmonics_ratio = voice_report_list[31]
mean_harmonics_to_noise_ratio_dB = voice_report_list[32]

voice_report_dict = {}
voice_report_dict['folder'] = folder
voice_report_dict['filename'] = filename
del folder, filename

duration = float(duration.split(' ')[-2])
voice_report_dict['duration [sec]'] = duration
del duration

voice_report_dict['pitch'] = {}
median_pitch_hertz = float(median_pitch_hertz.split(' ')[-2])
mean_pitch_hertz = float(mean_pitch_hertz.split(' ')[-2])
standard_deviation_hertz = float(standard_deviation_hertz.split(' ')[-2])
minimum_pitch_hertz = float(minimum_pitch_hertz.split(' ')[-2])
maximum_pitch_hertz = float(maximum_pitch_hertz.split(' ')[-2])
voice_report_dict['pitch']['median pitch [Hz]'] = median_pitch_hertz
voice_report_dict['pitch']['mean pitch [Hz]'] = mean_pitch_hertz
voice_report_dict['pitch']['stddev [Hz]'] = standard_deviation_hertz
voice_report_dict['pitch']['minimum pitch [Hz]'] = minimum_pitch_hertz
voice_report_dict['pitch']['maximum pitch [Hz]'] = maximum_pitch_hertz
del median_pitch_hertz, mean_pitch_hertz, standard_deviation_hertz, minimum_pitch_hertz, maximum_pitch_hertz

voice_report_dict['pulses'] = {}
number_of_pulses = int(number_of_pulses.split(' ')[-1])
number_of_periods = int(number_of_periods.split(' ')[-1])
mean_period_sec = float(mean_period_sec.split(' ')[-2])
standard_deviation_of_period_sec = float(standard_deviation_of_period_sec.split(' ')[-2])
voice_report_dict['pulses']['number of pulses'] = number_of_pulses
voice_report_dict['pulses']['number of periods'] = number_of_periods
voice_report_dict['pulses']['mean periond [sec]'] = mean_period_sec
voice_report_dict['pulses']['stddev of period [sec]'] = standard_deviation_of_period_sec
del number_of_pulses, number_of_periods, mean_period_sec, standard_deviation_of_period_sec

voice_report_dict['voicing'] = {}
fraction_of_locally_unvoiced_frames = float(unvoiced_str.split(' ')[8][:-1])
unvoiced_frames = int(unvoiced_str.split(' ')[11][1:])
all_frames = int(unvoiced_str.split(' ')[-1][:-1])
number_of_voice_breaks = int(number_of_voice_breaks.split(' ')[-1])
degree_of_voice_breaks = int(voice_breaks.split(' ')[7])
voice_breaks_sec = float(voice_breaks.split(' ')[-5][1:])
voice_report_dict['voicing']['fraction of locally unvoiced frames'] = fraction_of_locally_unvoiced_frames
voice_report_dict['voicing']['unvoiced frames'] = unvoiced_frames
voice_report_dict['voicing']['all frames'] = all_frames
voice_report_dict['voicing']['number of voice breaks'] = number_of_voice_breaks
voice_report_dict['voicing']['degree of voice breaks'] = degree_of_voice_breaks
voice_report_dict['voicing']['voice breaks [sec]'] = voice_breaks_sec
del fraction_of_locally_unvoiced_frames, unvoiced_frames, unvoiced_str, all_frames, number_of_voice_breaks, degree_of_voice_breaks, voice_breaks_sec

voice_report_dict['jitter'] = {}
jitter_local_percent = float(jitter_local_percent.split(' ')[-1][:-1])
jitter_local_absolute_sec = float(jitter_local_absolute_sec.split(' ')[-2])
jitter_rap_percent = float(jitter_rap_percent.split(' ')[-1][:-1])
jitter_ppq5_percent = float(jitter_ppq5_percent.split(' ')[-1][:-1])
jitter_ddp_percent = float(jitter_ddp_percent.split(' ')[-1][:-1])
voice_report_dict['jitter']['local [%]'] = jitter_local_percent
voice_report_dict['jitter']['local(absolute) [sec]'] = jitter_local_absolute_sec
voice_report_dict['jitter']['rap [%]'] = jitter_rap_percent
voice_report_dict['jitter']['ppq5 [%]'] = jitter_ppq5_percent
voice_report_dict['jitter']['ddp [%]'] = jitter_ddp_percent
del jitter_local_percent, jitter_local_absolute_sec, jitter_rap_percent, jitter_ppq5_percent, jitter_ddp_percent

voice_report_dict['shimmer'] = {}
shimmer_local_percent = float(shimmer_local_percent.split(' ')[-1][:-1])
shimmer_local_dB = float(shimmer_local_dB.split(' ')[-2])
shimmer_apq3_percent = float(shimmer_apq3_percent.split(' ')[-1][:-1])
shimmer_apq5_percent = float(shimmer_apq5_percent.split(' ')[-1][:-1])
shimmer_apq11_percent = float(shimmer_apq11_percent.split(' ')[-1][:-1])
shimmer_dda_percent = float(shimmer_dda_percent.split(' ')[-1][:-1])
voice_report_dict['shimmer']['local [%]'] = shimmer_local_percent
voice_report_dict['shimmer']['local [dB]'] = shimmer_local_dB
voice_report_dict['shimmer']['apq3 [%]'] = shimmer_apq3_percent
voice_report_dict['shimmer']['apq5 [%]'] = shimmer_apq5_percent
voice_report_dict['shimmer']['apq11 [%]'] = shimmer_apq11_percent
voice_report_dict['shimmer']['dda [%]'] = shimmer_dda_percent
del shimmer_local_percent, shimmer_local_dB, shimmer_apq3_percent, shimmer_apq5_percent, shimmer_apq11_percent, shimmer_dda_percent

voice_report_dict['harmonicity'] = {}
mean_autocorrelation = float(mean_autocorrelation.split(' ')[-1])
mean_noise_to_harmonics_ratio = float(mean_noise_to_harmonics_ratio.split(' ')[-1])
mean_harmonics_to_noise_ratio_dB = float(mean_harmonics_to_noise_ratio_dB.split(' ')[-2])
voice_report_dict['harmonicity']['mean autocorrelation'] = mean_autocorrelation
voice_report_dict['harmonicity']['mean NHR'] = mean_noise_to_harmonics_ratio
voice_report_dict['harmonicity']['mean HNR [dB]'] = mean_harmonics_to_noise_ratio_dB
del mean_autocorrelation, mean_noise_to_harmonics_ratio, mean_harmonics_to_noise_ratio_dB
