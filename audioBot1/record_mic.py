import sounddevice as sd
import wavio


def record_audio(duration, filename, fs=16000):
    """
    Record audio from the microphone and save it as a .wav file.

    Parameters:
    - duration: The duration of the recording in seconds.
    - filename: The name of the .wav file to save.
    - fs: The sampling rate (default 44100 Hz).
    """

    print(f"Recording for {duration} seconds...")

    # Record audio
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished

    # Save as a .wav file
    wavio.write(filename, recording, fs, sampwidth=2)
    print(f"Recording saved as '{filename}'")


# Example usage
duration = 5  # seconds
filename = "output.wav"

record_audio(duration, filename)
