import time

import pyaudio
import subprocess

# Define the FFmpeg command to receive and decode the UDP stream
from src.SoundProviders.FFmpegStream import FFmpegStream
from src.play import Player

ffmpeg_command = [
    'ffmpeg',
    '-i', 'https://rr5---sn-h0jeenl6.googlevideo.com/videoplayback?expire=1693717309&ei=3b7zZML4HYHd-gbIj5zYCw&ip=2a02%3A8070%3A9989%3A8d80%3Ad81%3A9667%3A7be1%3A8cdc&id=o-AEGQZJTe-W_LzpYMEOHPDlkFEvlxQplF02-8LP-q9TBy&itag=251&source=youtube&requiressl=yes&mh=HV&mm=31%2C26&mn=sn-h0jeenl6%2Csn-4g5lznez&ms=au%2Conr&mv=m&mvi=5&pl=49&initcwndbps=1695000&spc=UWF9f1GYMC2pRd5JaH2VW-VhR7k7I-c&vprv=1&svpuc=1&mime=audio%2Fwebm&gir=yes&clen=5240428&dur=294.881&lmt=1665403012353168&mt=1693695214&fvip=4&keepalive=yes&fexp=24007246%2C24363393&c=ANDROID&txp=4532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Csvpuc%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAMy9oLWdgJ-yuB5MaXbKcmGlG_VJo2vODXfsihFG0hjcAiEA0mvjSSM5-M_aWLpM8X3X8jVAcxY7HHbhlipeSlSgQAg%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgYtOv_MXQ0uIDjssKfBskbxqdxdg0dLgTEaZ3ldxKy8QCIBqs_9VYD3O63emMVcwGlfWI-xWJboe2rm0tuYeXqODW',  # Replace with your UDP stream address and port
    '-f', 'wav',  # Output format as WAV
    '-'
]

device=8

datastream = FFmpegStream(ffmpeg_command)
player = Player(8, datastream)

player.play()

