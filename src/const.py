from src.SoundProviders.FFmpegStream import FFmpegStream
from src.SoundProviders.Youtube import Youtube

available_backends = {'ffmpeg': FFmpegStream, 'yt': Youtube}