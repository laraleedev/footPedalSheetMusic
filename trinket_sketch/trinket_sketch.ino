/*
Trinket USB Foot Switch

Based on TrinketKeyboard example using the Trinket Keyboard Library
For Trinket (ATtiny85 based board) by Adafruit Industries

Version 1.0  2015-01-19 Initial version     Mike Barela

Support Adafruit tutorials by buying parts from Adafruit.com
*/

#include <TrinketKeyboard.h>  // Trinket keyboard library

const int PIN_SWITCH = 0;    // Trinket pin to connect to switch 

void setup()
{
  // Set button pin as input with an internal pullup resistor
  // The button is active-low, they read LOW when they are not pressed
  pinMode(PIN_SWITCH, INPUT_PULLUP);

  TrinketKeyboard.begin();  // initialize keyboard library
}

void loop()
{
  TrinketKeyboard.poll();
  // the poll function must be called at least once every 10 ms
  // or the computer may think that the device
  // has stopped working, and give driver errors

  if (digitalRead(PIN_SWITCH) == LOW)  // If the foot switch grounds the pin
  {
    // Select what key to press when the switch is tripped
    //   Possible keys are defined in TrinketKeyboard.h
    // Selected keys are Print Screen with the shift key modifier
    TrinketKeyboard.pressKey(0, KEYCODE_N);

    // If you want to send a string, replace the 2 calls above with the line below
    // TrinketKeyboard.print("Hello World!"); // use for string instead of char
  } 
  else 
  {
    TrinketKeyboard.pressKey(0, 0);  // release key
  }
}
