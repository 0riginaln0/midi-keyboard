import time
import board
import digitalio
import usb_midi
import adafruit_midi
import rotaryio
from adafruit_midi.note_on      import NoteOn
from adafruit_midi.note_off     import NoteOff


# Encoder rotation
encoder_dt = board.GP14
encoder_clk = board.GP13
encoder = rotaryio.IncrementalEncoder(encoder_clk, encoder_dt)
# Pressing the encoder
sw = board.GP15
encoder_button = digitalio.DigitalInOut(sw)
encoder_button.direction = digitalio.Direction.INPUT
encoder_button.pull = digitalio.Pull.UP

# Global variables
encoder_last_position = 0
encoder_button_state = None
# Global constants, States
DOUBLE_TAP_TIME_LIMIT = 0.5 # in seconds
WAS_PRESSED = True


#  MIDI setup as MIDI out device
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

#  button pins, all pins in order skipping GP15
note_pins = [board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21,
             board.GP22, board.GP26, board.GP27, board.GP28, board.GP2, board.GP1, board.GP0]

note_buttons = []
note_states = []
#  default midi number
midi_num = 40
current_midi_num = midi_num
#  array of default MIDI notes
midi_notes = []
for pin in note_pins:
    note_pin = digitalio.DigitalInOut(pin)
    note_pin.direction = digitalio.Direction.INPUT
    note_pin.pull = digitalio.Pull.UP
    note_buttons.append(note_pin)
    note_pressed = False
    note_states.append(note_pressed)
    midi_notes.append(midi_num + len(note_states) - 1)


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

def change_register_with_rotation():
    global encoder_last_position
    global current_position
    
    current_position = encoder.position
    position_change = current_position - encoder_last_position
    # Clockwise rotation
    if position_change > 0:
        for _ in range(position_change):
            change_register(1)
    # Counterclockwise rotation
    elif position_change < 0:
        for _ in range(-position_change):
            change_register(-1)            
    encoder_last_position = current_position


def change_register(val: int):
    global current_midi_num
    
    if (current_midi_num + val > 27) and (current_midi_num + val < 89):
        print(val)
        current_midi_num += val
        for note in midi_notes:
            note += val
        print(current_midi_num)
        
def reset_midi_note():
    global encoder_button_state
    global current_midi_num
    
    is_pressed = not encoder_button.value
    if is_pressed and encoder_button_state is None:
        encoder_button_state = WAS_PRESSED
    is_released = encoder_button.value
    if encoder_button_state == WAS_PRESSED and is_released:
        counter = 0
        for note in midi_notes:
            note = (midi_num + counter)
            counter += 1
        current_midi_num = midi_num
        encoder_button_state = None

while True:
    midi_input()
    change_register_with_rotation()
    reset_midi_note()
            
