import soundcard as sc


def do_test():
    sound_cards = sc.all_speakers()
    mics = sc.all_microphones()

    if len(sound_cards) > 0:
        sound_card_present = True
        default_sound_card = sc.default_speaker()
    else:
        sound_card_present = False
        default_sound_card = "No default sound card found. May not be enabled or plugged in."

    if len(mics) > 0:
        mic_present = True
        default_mic = sc.default_microphone()
    else:
        mic_present = False
        default_mic = "No default mic found. May not be enabled or plugged in."

    return_object = {
        'sound_cards': sound_cards,
        'sound_card_present': sound_card_present,
        'default_sound_card': default_sound_card,
        'mics': mics,
        'mic_present': mic_present,
        'default_mic': default_mic
    }

    return return_object


def get_audio_info():
    return do_test()


def print_audio_info():
    audio_devices = do_test()

    print("=" * 20 + " Audio Information " + "=" * 20)
    print("Sound Card Present: " + str(audio_devices['sound_card_present']))
    print("Default Sound Card: " + str(audio_devices['default_sound_card']))
    print("Mic Present: " + str(audio_devices['mic_present']))
    print("Default Mic: " + str(audio_devices['default_mic']))
    print(" ")
    print("All Soundcard Data: ")
    print(audio_devices['sound_cards'])
    print(" ")
    print("All Mic Data: ")
    print(audio_devices['mics'])
    print(" ")


if __name__ == '__main__':
    print_audio_info()
