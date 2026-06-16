import edge_tts
import asyncio

async def generate_voice_async(text, output_file):
    communicate = edge_tts.Communicate(
        text,
        "en-US-ChristopherNeural"
    )
    await communicate.save(output_file)

def text_to_speech(text):

    output_file = "assets/audio/voice.mp3"

    asyncio.run(
        generate_voice_async(
            text,
            output_file
        )
    )

    return output_file