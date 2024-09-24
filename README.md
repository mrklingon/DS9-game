# DS9-game

* ds9.js - Javascript/Makecode version of game (https://makecode.com/_KhmDoYXCpVdh)
* ds9.py - CircuitPython version (rename to code.py)
* bach.py - helper code for music and sounds for ds9.py

Simple game using the Circuit Playground circle of neopixels. The premise is the space station Deep Space Nine (a blue neopixel) is in motion near the Bajoran Wormhole (a neopixel of shifting color0. As the station shifts back and forth, the wormhole remains the same distance (five neopixels away). The station is launching automated probes to the wormhole - **A** sends them counter-clockwise, **B** sends them in a clockwise direction. You have ten probes to launch - if they successfully enter the wormhole, there will be a rainbow of neopixels across all ten. When you have sent all ten, you'll see pixels representing how many you managed to send into the wormhole (0-10). For the Makecode version, shake the CPX to restart. For the CircuitPython version press **A** or **B**.

Both versions make a sound when launching the probe, and will play a scale or musical flourish when you succeed. To turn that off, slide the switch to the left. To the right turns the game sounds on.
