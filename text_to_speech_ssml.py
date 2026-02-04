#!/usr/bin/env python3
"""
Text-to-Speech with SSML Support
Control pronunciation, pacing, pauses, emphasis, and more
"""

import asyncio
import edge_tts
import argparse
import os

# Popular natural-sounding voices
VOICE_OPTIONS = {
    "male_us_professional": "en-US-GuyNeural",
    "female_us_professional": "en-US-JennyNeural",
    "male_us_casual": "en-US-ChristopherNeural",
    "female_us_casual": "en-US-AriaNeural",
}

def apply_prosody(text, rate="0%", pitch="0%", volume="100%"):
    """
    Wrap text in prosody tags if non-default values are specified.

    Args:
        text (str): Plain text or text with inline SSML tags
        rate (str): Speech rate (-100% to +200%, default 0%)
        pitch (str): Pitch adjustment (-50% to +50%, default 0%)
        volume (str): Volume level (0% to 200%, default 100%)

    Returns:
        str: Text optionally wrapped in prosody tags
    """
    # Only wrap in prosody if non-default values are specified
    if rate != "0%" or pitch != "0%" or volume != "100%":
        return f'<prosody rate="{rate}" pitch="{pitch}" volume="{volume}">{text}</prosody>'
    return text

async def text_to_speech_ssml(text, output_filename="output.mp3", voice="male_us_professional", 
                               rate="0%", pitch="0%", volume="100%", use_ssml=True):
    """
    Convert text to speech using Edge TTS with SSML support
    
    Args:
        text (str): The text to convert (can include SSML tags)
        output_filename (str): Name of the output MP3 file
        voice (str): Voice option key from VOICE_OPTIONS or full voice name
        rate (str): Speech rate adjustment
        pitch (str): Pitch adjustment
        volume (str): Volume adjustment
        use_ssml (bool): Whether to wrap in SSML (if not already SSML)
    """
    try:
        # Get the voice name
        if voice in VOICE_OPTIONS:
            voice_name = VOICE_OPTIONS[voice]
        elif voice.endswith("Neural") or "-" in voice:
            voice_name = voice
        else:
            voice_name = VOICE_OPTIONS["male_us_professional"]
        
        # Apply prosody settings if needed (edge_tts supports inline SSML tags)
        if use_ssml:
            ssml_text = apply_prosody(text, rate, pitch, volume)
        else:
            ssml_text = text

        # Create TTS communicator with voice parameter
        # edge_tts handles voice selection and supports inline SSML tags like <break/>, <emphasis>, etc.
        communicate = edge_tts.Communicate(ssml_text, voice_name)
        
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
    """Display SSML examples and documentation"""
    examples = """
=== SSML CONTROL EXAMPLES ===

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
"""
    print(examples)

async def main():
    parser = argparse.ArgumentParser(
        description="Convert text to speech with SSML control"
    )
    parser.add_argument(
        "-i", "--input",
        help="Input text file (can contain SSML tags)"
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
        help="Text to convert (can include SSML tags)"
    )
    parser.add_argument(
        "--examples",
        action="store_true",
        help="Show SSML examples and documentation"
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
        # Default example with SSML
        text = """Welcome to today's training. <break time="1s"/>
Today we'll cover <emphasis level="strong">edge infrastructure automation</emphasis>.
<break time="500ms"/>
Let's get started."""
        print(f"No input specified. Using example with SSML markup.")
    
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
