import time

import serial
import pygame.midi

NOTES = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71] # MIDI note numbers for each channel
SERIAL_PORT = "COM7" # path to the serial port used by the Arduino
MIDI_OUTPUT = 3 # index of the MIDI output device to use - loopMIDI port
CHANNEL_COUNT = 12 # number of capacitive touch channels

port = serial.Serial(SERIAL_PORT, 9600)

try:
    pygame.midi.init()
    player = pygame.midi.Output(MIDI_OUTPUT)
    print(pygame.midi.get_device_info(3))
    previous_state = 0
    while True:
        line = port.readline().decode("utf-8")
        print(line)
        print("here")
        try:
            state = int(line.strip("\r\n"))
            print(state)
        except ValueError:
            print("error")
            continue # ignore bad lines
        for i in range(CHANNEL_COUNT):
            if (state >> i) & 1 != (previous_state >> i) & 1:
                print(state)
                if (state >> i) & 1:
                    player.note_on(NOTES[i], 127)
                    print(NOTES[i])
                else:
                    player.note_off(NOTES[i], 127)
        previous_state = state
except KeyboardInterrupt:
    del player
    pygame.midi.quit()
