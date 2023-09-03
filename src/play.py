import pyaudio
import threading

class Player:
    def __init__(self, device, dataprovider):
        self.device = device
        self.dataprovider = dataprovider
        self.playing_thread = None  # Thread for playing audio
        self.is_playing = False  # Flag to track whether audio is playing

    def play(self):
        if not self.is_playing:
            self.playing_thread = threading.Thread(target=self._play_audio)
            self.playing_thread.start()
            self.is_playing = True

    def stop(self):
        if self.is_playing:
            self.is_playing = False
            self.playing_thread.join()  # Wait for the playing thread to finish
        self.dataprovider.cleanup()  # Clean up the data provider
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

    def _play_audio(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=2,
            rate=44100,
            output=True,
            output_device_index=self.device
        )
        self.dataprovider.start()

        try:
            data = next(self.dataprovider.data)
            while data and self.is_playing:
                self.stream.write(data)
                data = next(self.dataprovider.data)
        except StopIteration:
            self.is_playing = False
            self.stop()
