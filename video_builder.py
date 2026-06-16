from moviepy.editor import *
from image_generator import get_images

def create_video(script_text, audio_file):

    audio = AudioFileClip(audio_file)
    images = get_images()

    duration_per_image = audio.duration / len(images)

    clips = []

    for img in images:
        clip = (
            ImageClip(img)
            .resize(width=1280)
            .set_duration(duration_per_image)
        )
        clips.append(clip)

    video = concatenate_videoclips(
        clips,
        method="compose"
    )

    video = video.set_audio(audio)

    video.write_videofile(
        "output/final_video.mp4",
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )