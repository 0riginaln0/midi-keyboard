# midi-keyboard
MIDI Keyboard based on Raspberry Pi Pico

13 note-buttons (range between low and high tonic inclusive)

2 buttons for changing register 1 octave up or down

1 encoder:

- clockwise/anticlockwise rotation = changing register 1 semitone up/down
  
- push = reset to default register

Outputs the current register boundaries to the display

Demo

[![Watch the video](https://img.youtube.com/vi/tdJX2ajELcE/0.jpg)](https://www.youtube.com/watch?v=tdJX2ajELcE)

Scheme
https://wokwi.com/projects/382935883407822849

![image](https://github.com/user-attachments/assets/8a770697-b474-4c50-9a9b-c265732d720c)



```json
{
  "version": 1,
  "author": "Anonymous maker",
  "editor": "wokwi",
  "parts": [
    { "type": "wokwi-breadboard", "id": "bb1", "top": -89.4, "left": -218, "attrs": {} },
    { "type": "wokwi-breadboard-half", "id": "bb2", "top": -310.2, "left": -35.6, "attrs": {} },
    {
      "type": "wokwi-pi-pico",
      "id": "pico",
      "top": -306.5,
      "left": 142.05,
      "rotate": 90,
      "attrs": {}
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn1",
      "top": -0.1,
      "left": -217.3,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn2",
      "top": -19.3,
      "left": -169.3,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn3",
      "top": -0.1,
      "left": -121.3,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn4",
      "top": -19.3,
      "left": -73.3,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn5",
      "top": -0.1,
      "left": -25.3,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn6",
      "top": -0.1,
      "left": 22.7,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn7",
      "top": -19.3,
      "left": 70.7,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn8",
      "top": -0.1,
      "left": 118.7,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn9",
      "top": -19.3,
      "left": 166.7,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn10",
      "top": -0.1,
      "left": 214.7,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn11",
      "top": -19.3,
      "left": 262.7,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn12",
      "top": -0.1,
      "left": 310.7,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn13",
      "top": -0.1,
      "left": 358.7,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-ky-040",
      "id": "encoder1",
      "top": -352.2,
      "left": -56.3,
      "rotate": 90,
      "attrs": {}
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn14",
      "top": -220.9,
      "left": 13.1,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-pushbutton",
      "id": "btn15",
      "top": -220.9,
      "left": -34.9,
      "rotate": 90,
      "attrs": { "color": "green" }
    },
    {
      "type": "wokwi-lcd1602",
      "id": "lcd1",
      "top": -550.4,
      "left": 255.2,
      "attrs": { "pins": "i2c" }
    }
  ],
  "connections": [
    [ "pico:GP0", "$serialMonitor:RX", "", [] ],
    [ "pico:GP1", "$serialMonitor:TX", "", [] ],
    [ "btn10:1.l", "bb1:tn.39", "black", [ "v0" ] ],
    [ "btn12:1.l", "bb1:tn.47", "black", [ "v0" ] ],
    [ "btn11:1.l", "bb1:tn.43", "black", [ "v0" ] ],
    [ "btn9:1.l", "bb1:tn.35", "black", [ "v0" ] ],
    [ "btn8:1.l", "bb1:tn.31", "black", [ "v0" ] ],
    [ "btn7:1.l", "bb1:tn.26", "black", [ "v0" ] ],
    [ "btn6:1.l", "bb1:tn.22", "black", [ "v0" ] ],
    [ "btn5:1.l", "bb1:tn.18", "black", [ "v0" ] ],
    [ "btn4:1.l", "bb1:tn.14", "black", [ "v0" ] ],
    [ "btn3:1.l", "bb1:tn.10", "black", [ "v0" ] ],
    [ "btn2:1.l", "bb1:tn.5", "black", [ "v0" ] ],
    [ "btn1:1.l", "bb1:tn.1", "black", [ "v0" ] ],
    [ "btn13:2.l", "pico:GP0", "green", [ "v-249.6", "h-115.4" ] ],
    [ "btn12:2.l", "pico:GP1", "green", [ "v-240", "h-77" ] ],
    [ "btn11:2.l", "pico:GP2", "green", [ "v-211.2", "h-48.2" ] ],
    [ "btn10:2.l", "pico:GP28", "green", [ "v-76.8", "h-29" ] ],
    [ "btn9:2.l", "pico:GP27", "green", [ "v0" ] ],
    [ "btn8:2.l", "pico:GP26", "green", [ "v-67.2", "h38.2" ] ],
    [ "btn7:2.l", "pico:GP22", "green", [ "v-57.6", "h67" ] ],
    [ "btn6:2.l", "pico:GP21", "green", [ "v-86.4", "h95.8" ] ],
    [ "btn5:2.l", "pico:GP20", "green", [ "v-96", "h134.2" ] ],
    [ "btn4:2.l", "pico:GP19", "green", [ "v-86.4", "h172.6" ] ],
    [ "btn3:2.l", "pico:GP18", "green", [ "v-115.2", "h211" ] ],
    [ "btn2:2.l", "pico:GP17", "green", [ "v-105.6", "h239.8" ] ],
    [ "btn1:2.l", "pico:GP16", "green", [ "v-134.4", "h278.2" ] ],
    [ "bb1:63t.c", "bb1:tn.49", "black", [ "v-19.2", "h-28" ] ],
    [ "pico:GND.8", "bb1:tn.50", "black", [ "v97.2", "h135.2" ] ],
    [ "pico:3V3", "encoder1:VCC", "red", [ "v-56.4", "h-230" ] ],
    [ "pico:GND.4", "bb2:1t.b", "black", [ "v19.2", "h-115.2", "v-28.8" ] ],
    [ "encoder1:SW", "pico:GP15", "green", [ "v0" ] ],
    [ "encoder1:DT", "pico:GP14", "green", [ "v9.6", "h76.7" ] ],
    [ "encoder1:CLK", "pico:GP13", "green", [ "h86.4", "v19.2" ] ],
    [ "btn14:2.r", "bb2:bn.5", "black", [ "v0" ] ],
    [ "bb2:bn.1", "btn15:2.r", "black", [ "v0" ] ],
    [ "btn15:1.r", "pico:GP12", "green", [ "v-230.2", "h115.2" ] ],
    [ "btn14:1.r", "pico:GP11", "green", [ "v-220.6", "h76.8" ] ],
    [ "pico:GND.6", "bb1:tp.24", "black", [ "v87.6", "h-66.4" ] ],
    [ "pico:GND.3", "bb2:bn.25", "black", [ "v-57.6", "h153.6", "v172.8", "h-40" ] ],
    [ "pico:GP0", "bb2:30t.c", "", [ "$bb" ] ],
    [ "pico:GP1", "bb2:29t.c", "", [ "$bb" ] ],
    [ "pico:GND.1", "bb2:28t.c", "", [ "$bb" ] ],
    [ "pico:GP2", "bb2:27t.c", "", [ "$bb" ] ],
    [ "pico:GP3", "bb2:26t.c", "", [ "$bb" ] ],
    [ "pico:GP4", "bb2:25t.c", "", [ "$bb" ] ],
    [ "pico:GP5", "bb2:24t.c", "", [ "$bb" ] ],
    [ "pico:GND.2", "bb2:23t.c", "", [ "$bb" ] ],
    [ "pico:GP6", "bb2:22t.c", "", [ "$bb" ] ],
    [ "pico:GP7", "bb2:21t.c", "", [ "$bb" ] ],
    [ "pico:GP8", "bb2:20t.c", "", [ "$bb" ] ],
    [ "pico:GP9", "bb2:19t.c", "", [ "$bb" ] ],
    [ "pico:GND.3", "bb2:18t.c", "", [ "$bb" ] ],
    [ "pico:GP10", "bb2:17t.c", "", [ "$bb" ] ],
    [ "pico:GP11", "bb2:16t.c", "", [ "$bb" ] ],
    [ "pico:GP12", "bb2:15t.c", "", [ "$bb" ] ],
    [ "pico:GP13", "bb2:14t.c", "", [ "$bb" ] ],
    [ "pico:GND.4", "bb2:13t.c", "", [ "$bb" ] ],
    [ "pico:GP14", "bb2:12t.c", "", [ "$bb" ] ],
    [ "pico:GP15", "bb2:11t.c", "", [ "$bb" ] ],
    [ "pico:GP16", "bb2:11b.h", "", [ "$bb" ] ],
    [ "pico:GP17", "bb2:12b.h", "", [ "$bb" ] ],
    [ "pico:GND.5", "bb2:13b.h", "", [ "$bb" ] ],
    [ "pico:GP18", "bb2:14b.h", "", [ "$bb" ] ],
    [ "pico:GP19", "bb2:15b.h", "", [ "$bb" ] ],
    [ "pico:GP20", "bb2:16b.h", "", [ "$bb" ] ],
    [ "pico:GP21", "bb2:17b.h", "", [ "$bb" ] ],
    [ "pico:GND.6", "bb2:18b.h", "", [ "$bb" ] ],
    [ "pico:GP22", "bb2:19b.h", "", [ "$bb" ] ],
    [ "pico:RUN", "bb2:20b.h", "", [ "$bb" ] ],
    [ "pico:GP26", "bb2:21b.h", "", [ "$bb" ] ],
    [ "pico:GP27", "bb2:22b.h", "", [ "$bb" ] ],
    [ "pico:GND.7", "bb2:23b.h", "", [ "$bb" ] ],
    [ "pico:GP28", "bb2:24b.h", "", [ "$bb" ] ],
    [ "pico:ADC_VREF", "bb2:25b.h", "", [ "$bb" ] ],
    [ "pico:3V3", "bb2:26b.h", "", [ "$bb" ] ],
    [ "pico:3V3_EN", "bb2:27b.h", "", [ "$bb" ] ],
    [ "pico:GND.8", "bb2:28b.h", "", [ "$bb" ] ],
    [ "pico:VSYS", "bb2:29b.h", "", [ "$bb" ] ],
    [ "pico:VBUS", "bb2:30b.h", "", [ "$bb" ] ],
    [ "btn1:1.l", "bb1:3t.d", "", [ "$bb" ] ],
    [ "btn1:2.l", "bb1:1t.d", "", [ "$bb" ] ],
    [ "btn1:1.r", "bb1:3b.i", "", [ "$bb" ] ],
    [ "btn1:2.r", "bb1:1b.i", "", [ "$bb" ] ],
    [ "btn2:1.l", "bb1:8t.b", "", [ "$bb" ] ],
    [ "btn2:2.l", "bb1:6t.b", "", [ "$bb" ] ],
    [ "btn2:1.r", "bb1:8b.g", "", [ "$bb" ] ],
    [ "btn2:2.r", "bb1:6b.g", "", [ "$bb" ] ],
    [ "btn3:1.l", "bb1:13t.d", "", [ "$bb" ] ],
    [ "btn3:2.l", "bb1:11t.d", "", [ "$bb" ] ],
    [ "btn3:1.r", "bb1:13b.i", "", [ "$bb" ] ],
    [ "btn3:2.r", "bb1:11b.i", "", [ "$bb" ] ],
    [ "btn4:1.l", "bb1:18t.b", "", [ "$bb" ] ],
    [ "btn4:2.l", "bb1:16t.b", "", [ "$bb" ] ],
    [ "btn4:1.r", "bb1:18b.g", "", [ "$bb" ] ],
    [ "btn4:2.r", "bb1:16b.g", "", [ "$bb" ] ],
    [ "btn5:1.l", "bb1:23t.d", "", [ "$bb" ] ],
    [ "btn5:2.l", "bb1:21t.d", "", [ "$bb" ] ],
    [ "btn5:1.r", "bb1:23b.i", "", [ "$bb" ] ],
    [ "btn5:2.r", "bb1:21b.i", "", [ "$bb" ] ],
    [ "btn6:1.l", "bb1:28t.d", "", [ "$bb" ] ],
    [ "btn6:2.l", "bb1:26t.d", "", [ "$bb" ] ],
    [ "btn6:1.r", "bb1:28b.i", "", [ "$bb" ] ],
    [ "btn6:2.r", "bb1:26b.i", "", [ "$bb" ] ],
    [ "btn7:1.l", "bb1:33t.b", "", [ "$bb" ] ],
    [ "btn7:2.l", "bb1:31t.b", "", [ "$bb" ] ],
    [ "btn7:1.r", "bb1:33b.g", "", [ "$bb" ] ],
    [ "btn7:2.r", "bb1:31b.g", "", [ "$bb" ] ],
    [ "btn8:1.l", "bb1:38t.d", "", [ "$bb" ] ],
    [ "btn8:2.l", "bb1:36t.d", "", [ "$bb" ] ],
    [ "btn8:1.r", "bb1:38b.i", "", [ "$bb" ] ],
    [ "btn8:2.r", "bb1:36b.i", "", [ "$bb" ] ],
    [ "btn9:1.l", "bb1:43t.b", "", [ "$bb" ] ],
    [ "btn9:2.l", "bb1:41t.b", "", [ "$bb" ] ],
    [ "btn9:1.r", "bb1:43b.g", "", [ "$bb" ] ],
    [ "btn9:2.r", "bb1:41b.g", "", [ "$bb" ] ],
    [ "btn10:1.l", "bb1:48t.d", "", [ "$bb" ] ],
    [ "btn10:2.l", "bb1:46t.d", "", [ "$bb" ] ],
    [ "btn10:1.r", "bb1:48b.i", "", [ "$bb" ] ],
    [ "btn10:2.r", "bb1:46b.i", "", [ "$bb" ] ],
    [ "btn11:1.l", "bb1:53t.b", "", [ "$bb" ] ],
    [ "btn11:2.l", "bb1:51t.b", "", [ "$bb" ] ],
    [ "btn11:1.r", "bb1:53b.g", "", [ "$bb" ] ],
    [ "btn11:2.r", "bb1:51b.g", "", [ "$bb" ] ],
    [ "btn12:1.l", "bb1:58t.d", "", [ "$bb" ] ],
    [ "btn12:2.l", "bb1:56t.d", "", [ "$bb" ] ],
    [ "btn12:1.r", "bb1:58b.i", "", [ "$bb" ] ],
    [ "btn12:2.r", "bb1:56b.i", "", [ "$bb" ] ],
    [ "btn13:1.l", "bb1:63t.d", "", [ "$bb" ] ],
    [ "btn13:2.l", "bb1:61t.d", "", [ "$bb" ] ],
    [ "btn13:1.r", "bb1:63b.i", "", [ "$bb" ] ],
    [ "btn13:2.r", "bb1:61b.i", "", [ "$bb" ] ],
    [ "encoder1:CLK", "bb2:5t.a", "", [ "$bb" ] ],
    [ "encoder1:DT", "bb2:4t.a", "", [ "$bb" ] ],
    [ "encoder1:SW", "bb2:3t.a", "", [ "$bb" ] ],
    [ "encoder1:VCC", "bb2:2t.a", "", [ "$bb" ] ],
    [ "encoder1:GND", "bb2:1t.a", "", [ "$bb" ] ],
    [ "btn14:1.l", "bb2:8t.d", "", [ "$bb" ] ],
    [ "btn14:2.l", "bb2:6t.d", "", [ "$bb" ] ],
    [ "btn14:1.r", "bb2:8b.i", "", [ "$bb" ] ],
    [ "btn14:2.r", "bb2:6b.i", "", [ "$bb" ] ],
    [ "btn15:1.l", "bb2:3t.d", "", [ "$bb" ] ],
    [ "btn15:2.l", "bb2:1t.d", "", [ "$bb" ] ],
    [ "btn15:1.r", "bb2:3b.i", "", [ "$bb" ] ],
    [ "btn15:2.r", "bb2:1b.i", "", [ "$bb" ] ],
    [ "lcd1:SCL", "pico:GP9", "green", [ "h0" ] ],
    [ "lcd1:SDA", "pico:GP8", "green", [ "h0" ] ],
    [ "pico:GND.1", "lcd1:GND", "black", [ "v0" ] ],
    [ "lcd1:VCC", "pico:VBUS", "red", [ "h-28.8", "v134.5", "h124.8", "v220.8", "h-86.4" ] ]
  ],
  "dependencies": {}
}

```
