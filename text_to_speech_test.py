from gtts import gTTS
import io
import pygame

def speak_text(text):
    # Convert text to speech in Nepali
    tts = gTTS(text=text, lang='ne')
    # Save audio to an in-memory file
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)

    # start pygame mixer
    pygame.mixer.init()

    # get sound from the in-memory file
    pygame.mixer.music.load(mp3_fp, 'mp3')

    # play the sound
    pygame.mixer.music.play()

    # wait for audio end
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)