import appdaemon.plugins.hass.hassapi as hass

class ListenExample(hass.Hass):
"""
Type of class:
- Listener

Method called:
- Call sound ringer script
"""

    # Next, we will define our initialize function, which is how AppDaemon starts our app. 
    def initialize(self):

        # Putting this line in the initialize function will tell AppDaemon that we want to call a certain method on a certain event ("EVENT"). 
        self.listen_event(self.call_ringer, "EVENT_DOORBELL_PRESSED")

    # the method that is called when an event happens
    def call_ringer(self, event_name, data, kwargs):

        # sound ringer script