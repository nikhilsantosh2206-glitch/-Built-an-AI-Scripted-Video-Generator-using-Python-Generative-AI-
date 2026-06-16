from moviepy.editor import *

audio = AudioFileClip("assets/audio/voice.mp3")

clip = ColorClip(
    size=(1280, 720),
    color=(0, 0, 0),
    duration=audio.duration
)

video = clip.set_audio(audio)

video.write_videofile(
    "output/audio_test.mp4",
    fps=24,
    codec="libx264",
    audio_codec="aac"
)

print("Done! Check output/audio_test.mp4")
