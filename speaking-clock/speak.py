from datetime import datetime
from subprocess import call
from random import randint

file_name = "/tmp/tmp123.wav"            #TODO: add to input arguments
flite_voices_path = "/usr/local/share/"  #TODO: add to input arguments

postfix_texts = ["Time flies!", "already", "Getting late", "Move on!", "yeah!", "Time goes by", "Time passes"]
good_nite_texts = ["Time to bed!", "Good night!", "Sweet dreams!", "See you tomorrow!", "Bye bye!"]
good_mornig_texts = ["Good morning!", "Nice to see you!", "Hello today!", "Have a nice day!", "How are you!"]
greeting_texts = ["Raspee here", "It's Raspee", "Raspee speaking"]

def get_prefix_text():
    index = randint(0, len(greeting_texts) - 1)
    return greeting_texts[index]

def get_random_postfix_text():
    index = randint(0, len(postfix_texts) - 1)
    return postfix_texts[index]

def get_random_good_nite_text():
    index = randint(0, len(good_nite_texts) - 1)
    return good_nite_texts[index]
    
def get_random_good_morning_text():
    index = randint(0, len(good_mornig_texts) - 1)
    return good_mornig_texts[index]    

def get_postfix_text():
    now = datetime.now()
    hour = int(now.strftime("%H"))
    minute = int(now.strftime("%M"))
    if hour == 22:
        return get_random_good_nite_text()
    elif hour in [7,8]:
        return get_random_good_morning_text()
    else:
        return get_random_postfix_text()

def get_current_time_str():
    now = datetime.now()
    time_string = now.strftime("%I:%M")
    return "Time is: " + time_string + "."

def create_text_to_speak():
    return get_prefix_text() + ", " + get_current_time_str() + " - " + get_postfix_text()

def speak_pico():
    tts = create_text_to_speak()
    tts = "<volume level='40'><pitch level='100'>" + tts + "</pitch>"
    call(["pico2wave", "-w", file_name, tts])
    call(["aplay", file_name])
    call(["rm", file_name])
    
def speak_flite():
    tts = create_text_to_speak()
    call(["flite_cmu_us_slt", "-voice", flite_voices_path + "flite/voices/cmu_us_bdl.flitevox", "-o", file_name, "-t", tts])
    call(["aplay", file_name])
    call(["rm", file_name])

#print(get_current_time_str())
#print(get_postfix_text())
speak_flite()
