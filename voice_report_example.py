import os
os.chdir('D:/Corp/11. parselmouth/')
import parselmouth

def get_voice_report(audioFile) :
    sound = parselmouth.Sound(audioFile)
    pitch = sound.to_pitch()
    pulse = parselmouth.praat.call([sound, pitch], "To PointProcess (cc)")
    voice_report = parselmouth.praat.call([sound, pitch, pulse], "Voice report", 0.0, 0.0, 75, 600, 1.3, 1.6, 0.03, 0.45)
    return voice_report

def voice_report_to_dictionary(voice_report, folder, filename) :
    voice_report_list = voice_report_list = voice_report.split('\n')
    
    voice_report_dict = {}
    voice_report_dict['folder'] = folder
    voice_report_dict['filename'] = filename
    voice_report_dict['duration [sec]'] = float(voice_report_list[0].split(' ')[-2])
    voice_report_dict['pitch'] = get_pitch_dictionary(voice_report_list)
    voice_report_dict['pulses'] = get_pulse_dictionary(voice_report_list)
    voice_report_dict['voicing'] = get_voicing_dictionary(voice_report_list)
    voice_report_dict['jitter'] = get_jitter_dictionary(voice_report_list)
    voice_report_dict['shimmer'] = get_shimmer_dictionary(voice_report_list)
    voice_report_dict['harmonicity of the voiced parts only'] = get_harmonicity_dictionary(voice_report_list)
    return voice_report_dict
    
def get_pitch_dictionary(voice_report_list) :
    pitch_dict = {}
    median_pitch_hertz = float(voice_report_list[2].split(' ')[-2])
    mean_pitch_hertz = float(voice_report_list[3].split(' ')[-2])
    standard_deviation_hertz = float(voice_report_list[4].split(' ')[-2])
    minimum_pitch_hertz = float(voice_report_list[5].split(' ')[-2])
    maximum_pitch_hertz = float(voice_report_list[6].split(' ')[-2])
    pitch_dict['median pitch [Hz]'] = median_pitch_hertz
    pitch_dict['mean pitch [Hz]'] = mean_pitch_hertz
    pitch_dict['stddev [Hz]'] = standard_deviation_hertz
    pitch_dict['minimum pitch [Hz]'] = minimum_pitch_hertz
    pitch_dict['maximum pitch [Hz]'] = maximum_pitch_hertz
    return pitch_dict

def get_pulse_dictionary(voice_report_list) :
    pulse_dict = {}
    number_of_pulses = int(voice_report_list[8].split(' ')[-1])
    number_of_periods = int(voice_report_list[9].split(' ')[-1])
    mean_period_sec = float(voice_report_list[10].split(' ')[-2])
    standard_deviation_of_period_sec = float(voice_report_list[11].split(' ')[-2])
    pulse_dict['number of pulses'] = number_of_pulses
    pulse_dict['number of periods'] = number_of_periods
    pulse_dict['mean periond [sec]'] = mean_period_sec
    pulse_dict['stddev of period [sec]'] = standard_deviation_of_period_sec
    return pulse_dict

def get_voicing_dictionary(voice_report_list) :
    voicing_dict = {}
    fraction_of_locally_unvoiced_frames = float(voice_report_list[13].split(' ')[8][:-1])
    unvoiced_frames = int(voice_report_list[13].split(' ')[11][1:])
    all_frames = int(voice_report_list[13].split(' ')[-1][:-1])
    number_of_voice_breaks = int(voice_report_list[14].split(' ')[-1])
    if '%' in voice_report_list[15].split(' ')[7] :
        degree_of_voice_breaks = float(voice_report_list[15].split(' ')[7][:-1])
    else :
        degree_of_voice_breaks = float(voice_report_list[15].split(' ')[7])
    voice_breaks_sec = float(voice_report_list[15].split(' ')[-5][1:])
    voicing_dict['fraction of locally unvoiced frames'] = fraction_of_locally_unvoiced_frames
    voicing_dict['unvoiced frames'] = unvoiced_frames
    voicing_dict['all frames'] = all_frames
    voicing_dict['number of voice breaks'] = number_of_voice_breaks
    voicing_dict['degree of voice breaks'] = degree_of_voice_breaks
    voicing_dict['voice breaks [sec]'] = voice_breaks_sec
    return voicing_dict

def get_jitter_dictionary(voice_report_list) :
    jitter_dict = {}
    jitter_local_percent = float(voice_report_list[17].split(' ')[-1][:-1])
    jitter_local_absolute_sec = float(voice_report_list[18].split(' ')[-2])
    jitter_rap_percent = float(voice_report_list[19].split(' ')[-1][:-1])
    jitter_ppq5_percent = float(voice_report_list[20].split(' ')[-1][:-1])
    jitter_ddp_percent = float(voice_report_list[21].split(' ')[-1][:-1])
    jitter_dict['local [%]'] = jitter_local_percent
    jitter_dict['local(absolute) [sec]'] = jitter_local_absolute_sec
    jitter_dict['rap [%]'] = jitter_rap_percent
    jitter_dict['ppq5 [%]'] = jitter_ppq5_percent
    jitter_dict['ddp [%]'] = jitter_ddp_percent
    return jitter_dict

def get_shimmer_dictionary(voice_report_list) :
    shimmer_dict = {}
    shimmer_local_percent = float(voice_report_list[23].split(' ')[-1][:-1])
    shimmer_local_dB = float(voice_report_list[24].split(' ')[-2])
    shimmer_apq3_percent = float(voice_report_list[25].split(' ')[-1][:-1])
    shimmer_apq5_percent = float(voice_report_list[26].split(' ')[-1][:-1])
    shimmer_apq11_percent = float(voice_report_list[27].split(' ')[-1][:-1])
    shimmer_dda_percent = float(voice_report_list[28].split(' ')[-1][:-1])
    shimmer_dict['local [%]'] = shimmer_local_percent
    shimmer_dict['local [dB]'] = shimmer_local_dB
    shimmer_dict['apq3 [%]'] = shimmer_apq3_percent
    shimmer_dict['apq5 [%]'] = shimmer_apq5_percent
    shimmer_dict['apq11 [%]'] = shimmer_apq11_percent
    shimmer_dict['dda [%]'] = shimmer_dda_percent
    return shimmer_dict

def get_harmonicity_dictionary(voice_report_list) :
    harmonicity_dictionary = {}
    mean_autocorrelation = float(voice_report_list[30].split(' ')[-1])
    mean_noise_to_harmonics_ratio = float(voice_report_list[31].split(' ')[-1])
    mean_harmonics_to_noise_ratio_dB = float(voice_report_list[32].split(' ')[-2])
    harmonicity_dictionary['mean autocorrelation'] = mean_autocorrelation
    harmonicity_dictionary['mean NHR'] = mean_noise_to_harmonics_ratio
    harmonicity_dictionary['mean HNR [dB]'] = mean_harmonics_to_noise_ratio_dB
    return harmonicity_dictionary

if __name__ == '__main__' :
    audio_data_path = './data/'
    sound_folder_list = sorted(os.listdir(audio_data_path))
    example_sound_list = sorted(f for f in os.listdir(audio_data_path + sound_folder_list[0]) if f.endswith('.wav'))
    
    folder = sound_folder_list[0]
    filename = example_sound_list[1]
    
    voice_report = get_voice_report('./data/' + folder + '/' + filename)
    voice_report_dict = voice_report_to_dictionary(voice_report, folder, filename)
