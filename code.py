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
WAS_PRESSED = True
octave_up_button_state = None
octave_down_button_state = None

# Pressing the button for next track
octave_up_button = digitalio.DigitalInOut(board.GP11)
octave_up_button.direction = digitalio.Direction.INPUT
octave_up_button.pull = digitalio.Pull.UP

# Pressing the button for previous track
octave_down_button = digitalio.DigitalInOut(board.GP12)
octave_down_button.direction = digitalio.Direction.INPUT
octave_down_button.pull = digitalio.Pull.UP



#  MIDI setup as MIDI out device
midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0)

#  button pins, all pins in order skipping GP15
note_pins = [board.GP16, board.GP17, board.GP18, board.GP19, board.GP20, board.GP21,
             board.GP22, board.GP26, board.GP27, board.GP28, board.GP2, board.GP1, board.GP0]

note_buttons = []
note_states = []
#  default midi number
midi_num = 60
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
    for i in range(len(midi_notes)):
        buttons = note_buttons[i]
        #  if button is pressed...
        if not buttons.value and note_states[i] is False:
            #  send the MIDI note and light up the LED
            midi.send(NoteOn(midi_notes[i], 120))
            note_states[i] = True
            #print("Button pressed")
            #print_midi_notes()
        #  if the button is released...
        if buttons.value and note_states[i] is True:
            #  stop sending the MIDI note and turn off the LED
            midi.send(NoteOff(midi_notes[i], 120))
            note_states[i] = False
            #print("Button released")
            #print_midi_notes()
            

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
    new_notes = midi_notes
    
    if (current_midi_num + val >= 21) and (current_midi_num + val + len(midi_notes) - 1 <= 127):
        #print(val)
        current_midi_num += val
        for i in range(len(new_notes)):
            midi.send(NoteOff(midi_notes[i], 120))
            note_states[i] = False      
            midi_notes[i] = new_notes[i] + val
    #print_midi_notes()


def reset_midi_note():
    global encoder_button_state
    global current_midi_num
    
    is_pressed = not encoder_button.value
    if is_pressed and encoder_button_state is None:
        encoder_button_state = WAS_PRESSED
    is_released = encoder_button.value
    if encoder_button_state == WAS_PRESSED and is_released:
        counter = 0
        for i in range(len(midi_notes)):
            midi_notes[i] = (midi_num + counter)
            counter += 1
        current_midi_num = midi_num
        encoder_button_state = None

def print_midi_notes():
    print(midi_notes)
    
def octave_up():
    global octave_up_button_state
    
    is_pressed = not octave_up_button.value
    if is_pressed and octave_up_button_state is None:
        octave_up_button_state = WAS_PRESSED
    is_released = octave_up_button.value
    if octave_up_button_state == WAS_PRESSED and is_released:
        change_register(12)
        octave_up_button_state = None

def octave_down():
    global octave_down_button_state
    
    is_pressed = not octave_down_button.value
    if is_pressed and octave_down_button_state is None:
        octave_down_button_state = WAS_PRESSED
    is_released = octave_down_button.value
    if octave_down_button_state == WAS_PRESSED and is_released:
        change_register(-12)
        octave_down_button_state = None

while True:
    midi_input()
    change_register_with_rotation()
    reset_midi_note()
    octave_up()
    octave_down()
    
            

