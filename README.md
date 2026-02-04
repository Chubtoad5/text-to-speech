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

## Usage
```
usage: text_to_speech_ssml.py [-h] [-i INPUT] [-o OUTPUT] [-v VOICE] [-r RATE] [-p PITCH] [--volume VOLUME] [-t TEXT] [--examples]

Convert text to speech with SSML control

options:
  -h, --help                  Show this help message and exit
  -i INPUT, --input INPUT     Input text file (can contain SSML tags)
  -o OUTPUT, --output OUTPUT  Output MP3 filename
  -v VOICE, --voice VOICE     Voice option
  -r RATE, --rate RATE        Speech rate: -100% to +200% (default: 0%)
  -p PITCH, --pitch PITCH     Pitch: -50% to +50% (default: 0%)
  --volume VOLUME             Volume: 0% to 200% (default: 100%)
  -t TEXT, --text TEXT        Text to convert (can include SSML tags)
  --examples                  Show SSML examples and documentation
```
## Usage Examples

```
python3 text_to_speech_ssml.py -t "Convert this text to speech." -o audio_test.mp3

python3 text_to_speech_ssml.py -i transcript.txt -o audio_test.mp3 -v female_us_casual

python3 text_to_speech_ssml.py -t "Convert this text to speech." -o audio_test.mp3 -r +20%

```


### SSML CONTROL EXAMPLES
```
PAUSES:
  <break time="500ms"/>          - Pause for 500 milliseconds
  <break time="2s"/>             - Pause for 2 seconds
  <break strength="weak"/>       - Short pause (like a comma)
  <break strength="medium"/>     - Medium pause (like a period)
  <break strength="strong"/>     - Long pause (like a paragraph break)

EMPHASIS:
  <emphasis level="strong">important</emphasis>     - Emphasize strongly
  <emphasis level="moderate">notable</emphasis>     - Moderate emphasis
  <emphasis level="reduced">minor</emphasis>        - De-emphasize

PRONUNCIATION:
  <phoneme alphabet="ipa" ph="təˈmeɪtoʊ">tomato</phoneme>
  <say-as interpret-as="spell-out">API</say-as>    - Spell out "A-P-I"
  <say-as interpret-as="digits">123</say-as>       - Say "one two three"
  <say-as interpret-as="cardinal">123</say-as>     - Say "one hundred twenty three"
  <say-as interpret-as="ordinal">1</say-as>        - Say "first"
  <say-as interpret-as="date" format="mdy">3/15/2024</say-as>

PACING & PITCH (can be applied to sections):
  <prosody rate="slow">slower speech</prosody>
  <prosody rate="fast">faster speech</prosody>
  <prosody rate="150%">50% faster</prosody>
  <prosody pitch="high">higher pitch</prosody>
  <prosody pitch="+10%">slightly higher</prosody>
  <prosody volume="loud">louder</prosody>

SUBSTITUTE TEXT (say one thing while displaying another):
  <sub alias="World Wide Web Consortium">W3C</sub>

EXAMPLE FULL TEXT:
  Welcome to today's training. <break time="1s"/>
  We'll cover three topics: <break strength="medium"/>
  <emphasis level="strong">automation</emphasis>,
  <break strength="weak"/>
  infrastructure,
  <break strength="weak"/>
  and monitoring.
  <break time="2s"/>
  Let's begin with <prosody rate="slow">automation fundamentals</prosody>.
```