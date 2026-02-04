#!/usr/bin/env python3
"""
Text-to-Speech using Microsoft Edge TTS

Supports speech rate, pitch, and volume adjustments.
Note: Custom SSML tags are NOT supported by edge-tts due to Microsoft restrictions.
"""

import asyncio
import edge_tts
import argparse
import os
import re

# SSML Limitation Note:
# edge-tts no longer supports custom SSML tags (break, emphasis, say-as, etc.)
# Microsoft only allows a single <voice> tag with a single <prosody> tag.
# This script strips unsupported SSML tags and uses only the supported prosody parameters.

# Popular natural-sounding voices
VOICE_OPTIONS = {
    "male_us_professional": "en-US-GuyNeural",
    "female_us_professional": "en-US-JennyNeural",
    "male_us_casual": "en-US-ChristopherNeural",
    "female_us_casual": "en-US-AriaNeural",
}

# SSML tags that are NOT supported by edge-tts (will be stripped)
UNSUPPORTED_SSML_TAGS = [
    'break', 'emphasis', 'say-as', 'phoneme', 'sub', 'prosody',
    'voice', 'speak', 'p', 's', 'w', 'lang', 'mark', 'desc', 'audio',
    'mstts:express-as', 'mstts:silence', 'mstts:backgroundaudio'
]

def detect_ssml_tags(text):
    """
    Detect SSML tags in text and return a list of found tags.

    Args:
        text (str): Text that may contain SSML tags

    Returns:
        list: List of unique SSML tag names found in the text
    """
    # Pattern to match SSML tags (both opening and self-closing)
    pattern = r'</?([a-zA-Z][a-zA-Z0-9:-]*)[^>]*/?>'
    matches = re.findall(pattern, text)
    return list(set(matches))

def strip_ssml_tags(text):
    """
    Remove all SSML tags from text, keeping only the text content.

    Args:
        text (str): Text containing SSML tags

    Returns:
        str: Plain text with all SSML tags removed
    """
    # Remove self-closing tags like <break time="1s"/>
    text = re.sub(r'<[^>]+/>', '', text)
    # Remove opening tags like <emphasis level="strong">
    text = re.sub(r'<[a-zA-Z][^>]*>', '', text)
    # Remove closing tags like </emphasis>
    text = re.sub(r'</[a-zA-Z][^>]*>', '', text)
    # Clean up extra whitespace (but preserve paragraph breaks)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text.strip()

async def text_to_speech_ssml(text, output_filename="output.mp3", voice="male_us_professional",
                               rate="0%", pitch="0%", volume="100%", use_ssml=True):
    """
    Convert text to speech using Edge TTS.

    Note: edge-tts no longer supports custom SSML tags (break, emphasis, say-as, etc.)
    due to Microsoft restrictions. Only rate, pitch, and volume adjustments are supported.
    Any SSML tags in the input will be stripped and a warning will be displayed.

    Args:
        text (str): The text to convert (SSML tags will be stripped)
        output_filename (str): Name of the output MP3 file
        voice (str): Voice option key from VOICE_OPTIONS or full voice name
        rate (str): Speech rate adjustment (-100% to +200%)
        pitch (str): Pitch adjustment (-50% to +50%)
        volume (str): Volume adjustment (0% to 200%)
        use_ssml (bool): Whether to apply rate/pitch/volume settings
    """
    try:
        # Get the voice name
        if voice in VOICE_OPTIONS:
            voice_name = VOICE_OPTIONS[voice]
        elif voice.endswith("Neural") or "-" in voice:
            voice_name = voice
        else:
            voice_name = VOICE_OPTIONS["male_us_professional"]

        # Check for SSML tags and warn user if found
        detected_tags = detect_ssml_tags(text)
        if detected_tags:
            print(f"⚠ Warning: SSML tags detected but not supported by edge-tts: {', '.join(detected_tags)}")
            print("  These tags will be stripped. Only --rate, --pitch, and --volume are supported.")
            print("  Microsoft has restricted edge-tts to prevent custom SSML usage.")
            # Strip all SSML tags from the text
            text = strip_ssml_tags(text)

        # Create TTS communicator with voice and prosody parameters
        # Note: edge-tts only supports rate, pitch, and volume as parameters
        communicate = edge_tts.Communicate(text, voice_name, rate=rate, pitch=pitch, volume=volume)

        # Save to MP3 file
        await communicate.save(output_filename)

        print(f"✓ Audio file created successfully: {output_filename}")
        print(f"  Voice: {voice_name}")
        print(f"  Rate: {rate}, Pitch: {pitch}, Volume: {volume}")
        print(f"  File size: {os.path.getsize(output_filename):,} bytes")

    except Exception as e:
        print(f"✗ Error creating audio file: {e}")

