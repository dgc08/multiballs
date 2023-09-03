import subprocess


class FFmpegStream:
    stream_not_started = True

    def __init__(self, params):
        self.params = params
        self.data = self.__data_provider()

    @staticmethod
    def get_by_argument(arg):
        return FFmpegStream(['ffmpeg','-i',arg, '-f', 'wav', '-'])

    def start(self):
        self.ffmpeg_process = subprocess.Popen(self.params, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                              bufsize=1024)

    def __data_provider(self):
        data = self.ffmpeg_process.stdout.read(1024)
        while data:
            yield data
            data = self.ffmpeg_process.stdout.read(1024)


    def cleanup(self):
        self.ffmpeg_process.kill()
