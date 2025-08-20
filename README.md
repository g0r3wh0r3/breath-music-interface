
# breath/music interface project 

## brief overview 
wearable sensor system that converts respiratory signals into analog control signals for guitar effects or synth systems, to have expressive and intuitive, hands-free control of sound. current stage: prototyping wearable inductance band sensor. 

## instigating/driving problem
- traditional instrument setups seem to mostly rely on hands and feet for playing instruments and controlling pedals/switches/knobs/etc. 
- that can feel clunky, physically and cognitively demanding having to multitask between playing an instrument and controlling various effects and switches with your hands 
- and these methods of control are often limited, lacking more precise and expressive control 
## what i want to explore
- what other inputs from our bodies could be used to control sound?  
- how can we create channels for more nuanced control of more parameters, in a way that feels more organic/natural? less cognitively effortful? 

## project overview 
There will be two parts to the setup, the sensor (the input) and the effect that it controls (the output).  The user should be able to map the sensor output to different effects. The first sensor we are making is a respiratory band. The user will wear the band around their belly or ribs, and as they inhale the band will stretch. The stretching of the band will generate a signal. We are starting with one sensor and hopefully will start building more to map to different effects over time. 

## conceptual motivation 
-  Effects feel like something you add on top after the fact, not something you “play” - i want to make the control of effects feel just as much a part of/extension of the instrument 
- Overall the goal is related to expression in a way that’s not as cognitively “effortful” 
- Direct extension of physical expression 

## technical 
should be compatible to just plug and use in place of an expression pedal, so outputs a variable resistance across a TRS jack

## input ideas 
### Heart reate 
- heart rate sensors work through photoplethysmography which detects changes in blood volume 
- light shines on the skin, the amount that is reflected back is related to the blood volume 
-  the frequencies that get reflected back is related to the oxygen saturation (oxygenated hemoglobin absorbs more infrared light, deoxygenated absorbs more red, less infrared) 
- the signal that comes back from this is periodic w/ spikes at heart beats 
-  there will be noise from the user's movement needs to be filtered out (or, maybe not for this application . . . )
- if i get an off-the-shelf HR monitor it'll just give me a digital signal, like just the bpm? i think I might want the raw waveform tho am I going to have to make one myself? that could be fun . .

### Jaw EMG 
clenching jaw muscles -> distortion++

### Skin conductivity 
see papers in resources section 

### temperature
body temp 
temperature as feedback to the user, potentially? 

## output ideas 
### analog "reverb" 
using bucket bridage set up a network of a bunch of feedback loops to create an analog sort of reverb effect 

### haptic feedback 
What if the device could also give some sort of haptic feedback to the user? 

### lights 
Could work well with breath sensor. There is a prof in BME (?? or SYDE?) who apparently has like 9000 extra LEDs  

### perlin noise 
Use the sensor's output as the seed to generate perlin noise, or for the other shaping parameters for it. For visual effects ([using perlin noise in sound design](https://lac.linuxaudio.org/2018/pdf/14-paper.pdf ))

## references/resources 
### materials 
[polymeric nanocomposite-based wearable strain sensor](https://www.sciencedirect.com/science/article/pii/S2468519424001307)

https://www.sciencedirect.com/science/article/pii/S2352940724001112

**look into PEDOT:PSS devices later? 

### circuit design ref 
[BBD IC for making a reverb-like effect](https://www.experimentalistsanonymous.com/diy/Datasheets/MN3011.pdf)  

[this](https://oldbloodnoise.com/pedals/p/dweller-phase-repeater?srsltid=AfmBOoqE6TcFPwf2adqMzhS6i7uTlZFXy28zq6bI5YMuOL4RTe6DqfCq) sounds cool, how does it work?? ([video](https://youtu.be/V1spQIuSd4Q?si=idhsKbtcABerTEm9&t=76))  

[ultra clean 9V power supply](https://generalguitargadgets.com/wp-content/uploads/ultra_clean_ps_sc.gif )

[understanging expression pedals](https://missionengineering.com/understanding-expression-pedals/)
 

### respiratory inductance plethysmography 
* whats used in medical devices for respiratory  monitoring 
* [RIP](https://en.wikipedia.org/wiki/Respiratory_inductance_plethysmography#:~:text=Respiratory%20inductance%20plethysmography%20\(RIP\)%20is,coupled%20to%20the%20airway%20opening.) ([video](https://www.youtube.com/watch?v=vMgPrCn_1Uk))
* Often it uses two bands, the thoracic which goes over your ribs/chest, and the abdominal which goes over your belly. Could be interesting to use both, especially for vocalists 

### cool stuff other people made 
https://zenodo.org/records/15028172\ 





