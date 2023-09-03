# Define the FFmpeg command to receive and decode the UDP stream
from src.SoundProviders.FFmpegStream import FFmpegStream
from src.SoundProviders.Youtube import Youtube
from src.play import Player

device=8

#datastream = Youtube.get_by_argument("https://www.youtube.com/watch?v=9HuSvo6qQ-E")
datastream = FFmpegStream.get_by_argument("C:\Library\cache\change\SymphonicSuite [AoT] Part2-2nd：ShingekiNoKyojin [YAiSUQGXcew].webm")


player = Player(device, datastream)

player.play()

