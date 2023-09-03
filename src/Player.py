import pyaudio
import threading

class Player:
    def __init__(self, dataprovider, *devices):
        self.container = None
        self.devices = devices
        self.dataprovider = dataprovider
        self.playing_thread = None  # Thread for playing audio
        self.is_playing = None  # Flag to track whether audio is playing

    def play(self):
        if not self.is_playing:
            self.playing_thread = threading.Thread(target=self._play_audio)
            self.playing_thread.start()
            self.is_playing = True

    def enable_self_deletion(self, container):
        self.container = container

    def stop(self):
        if self.is_playing:
            self.is_playing = False
            self.playing_thread.join()  # Wait for the playing thread to finish
        self.dataprovider.cleanup()  # Clean up the data provider
        for i in self.streams:
            i.stop_stream()
            i.close()
        self.p.terminate()
        if self.container is not None:
            self.container.remove(self)
        del self

    def _play_audio(self):
        self.p = pyaudio.PyAudio()
        self.streams = []
        for i in self.devices:
            self.streams.append(self.p.open(
                format=pyaudio.paInt16,
                channels=2,
                rate=48000,
                output=True,
                output_device_index=i
                )

            )

        self.dataprovider.start()

        try:
            data = next(self.dataprovider.data)
            while data and self.is_playing:
                for i in self.streams:
                    i.write(data)
                data = next(self.dataprovider.data)
        except StopIteration:
            self.is_playing = False
            self.stop()
