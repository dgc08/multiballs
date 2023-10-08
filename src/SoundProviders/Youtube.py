from src.SoundProviders.FFmpegStream import FFmpegStream
from src.utils import get_command_output, get_project_root, Singleton


class Youtube (FFmpegStream):
    def __init__(self, arg, *ffmpeg_args):
        command = f"{get_project_root()}bin/yt-dlp.exe -f 251 -g {arg} --no-warnings"
        web_resource = get_command_output(command)
        if Singleton.get_instance().get_value("verbose"):
            print("Youtube (SoundProvider) yt-dlp Command:", command)
            print("web resource:", web_resource)
            print("--------------------------------------------------")
        super().__init__(web_resource, *ffmpeg_args)