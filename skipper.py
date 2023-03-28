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
            print(result)
            time.sleep(float(result))

class InputThread(threading.Thread):
    def __init__(self):
        behavioral_dict = dict()
        behavioral_dict.update(dict.fromkeys(["quit"], (self.set_quit_true,)))
        behavioral_dict.update(dict.fromkeys(["reload"], (SpotifyReloader().start,)))
        self.switch = behavioral_dict
        self.quit = False
        threading.Thread.__init__(self)

    def run(self):
        while self.quit != True:
            response = input("instruction: ")
            requested_behavior = self.switch[response] if response in self.switch else None
            if requested_behavior == None:
                print(f"{response} isn't a valid response")
            else:
                requested_fn = requested_behavior[0]
                requested_params = requested_behavior[1:]
                requested_fn(*requested_params)

    def set_quit_true(self):
        self.quit = True

if __name__ == "__main__":

    spot_t = SpotifyReloader()
    spot_t.setDaemon(True)
    spot_t.start()
    in_t = InputThread()
    in_t.start()
