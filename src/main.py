import argparse
import json
import socket
import subprocess
import sys

import pyaudio

from src.Player import Player
from src.const import available_backends
from src.server import Server
from src.utils import get_device_name_by_number, get_project_root

"""
device=8
#datastream = Youtube("https://www.youtube.com/watch?v=9HuSvo6qQ-E")
datastream = FFmpegStream("C:\Library\cache\change\SymphonicSuite [AoT] Part2-2nd：ShingekiNoKyojin [YAiSUQGXcew].webm")


player = Player(device, datastream)

player.play()
"""


default_backend = 'ffmpeg'


def main():
    parser = argparse.ArgumentParser(description="MultiBalls © Sinthoras39, 2023 MIT License")

    # Add the arguments
    parser.add_argument('-s', '--server', action='store_true', help='Start the Server as Daemon')
    parser.add_argument('-sn', '--server-no-daemon', action='store_true', help='Start the Server without Daemon')
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose Output')
    parser.add_argument('-cp', '--client-play', action='store_true', help='Play on CLient instead of Server')
    parser.add_argument('-b', '--backend', choices=available_backends.keys(), default=default_backend,
                        help='Specify Backend (ffmpeg or youtube)')
    parser.add_argument('-d', '--devices', type=str, default="8", help='List of device numbers')
    parser.add_argument('--list-devices', action='store_true', help='List all available devices')
    parser.add_argument('expression', nargs='?', default=None, help='Thing to play')

    # Parse the command-line arguments
    args, unknown_args = parser.parse_known_args()

    if args.server_no_daemon:
        print("Starting Server, stop with CTRL-C...")
        Server().run_server()
        print("Exited Gracefully.")
        return
    if args.server:
        print("Starting Server as Daemon...")
        subprocess.Popen([sys.executable, get_project_root() + 'src/server.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE, shell=True)
        print("Done.")
        return

    # Device Handling
    devices = args.devices.split(",")
    for i in range(len(devices)):
        devices[i] = int(devices[i])
    if args.verbose:
        p = pyaudio.PyAudio()
        print("Selected Devices:")
        for i in devices:
            print(f"{i}: {get_device_name_by_number(i, p)}")

    if args.list_devices:
        if not args.verbose:
            p = pyaudio.PyAudio()
        for i in range(p.get_device_count()):
            device_info = p.get_device_info_by_index(i)
            if device_info['name'].startswith(p.get_device_info_by_index(1)['name']) and i != 1:
                break
            print(f"Device {i}: {device_info['name']}")
        return
    elif args.expression is None:
        print("You must provide input to the Backend ('Thing to do', e.g. a filename)")
        return

    # Access the parsed arguments
    if args.verbose:
        print(f"Selected Backend: {args.backend}")

    if args.verbose:
        print(f"Thing to do: {args.expression}")

    if args.client_play:
        player = Player(available_backends[args.backend](args.expression, *unknown_args), *devices)
        player.play()
        return

    HOST = '127.0.0.1'  # Replace with the server's IP address or hostname
    PORT = 47434  # Replace with the server's port number
    data = {"command":"play","backend":args.backend, "params": [args.expression, *unknown_args], "devices":devices}

    # Create a socket and connect to the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Prepare the data to be sent
        data_json = json.dumps(data)

        # Encode the data and send it to the server
        s.sendall(data_json.encode('utf-8'))


if __name__ == "__main__":
    main()
