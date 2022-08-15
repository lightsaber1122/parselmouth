import os
import parselmouth

audio_data_path = './data/'                             # Audio MNIST 데이터가 있는 경로 설정
sound_folder_list = sorted(os.listdir(audio_data_path)) # 01 ~ 60 폴더명 정리 (정렬)
example_sound_list = sorted(os.listdir(audio_data_path+sound_folder_list[0])) # 01 폴더에 있는 파일 리스트

sound = parselmouth.Sound('data/' + sound_folder_list[0] + '/' + example_sound_list[0]) # 데이터 로드
pitch = sound.to_pitch()                                                                # pitch 계산 (아래 코드와 차이 비교)
# pitch = parselmouth.praat.call(sound, "To Pitch")
pulse = parselmouth.praat.call([sound, pitch], "To PointProcess (cc)")                  # pulses 계산

voice_report = parselmouth.praat.call([sound, pitch, pulse], "Voice report",
                                      0.0, 0.0, 75, 600, 1.3, 1.6, 0.03, 0.45)          # string 형태의 voice report 출력

voice_report_list = voice_report.split('\n')                                            # \n 단위로 분할하여 list로 저장

duration_str_list = voice_report_list[0]          # duration이 포함된 항목 (후처리 필요)
pitch_str_list = voice_report_list[1:7]           # pitch가 포함된 항목 (median, mean, min, max, ...)
pulse_str_list = voice_report_list[7:12]          # pulse가 포함된 항목
voicing_str_list = voice_report_list[12:16]       # voicing이 포함된 항목
jitter_str_list = voice_report_list[16:22]        # jitter가 포함된 항목
shimmer_str_list = voice_report_list[22:29]       # shimmer가 포함된 항목
harmonicity_str_list = voice_report_list[29:33]   # HNR 등이 포함된 항목
