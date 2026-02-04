#!/usr/bin/env python3
"""
List all available Edge TTS voices
"""

import asyncio
import edge_tts

async def list_all_voices():
    """
    Fetch and display all available Edge TTS voices
    """
    try:
        voices = await edge_tts.list_voices()
        
        # Organize by language
        voices_by_lang = {}
        for voice in voices:
            lang = voice["Locale"]
            if lang not in voices_by_lang:
                voices_by_lang[lang] = []
            voices_by_lang[lang].append(voice)
        
        # Display all voices
        print(f"\n{'='*80}")
        print(f"TOTAL VOICES AVAILABLE: {len(voices)}")
        print(f"{'='*80}\n")
        
        # Show English voices first
        english_locales = [loc for loc in sorted(voices_by_lang.keys()) if loc.startswith('en-')]
        other_locales = [loc for loc in sorted(voices_by_lang.keys()) if not loc.startswith('en-')]
        
        print("=" * 80)
        print("ENGLISH VOICES")
        print("=" * 80)
        
        for locale in english_locales:
            print(f"\n{locale} ({len(voices_by_lang[locale])} voices):")
            print("-" * 80)
            for voice in voices_by_lang[locale]:
                gender = voice.get("Gender", "Unknown")
                name = voice["ShortName"]
                display_name = voice.get("FriendlyName", voice["Name"])
                print(f"  {name:40s} | {gender:6s} | {display_name}")
        
        print("\n" + "=" * 80)
        print("OTHER LANGUAGES (showing first 10)")
        print("=" * 80)
        
        for locale in other_locales[:10]:
            print(f"\n{locale} ({len(voices_by_lang[locale])} voices):")
            print("-" * 80)
            for voice in voices_by_lang[locale]:
                gender = voice.get("Gender", "Unknown")
                name = voice["ShortName"]
                display_name = voice.get("FriendlyName", voice["Name"])
                print(f"  {name:40s} | {gender:6s} | {display_name}")
        
        if len(other_locales) > 10:
            print(f"\n... and {len(other_locales) - 10} more language groups")
        
        # Save to file for reference
        with open("all_voices.txt", "w", encoding="utf-8") as f:
            f.write(f"Total voices: {len(voices)}\n\n")
            for locale in sorted(voices_by_lang.keys()):
                f.write(f"\n{locale} ({len(voices_by_lang[locale])} voices):\n")
                f.write("-" * 80 + "\n")
                for voice in voices_by_lang[locale]:
                    gender = voice.get("Gender", "Unknown")
                    name = voice["ShortName"]
                    display_name = voice.get("FriendlyName", voice["Name"])
                    f.write(f"  {name:40s} | {gender:6s} | {display_name}\n")
        
        print(f"\n{'='*80}")
        print(f"✓ Complete list saved to: all_voices.txt")
        print(f"{'='*80}\n")
        
    except Exception as e:
        print(f"Error fetching voices: {e}")

if __name__ == "__main__":
    asyncio.run(list_all_voices())
