import appdaemon.plugins.hass.hassapi as hass

class ListenExample(hass.Hass):
"""
Type of class:
- Listener

Method called:
- Print to log: "Hey, Listen!"
"""

    # Next, we will define our initialize function, which is how AppDaemon starts our app. 
    def initialize(self):

        # Putting this line in the initialize function will tell AppDaemon that we want to call a certain method on a certain event ("EVENT"). 
        self.listen_event(self.event_happened, "EVENT")

    # the method that is called when an event happens
    def event_happened(self, event_name, data, kwargs):

        # Now let's print a message when this function is called. Add the following line
        self.log("Hey, Listen!")