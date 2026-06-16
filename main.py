from script_generator import generate_script
from voice_generator import text_to_speech
from subtitle_generator import generate_subtitles
from video_builder import create_video

topic = input("Enter video topic: ")

print("Generating script...")
script = generate_script(topic)

print(script)

print("Generating voice...")
audio_file = text_to_speech(script)

print("Generating subtitles...")
generate_subtitles(script)

print("Creating video...")
create_video(script, audio_file)

print("\nDone!")
print("Video saved at:")
print("output/final_video.mp4")