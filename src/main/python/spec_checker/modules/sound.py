import sys
if sys.platform.startswith('win32'):
    import soundcard


class SoundRecord:
    def __init__(self, sound_cards=None, sound_card_present=False, default_sound_card=None,
                 mics=None, mic_present=False, default_mic=None):
        self.sound_cards = sound_cards
        self.sound_card_present = sound_card_present
        self.default_sound_card = default_sound_card
        self.mics = mics
        self.mic_present = mic_present
        self.default_mic = default_mic

    def __repr__(self):
        return f"<SoundRecord sound_card_present:{self.sound_card_present} mic_present: {self.mic_present}>"

    def __str__(self):
        return f"""
Sound Information:
Sound Card Present: {self.sound_card_present}
Default Sound Card: {self.default_sound_card}
Mic Present: {self.mic_present}
Default Mic: {self.default_mic}"""

    def test(self):
        self.sound_cards = soundcard.all_speakers()
        self.mics = soundcard.all_microphones()

        if len(self.sound_cards) > 0:
            self.sound_card_present = True
            self.default_sound_card = soundcard.default_speaker()
        else:
            self.sound_card_present = False
            self.default_sound_card = "No default sound card found. May not be enabled or plugged in."

        if len(self.mics) > 0:
            self.mic_present = True
            self.default_mic = soundcard.default_microphone()
        else:
            self.mic_present = False
            self.default_mic = "No default mic found. May not be enabled or plugged in."
        return self
