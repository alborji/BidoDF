# BidoDF

   A `parser` for EDF and `stream` of EDF data across a network or internet

---
### Overview
We needed a small tools to pars lard EDF tools and stream it's data via network base on TCP/IP. So, I write this codes 
to emulate a EEG headset. 
 - Read data from EDF file (instead of Headset probes)
 - convert data to `JSON` format.
 - send to a sample HTTP listener by `post` method.
 

---
### Usage

fist clone this repository. In this I have blow files:

- `configuration.py`
    
    set your setting in this file.
- `requirements.txt`

    use this file to install python moduls via `pip` 
    
- `reader.py`

    main file, that you must run it.
    
- `sample.edf`

    A sample `edf` file for test. you can replace it with your `edf` file.
   
 
 After cloning, you must install python modules. (use `python version 3`)
 ```bash
pip3 install -f requirements.txt
```

Then you must set your setting in configuration file:
 
 ```python
# Defining EDF file path (user full path)
edf_file = 'sample.edf'

# Define your http listener (http ingress)
http_url = 'https://myserver.mydomain.local/'

# Defining your patient ID
patient_id = 'patient-A'

# Defining your exam ID
exam_id = 'Exam-1'

# Defining Your headset UUID
headset_uuid = '12345'
```

The code automatically detect sample rate and send data for `ONE` second in one `JSON` via http protocol.
 

At the end you can run `reader.py` file: 


```bash
python3 reader.py
```
 
 
 
 
  
  