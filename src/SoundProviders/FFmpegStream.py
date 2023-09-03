import subprocess


class FFmpegStream:
    stream_not_started = True

    def __init__(self, params):
        self.params = params
    def start(self):
        self.ffmpeg_process = subprocess.Popen(self.params, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                              bufsize=1024)
        self.data = self.__data_provider()


    def __data_provider(self):
        data = self.ffmpeg_process.stdout.read(1024)
        while data:
            yield data
            data = self.ffmpeg_process.stdout.read(1024)


    def cleanup(self):
        self.ffmpeg_process.kill()
