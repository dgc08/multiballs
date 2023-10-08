import subprocess
from src.utils import get_project_root, Singleton


class FFmpegStream:
    stream_not_started = True

    def __init__(self, arg, *ffmpeg_args):
        self.params = [get_project_root() + 'bin/ffmpeg.exe','-i',arg, '-f', 'wav', "-ar", "48000", *ffmpeg_args, '-']
        if Singleton.get_instance().get_value("verbose"):
            print("FFmpegStream Params:", self.params)
            print("--------------------------------------------------")
        self.data = self.__data_provider()

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
