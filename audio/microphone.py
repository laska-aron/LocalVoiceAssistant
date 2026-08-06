from __future__ import annotations

import queue
from dataclasses import dataclass

import sounddevice as sd

import time

@dataclass
class AudioDevice:
    index: int
    name: str
    channels: int
    samplerate: int


class MicrophoneManager:

    def __init__(self) -> None:
        self.devices: list[AudioDevice] = []

        self.queue = queue.Queue()
        self.stream = None


    def scan(self) -> list[AudioDevice]:

        self.devices.clear()

        for index, device in enumerate(sd.query_devices()):

            if device["max_input_channels"] <= 0:
                continue

            self.devices.append(
                AudioDevice(
                    index=index,
                    name=device["name"],
                    channels=device["max_input_channels"],
                    samplerate=int(device["default_samplerate"])
                )
            )

        return self.devices


    def _callback(self, indata, frames, time, status):

        if status:
            print(status)

        self.queue.put(
            bytes(indata)
        )


    def start(self, device=None):

        self.stream = sd.RawInputStream(

            samplerate=16000,

            blocksize=8000,

            device=device,

            dtype="int16",

            channels=1,

            callback=self._callback
        )

        self.stream.start()


    def read(self):

        return self.queue.get()


    def stop(self):

        if self.stream:

            self.stream.stop()
            self.stream.close()

    def pause(self):

        if self.stream:

            self.stream.stop()


    def resume(self):

        if self.stream:

            self.stream.start()

            time.sleep(0.1)