# Text To Speach

Use this app to convert text into mp3 audio files using an SSML based text-to-speach algorithm.  

- Supports string input or txt files
- Supports SSML formatting
- Access to 100's of different neural voices using the `list_voices.py`
- Outputs and mp3 format file

## Prerequisites

This script leverages python and the Microsoft edge-tts package

```
sudo apt install git phython3 python3-pip
pip install edge-tts
```


## Running the script
Clone the repository and run a basic test

```
git clone https://github.com/Chubtoad5/text-to-speach.git
cd text-to-speach
python3 text_to_speech_ssml.py -t "Convert this text to speech." -o audio_test.mp3
```

Other parameters  
```

```

### Examples