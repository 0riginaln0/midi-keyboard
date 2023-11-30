import time
import board
import digitalio
import usb_midi
import adafruit_midi
from adafruit_midi.note_on      import NoteOn
from adafruit_midi.note_off     import NoteOff

#  MIDI setup as MIDI out device
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

#  button pins, all pins in order skipping GP15
note_pins = [board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21,
             board.GP22, board.GP26, board.GP27, board.GP28, board.GP2, board.GP1, board.GP0]

note_buttons = []
note_states = []
#  default midi number
midi_num = 58
counter = 0
#  array of default MIDI notes
midi_notes = []

for pin in note_pins:
    note_pin = digitalio.DigitalInOut(pin)
    note_pin.direction = digitalio.Direction.INPUT
    note_pin.pull = digitalio.Pull.UP
    note_buttons.append(note_pin)
    note_pressed = False
    note_states.append(note_pressed)
    midi_notes.append(midi_num + counter)
    counter += 1

#  default MIDI button
button_num = 0
#  default MIDI button position
button_pos = 0


def midi_input():
    #  MIDI input
    for i in range(len(note_pins)):
        buttons = note_buttons[i]
        #  if button is pressed...
        if not buttons.value and note_states[i] is False:
            #  send the MIDI note and light up the LED
            midi.send(NoteOn(midi_notes[i], 120))
            note_states[i] = True
            print("Button pressed")
        #  if the button is released...
        if buttons.value and note_states[i] is True:
            #  stop sending the MIDI note and turn off the LED
            midi.send(NoteOff(midi_notes[i], 120))
            note_states[i] = False
            print("Button released")

while True:
    midi_input()
            
