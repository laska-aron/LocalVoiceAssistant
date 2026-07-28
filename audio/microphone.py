from __future__ import annotations

from dataclasses import dataclass

import sounddevice as sd

import queue
import numpy as np
import sounddevice as sd

from dataclasses import dataclass

@dataclass(slots=True)
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

        self.queue.put(indata.copy())

    def start(self, device: int | None = None):

        self.stream = sd.InputStream(
            samplerate=16000,
            channels=1,
            dtype="int16",
            blocksize=1024,
            callback=self._callback,
            device=device,
        )

        self.stream.start()

    def stop(self):

        if self.stream is not None:
            self.stream.stop()
            self.stream.close()

    def read(self):
        return self.queue.get()