#!/usr/bin/python

import subprocess, time
import threading

# use threading.Timer for SpotifyReloader
#  and stop writing in the sleep yourself.
# otherwise, InputThread should gain the functionality of skipping
#  (and subsequently cancelling and recreating a SpotifyReloader thread)
#  pausing, playing, and printing song details.

class SpotifyReloader(threading.Thread):
    def run(self):
        while True:
            result = subprocess.check_output(["osascript", "./reloadSpotify.osascript"])
            result = str(result.decode("utf-8")).strip()
            time.sleep(float(result))

class InputThread(threading.Thread):
    def run(self):
        quit = False
        while quit != True:
            response = input("instruction: ")
            print(f"you said {response}")
            if response == "quit":
                quit = True

if __name__ == "__main__":
    spot_t = SpotifyReloader()
    spot_t.start()
    in_t = InputThread()
    in_t.start()
    