def read_text_file(filename):
    """Read text from a file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read().strip()
        print(f"✓ Read {len(text)} characters from {filename}")
        return text
    except FileNotFoundError:
        print(f"✗ Error: File '{filename}' not found")
        return None
    except Exception as e:
        print(f"✗ Error reading file: {e}")
        return None

def show_ssml_examples():
    """Display speech control examples and documentation"""
    examples = """
=== SPEECH CONTROL OPTIONS ===

IMPORTANT: Custom SSML tags (break, emphasis, say-as, phoneme, etc.) are NOT
supported by edge-tts. Microsoft has restricted the service to prevent custom
SSML usage. Any SSML tags in your input will be automatically stripped.

SUPPORTED OPTIONS (command-line parameters):

SPEECH RATE (--rate or -r):
  --rate="-50%"    - 50% slower than normal
  --rate="0%"      - Normal speed (default)
  --rate="+50%"    - 50% faster than normal
  --rate="+100%"   - Double speed
  Range: -100% to +200%

PITCH (--pitch or -p):
  --pitch="-20%"   - Lower pitch
  --pitch="0%"     - Normal pitch (default)
  --pitch="+20%"   - Higher pitch
  Range: -50% to +50%

VOLUME (--volume):
  --volume="50%"   - Half volume
  --volume="100%"  - Normal volume (default)
  --volume="150%"  - 50% louder
  Range: 0% to 200%

VOICE OPTIONS (--voice or -v):
  male_us_professional   - en-US-GuyNeural (default)
  female_us_professional - en-US-JennyNeural
  male_us_casual         - en-US-ChristopherNeural
  female_us_casual       - en-US-AriaNeural
  Or use any valid Microsoft Edge voice name directly

EXAMPLE COMMANDS:
  python text_to_speech_ssml.py -i script.txt -o output.mp3
  python text_to_speech_ssml.py -t "Hello world" --rate="-20%" --pitch="+10%"
  python text_to_speech_ssml.py -i script.txt -v female_us_professional

NOTE: If your input contains SSML tags, they will be stripped and a warning
will be displayed. The text content inside the tags will still be spoken.
"""
    print(examples)

async def main():
    parser = argparse.ArgumentParser(
        description="Convert text to speech using Microsoft Edge TTS"
    )
    parser.add_argument(
        "-i", "--input",
        help="Input text file (SSML tags will be stripped)"
    )
    parser.add_argument(
        "-o", "--output",
        default="output.mp3",
        help="Output MP3 filename"
    )
    parser.add_argument(
        "-v", "--voice",
        default="male_us_professional",
        help="Voice option"
    )
    parser.add_argument(
        "-r", "--rate",
        default="0%",
        help="Speech rate: -100%% to +200%% (default: 0%%)"
    )
    parser.add_argument(
        "-p", "--pitch",
        default="0%",
        help="Pitch: -50%% to +50%% (default: 0%%)"
    )
    parser.add_argument(
        "--volume",
        default="100%",
        help="Volume: 0%% to 200%% (default: 100%%)"
    )
    parser.add_argument(
        "-t", "--text",
        help="Text to convert (SSML tags will be stripped)"
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="Show supported speech control options"
    )
    
    args = parser.parse_args()
    
    # Show examples if requested
    if args.examples:
        show_ssml_examples()
        return
    
    # Get text from file or command line
    if args.input:
        text = read_text_file(args.input)
        if text is None:
            return
    elif args.text:
        text = args.text
    else:
        # Default example text
        text = """Welcome to today's training.
Today we'll cover edge infrastructure automation.
Let's get started."""
        print(f"No input specified. Using example text.")
    
    # Generate audio
    await text_to_speech_ssml(
        text, 
        args.output, 
        args.voice,
        args.rate,
        args.pitch,
        args.volume
    )

if __name__ == "__main__":
    asyncio.run(main())
