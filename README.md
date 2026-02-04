# Text To Speech

Convert text into MP3 audio files using Microsoft Edge's neural text-to-speech engine with inline SSML support.

- Supports string input or text files
- Supports inline SSML formatting for pauses, emphasis, pronunciation control
- Access to multiple natural-sounding neural voices
- Configurable speech rate, pitch, and volume
- Outputs MP3 format audio files

## Prerequisites

This script requires Python 3 and the Microsoft edge-tts package.

```bash
sudo apt install git python3 python3-pip
pip install edge-tts
```

## Basic Usage

Clone the repository and run a basic test:

```bash
git clone https://github.com/Chubtoad5/text-to-speech.git
cd text-to-speech
python3 text_to_speech_ssml.py -t "Convert this text to speech." -o audio_test.mp3
```

## Usage Syntax

```
python3 text_to_speech_ssml.py [OPTIONS]

Options:
  -t, --text TEXT       Text to convert (can include inline SSML tags)
  -i, --input FILE      Input text file (can contain SSML tags)
  -o, --output FILE     Output MP3 filename (default: output.mp3)
  -v, --voice VOICE     Voice option (default: male_us_professional)
  -r, --rate RATE       Speech rate: -100% to +200% (default: 0%)
  -p, --pitch PITCH     Pitch adjustment: -50% to +50% (default: 0%)
  --volume VOLUME       Volume level: 0% to 200% (default: 100%)
  --examples            Show SSML examples and documentation
```

## Voice Options

Built-in voice presets:

| Option | Voice |
|--------|-------|
| `male_us_professional` | en-US-GuyNeural (default) |
| `female_us_professional` | en-US-JennyNeural |
| `male_us_casual` | en-US-ChristopherNeural |
| `female_us_casual` | en-US-AriaNeural |

You can also use any Edge TTS voice name directly (e.g., `en-GB-SoniaNeural`).

To list all available voices:
```bash
python3 list_voices.py
```

## Inline SSML Features

The script supports inline SSML tags for fine-grained control over speech output:

### Pauses
```xml
<break time="500ms"/>         Pause for 500 milliseconds
<break time="2s"/>            Pause for 2 seconds
<break strength="weak"/>      Short pause (like a comma)
<break strength="medium"/>    Medium pause (like a period)
<break strength="strong"/>    Long pause (like a paragraph break)
```

### Emphasis
```xml
<emphasis level="strong">important</emphasis>    Emphasize strongly
<emphasis level="moderate">notable</emphasis>    Moderate emphasis
<emphasis level="reduced">minor</emphasis>       De-emphasize
```

### Pronunciation Control
```xml
<say-as interpret-as="spell-out">API</say-as>           Spell out "A-P-I"
<say-as interpret-as="digits">123</say-as>              Say "one two three"
<say-as interpret-as="cardinal">123</say-as>            Say "one hundred twenty three"
<say-as interpret-as="ordinal">1</say-as>               Say "first"
<say-as interpret-as="date" format="mdy">3/15/2024</say-as>
```

### Pacing and Pitch (inline)
```xml
<prosody rate="slow">slower speech</prosody>
<prosody rate="fast">faster speech</prosody>
<prosody rate="150%">50% faster</prosody>
<prosody pitch="high">higher pitch</prosody>
<prosody volume="loud">louder</prosody>
```

### Text Substitution
```xml
<sub alias="World Wide Web Consortium">W3C</sub>
```

## Examples

Basic text to speech:
```bash
python3 text_to_speech_ssml.py -t "Hello world!" -o hello.mp3
```

Using a different voice:
```bash
python3 text_to_speech_ssml.py -t "Hello world!" -o hello.mp3 -v female_us_casual
```

Adjusting speech rate and pitch:
```bash
python3 text_to_speech_ssml.py -t "Speaking faster and higher." -o fast.mp3 -r "+50%" -p "+10%"
```

Using inline SSML for pauses and emphasis:
```bash
python3 text_to_speech_ssml.py -t "Welcome to the demo. <break time=\"1s\"/> This is <emphasis level=\"strong\">important</emphasis>." -o demo.mp3
```

Converting a text file:
```bash
python3 text_to_speech_ssml.py -i script.txt -o narration.mp3 -v female_us_professional
```

Show all SSML examples:
```bash
python3 text_to_speech_ssml.py --examples
```
