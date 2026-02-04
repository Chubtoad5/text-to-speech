# SSML Quick Reference Guide

## Pauses and Breaks

### Time-based pauses:
<break time="500ms"/>     - Half second pause
<break time="1s"/>        - 1 second pause
<break time="2s"/>        - 2 second pause

### Strength-based pauses:
<break strength="weak"/>      - Comma-like pause (~250ms)
<break strength="medium"/>    - Period-like pause (~500ms)
<break strength="strong"/>    - Paragraph break (~750ms)
<break strength="x-strong"/>  - Long pause (~1s)

## Emphasis

<emphasis level="strong">critical point</emphasis>     - Strong emphasis
<emphasis level="moderate">important</emphasis>        - Moderate emphasis  
<emphasis level="reduced">less important</emphasis>    - De-emphasize

## Speech Rate & Timing

### Rate (speed):
<prosody rate="x-slow">very slow</prosody>      - 50% speed
<prosody rate="slow">slower</prosody>           - 75% speed
<prosody rate="medium">normal</prosody>         - 100% speed (default)
<prosody rate="fast">faster</prosody>           - 125% speed
<prosody rate="x-fast">very fast</prosody>      - 150% speed

### Percentage-based:
<prosody rate="50%">half speed</prosody>
<prosody rate="150%">1.5x speed</prosody>
<prosody rate="200%">double speed</prosody>

Can use negative values:
<prosody rate="-20%">20% slower</prosody>
<prosody rate="+30%">30% faster</prosody>

## Pitch Control

<prosody pitch="x-low">very low</prosody>
<prosody pitch="low">lower pitch</prosody>
<prosody pitch="medium">normal pitch</prosody>
<prosody pitch="high">higher pitch</prosody>
<prosody pitch="x-high">very high</prosody>

### Percentage/semitone adjustments:
<prosody pitch="+10%">slightly higher</prosody>
<prosody pitch="-10%">slightly lower</prosody>
<prosody pitch="+2st">up 2 semitones</prosody>

## Volume Control

<prosody volume="silent">silent</prosody>
<prosody volume="x-soft">very quiet</prosody>
<prosody volume="soft">quiet</prosody>
<prosody volume="medium">normal volume</prosody>
<prosody volume="loud">loud</prosody>
<prosody volume="x-loud">very loud</prosody>

### Percentage-based:
<prosody volume="50%">half volume</prosody>
<prosody volume="150%">1.5x volume</prosody>

## Pronunciation & Say-As

### Spell out text:
<say-as interpret-as="spell-out">API</say-as>
Result: "A P I"

### Numbers as digits:
<say-as interpret-as="digits">123</say-as>
Result: "one two three"

### Numbers as cardinal:
<say-as interpret-as="cardinal">123</say-as>
Result: "one hundred twenty three"

### Numbers as ordinal:
<say-as interpret-as="ordinal">1</say-as>
Result: "first"

### Dates:
<say-as interpret-as="date" format="mdy">3/15/2024</say-as>
<say-as interpret-as="date" format="dmy">15/3/2024</say-as>
<say-as interpret-as="date" format="ymd">2024/3/15</say-as>

### Telephone numbers:
<say-as interpret-as="telephone">555-1234</say-as>

### Time:
<say-as interpret-as="time">2:30pm</say-as>

### Currency:
<say-as interpret-as="currency">$50.25</say-as>

## Substitution

Say one thing while text shows another:
<sub alias="World Wide Web Consortium">W3C</sub>
<sub alias="Application Programming Interface">API</sub>
<sub alias="Kubernetes">K8s</sub>

## Phonetic Pronunciation (IPA)

<phoneme alphabet="ipa" ph="təˈmeɪtoʊ">tomato</phoneme>
<phoneme alphabet="ipa" ph="ˈdætə">data</phoneme>

## Combining Multiple Controls

<prosody rate="90%" pitch="+5%" volume="110%">
  This text will be slightly slower, higher-pitched, and louder.
</prosody>

<prosody rate="slow">
  <emphasis level="strong">Important:</emphasis>
  <break time="500ms"/>
  This section is critical.
</prosody>

## Practical Examples for Training

### Technical term pronunciation:
We'll use <say-as interpret-as="spell-out">REST</say-as> <say-as interpret-as="spell-out">API</say-as>s.

### Emphasizing key points:
The <emphasis level="strong">three pillars</emphasis> are:
<break strength="weak"/> security,
<break strength="weak"/> scalability,
<break strength="weak"/> and reliability.

### Pacing for clarity:
<prosody rate="slow">
Let me repeat that important concept.
</prosody>

### Creating natural pauses:
First, we configure the network. <break time="800ms"/>
Then, we deploy the containers. <break time="800ms"/>
Finally, we verify the setup.

### Spelling acronyms:
<say-as interpret-as="spell-out">AWS</say-as> provides infrastructure as a service.

## Command-Line Usage Examples

### Basic with SSML file:
python text_to_speech_ssml.py -i script.txt -o output.mp3

### Adjust global speech rate (20% faster):
python text_to_speech_ssml.py -i script.txt -o output.mp3 -r "+20%"

### Slower pace with lower pitch:
python text_to_speech_ssml.py -i script.txt -o output.mp3 -r "-10%" -p "-5%"

### Different voice:
python text_to_speech_ssml.py -i script.txt -o output.mp3 -v female_us_professional

### Quick inline text with SSML:
python text_to_speech_ssml.py -t "Hello <break time='1s'/> world" -o test.mp3

## Tips for Training Content

1. Use breaks between major sections (1-2 seconds)
2. Use emphasis for key concepts
3. Slow down for complex technical terms
4. Spell out acronyms on first use
5. Add pauses after questions to let them sink in
6. Use moderate pacing (90-95%) for technical content
7. Add strong breaks before/after code examples or demos
