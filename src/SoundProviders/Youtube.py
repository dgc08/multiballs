from src.SoundProviders.FFmpegStream import FFmpegStream
from src.utils import get_command_output


class Youtube (FFmpegStream):
    @staticmethod
    def get_by_argument(arg):
        command = f"yt-dlp -f 251 -g {arg} --no-warnings"
        web_resource = get_command_output(command)
        return FFmpegStream.get_by_argument(web_resource)