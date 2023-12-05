import time
import board
import digitalio
import usb_midi
import adafruit_midi
import rotaryio
from adafruit_midi.note_on      import NoteOn
from adafruit_midi.note_off     import NoteOff

import busio
import lcd
import i2c_pcf8574_interface
from lcd import LCD, CursorMode
from i2c_pcf8574_interface import I2CPCF8574Interface



i2c = busio.I2C(scl=board.GP9, sda=board.GP8)
address = 0x27


i2c = i2c_pcf8574_interface.I2CPCF8574Interface(i2c, address)
lcd = lcd.LCD(i2c, num_rows=2, num_cols=16)

lcd.set_display_enabled(True)
lcd.print('kolobok povesilsya')

notes_dc = {
    93: 'A6',
    92: 'G#6/Ab6',
    91: 'G6',
    90: 'F#6/Gb6',
    89: 'F6',
    88: 'E6',
    87: 'D#6/Eb6',
    86: 'D6',
    85: 'C#6/Db6',
    84: 'C6',
    83: 'B5',
    82: 'A#5/Bb5',
    81: 'A5',
    80: 'G#5/Ab5',
    79: 'G5',
    78: 'F#5/Gb5',
    77: 'F5',
    76: 'E5',
    75: 'D#5/Eb5',
    74: 'D5',
    73: 'C#5/Db5',
    72: 'C5',
    71: 'B4',
    70: 'A#4/Bb4',
    69: 'A4',
    68: 'G#4/Ab4',
    67: 'G4',
    66: 'F#4/Gb4',
    65: 'F4',
    64: 'E4',
    63: 'D#4/Eb4',
    62: 'D4',
    61: 'C#4/Db4',
    60: 'C4',
    59: 'B3',
    58: 'A#3/Bb3',
    57: 'A3',
    56: 'G#3/Ab3',
    55: 'G3',
    54: 'F#3/Gb3',
    53: 'F3',
    52: 'E3',
    51: 'D#3/Eb3',
    50: 'D3',
    49: 'C#3/Db3',
    48: 'C3',
    47: 'B2',
    46: 'A#2/Bb2',
    45: 'A2',
    44: 'G#2/Ab2',
    43: 'G2',
    42: 'F#2/Gb2',
    41: 'F2',
    40: 'E2',
    39: 'D#2/Eb2',
    38: 'D2',
    37: 'C#2/Db2',
    36: 'C2',
    35: 'B1',
    34: 'A#1/Bb1',
    33: 'A1',
    32: 'G#1/Ab1',
    31: 'G1',
    30: 'F#1/Gb1',
    29: 'F1',
    28: 'E1',
    27: 'D#1/Eb1',
    26: 'D1',
    25: 'C#1/Db1',
    24: 'C1',
    23: 'B0',
    22: 'A#0/Bb0',
    21: 'A0',
}




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

#  button pins, all buttons in order
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
    global current_midi_num
    #  MIDI input
    for i in range(len(midi_notes)):
        buttons = note_buttons[i]
        #  if button is pressed...
        if not buttons.value and note_states[i] is False:
            #  send the MIDI note and light up the LED
            midi.send(NoteOn(midi_notes[i], 120))
            note_states[i] = True
            print(midi_notes[i])
            print(current_midi_num)
            lcd.clear()
            str1 = str(notes_dc[midi_notes[0]]) + ' ' + str(notes_dc[midi_notes[12]])
            str2 = str(notes_dc[midi_notes[i]])
            lcd.print(str1 + ' ' * (16-len(str1)) + str2 + ' ' * (16 - len(str2)))
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
    
    if (current_midi_num + val >= 21) and (current_midi_num + val + len(midi_notes) - 1 <= 93):
        #print(val)
        current_midi_num += val
        for i in range(len(new_notes)):
            midi.send(NoteOff(midi_notes[i], 120))
            note_states[i] = False
            midi_notes[i] = new_notes[i] + val
    #print_midi_notes()
    lcd.clear()
    str1 = str(notes_dc[midi_notes[0]]) +' ' + str(notes_dc[midi_notes[12]])
    lcd.print(str1 + ' ' * (16-len(str1)))


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
    
            
