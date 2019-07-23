########################################
# Sample Data generator from EDF file  #
# By @alborji       2019               #
########################################

import datetime, mne
from datetime import timedelta
from requests import post
from configuration import edf_file, patient_id , exam_id, headset_uuid, http_url
import time


# define data reader function to read time by time from edf file and send to HTTP server
def data_reader(t_time):
    data = raw.get_data(start=t_time * sfreq, stop=(1 + t_time) * sfreq)
    timestamp = exam_time + timedelta(seconds=t_time)
    struct_data = {}
    for i in range(n_channel):
        struct_data[channel_name[i]] = list(data[i])
    #create JSON data structure
    json_data = {
        "patient_id": patient_id.lower(),
        "exam_id" : exam_id.lower(),
        "n_channel": n_channel,
        "sample_time": timestamp.isoformat(),
        "channel_data": struct_data
    }
    # Send data to HTTP server (we use headset uuid as a token to verify data source
    res = post(url= http_url + '?' + headset_uuid, json=json_data)
    return res


if __name__ == '__main__':
    # Read edf file
    file = edf_file
    raw = mne.io.read_raw_edf(file)

    # read sample rate in file
    sfreq = int(raw.info['sfreq'])
    exam_time = datetime.datetime.utcfromtimestamp(raw.info['meas_date'][0])
    print('The exam time:', exam_time)

    # read channels in edf file
    channel_name = raw.ch_names
    n_channel = raw.info['nchan']

    # find duration of exam
    n_times = raw.n_times
    duration = int(n_times / sfreq)  # in second
    print('The exam duration:', duration, 'Sec')

    print('[*] Start to stream data ...')
    # Run a loop to tail edf file in time , every one second !

    for i in range(duration):
        res = data_reader(t_time=i)
        if res.status_code is 201:
            print('IN-T:' + str(i), 'Data send.')
        else:
            print('IN-T:' + str(i), 'Error on sending data')
        time.sleep(1)

