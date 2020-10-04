# Speaking Clock for Raspbery Pi
 
Speaking clock uses offline text-to-spech (TTS) engine and Linux cron to generate and play a waveform file.
Cron is configured to run every half an hour and runs a shell script which in turn executes Python code.

## TTS Engine Selection
Various text2speech libraries can be used like Pico2Wave, Festival, eSpeaker and Flite for offline processing.
Flite with additional voices sounds preety good.

### Examples for pico2wave and flite:

```
pico2wave -w lookdave.wav "<volume level='40'><pitch level='70'>Hello there i am a smurf and now i'm not" && aplay lookdave.wav
pico2wave -w lookdave.wav "<volume level='40'><pitch level='5'>Time is: 05:30</pitch>" && aplay lookdave.wav
pico2wave -w lookdave.wav "<volume level='40'><pitch level='120'>Pink here</pitch>" && aplay lookdave.wav
```
   
```
flite -voice rms -o tt.wav -t "All good men come to the aid of the rebellion" && aplay tt.wav
flite -voice rms -o /tmp/tt.wav -t "Time is: 05:30" && aplay /tmp/tt.wav
flite -voice flite_voices/cmu_us_bdl.flitevox -o tt.wav -t "RPi here. Time is: 5:30" && aplay tt.wav
```
### Flite binaries and voices:
http://festvox.org/flite/packed/flite-2.1/   
Voices files were placed in `/usr/local/share/flite/voices` folder on Raspberry Pi.

## Software versions
Raspbian GNU/Linux 10 (buster)   
Linux raspberrypi 4.19.97-v7+ #1294 SMP Thu Jan 30 13:15:58 GMT 2020 armv7l GNU/Linux   
flite-2.1-release Dec 2017   
Python 2.7.16   

## Crontab configuration
`0,30 7-22 * * * bash /home/pi/projects/speaking-clock/run.sh`

## References
https://elinux.org/RPi_Text_to_Speech_(Speech_Synthesis)
https://www.raspberrypi.org/forums/viewtopic.php?t=220494
https://www.raspberrypi.org/forums/viewtopic.php?t=180281
https://circuitdigest.com/microcontroller-projects/raspberry-pi-based-jarvis-themed-speaking-alarm-clock
https://www.dronkert.net/rpi/vol.html
http://www.speech.cs.cmu.edu/flite/doc/flite_toc.html
http://www.festvox.org/flite/download.html
http://www.festvox.org/flite/doc/flite_8.html
https://github.com/festvox/flite
