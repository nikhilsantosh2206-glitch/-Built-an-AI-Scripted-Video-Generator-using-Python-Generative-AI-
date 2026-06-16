import os

def generate_subtitles(script):

    os.makedirs("output", exist_ok=True)

    with open(
        "output/subtitles.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write(script)

    return script