import json
import threading
import time
import socket as sock

import pystray
from PIL import Image

from src.Player import Player
from src.const import available_backends
from src.utils import get_project_root

class Server:
    def __init__(self):
        self.server_running = False
        self.players = []

    def run_server(self):
        self.server_running = True

        image = Image.open(get_project_root() + 'assets/icon.png')  # Replace 'icon.png' with your icon image
        menu = (
            pystray.MenuItem('Exit', self.exit_program),
            pystray.MenuItem('Stop all', self.stop_all),
        )

        self.icon = pystray.Icon('MultiBalls Server', image, 'Soundboard / Music Player', menu)

        # Start the background thread
        self.background_thread = threading.Thread(target=self.__server)
        self.background_thread.daemon = True
        self.background_thread.start()

        # Start the icon and run the program

        self.main_thread = threading.Thread(target=self.icon.run)
        self.main_thread.daemon = True
        self.main_thread.start()
        try:
            # Keep the main script alive
            while self.server_running:
                time.sleep(0.5)
        except KeyboardInterrupt:
            # Handle CTRL-C by setting the server_running flag to False
            self.server_running = False
            self.exit_program(self.icon, None)

    def exit_program(self, icon=None, item=None):
        self.server_running = False  # Terminate the server
        self.icon.stop()
        try:
            self.main_thread.join()
        except RuntimeError:
            pass
        exit(0)

    def __server(self):
        HOST = '127.0.0.1'
        PORT = 47434

        # Use the renamed module name
        with sock.socket(sock.AF_INET, sock.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()

            while self.server_running:
                conn, addr = s.accept()

                with conn:
                    data = conn.recv(1024)

                    if not data:
                        break

                    instruction = data.decode('utf-8')

                    self.play(instruction)
            s.close()


            """datastream = FFmpegStream(
                    "C:\Library\cache\change\SymphonicSuite [AoT] Part2-2nd：ShingekiNoKyojin [YAiSUQGXcew].webm")

                self.player = Player(datastream, 8)

                background_thread = threading.Thread(target=self.player.play)
                background_thread.daemon = True
                background_thread.start()"""

    def play(self, instruction):
        # Implement your logic for handling the received instruction here
        # You can replace this with your actual logic
        data = json.loads(instruction)
        print(f"Received instruction: {data}")

        if data["command"] == "play":
            self.players.append(Player(available_backends[data["backend"]](*data["params"]), *(data["devices"])))
            self.players[-1].enable_self_deletion(self.players)
            self.players[-1].play()

    def stop_all(self,icon=None, item=None):
        for i in self.players:
            i.stop()
        self.players = []

if __name__ == "__main__":
    Server().run_server()
