 (need to organise/review this mess, separate out references/resources and organise those, separate out different ideas.)
- bio controlled fx 
- goal: intuitive control of sound from bio signals. somatic experiences -> music 
- How can we add more ways to control/create sounds that don’t involve having to “multitask” using your hands to control many things at once? How can it be made more intuitive/natural extension that works with you rather than you working with it?  
- Should it provide some sort of haptic feedback right away then too or something? Something to think about later temperature could be interesting too
- Overall the goal is related to expression in a way that’s not as cognitively “effortful” \
- direct extension of physical expression , embodied cognition, somatic design, something about heidegger, more buzzword here,  idk i just want to make cool thing 
- Effects feel like something you add on top after the fact, not something you “play” - i want to make the control of effects feel just as much a part of/extension of the instrument
- can layer in more signals and map them to different effects over time, piece by piece like adding more detail to the sound (like that layered ambient texture shoegazey shit like mbv/airiel/isis( panopticon)/alcest/deafheaven maybe)
- So I can split this into two things that I want to make: 
- “expression” input. So this would be the sensor hardware, as in the actual breath band part if I decide to make that. Should be compatible to just plug and use in place of an expression pedal, so outputs a variable resistance across a TRS jack 
- The effect(s) itself, should be able to be used just like any other pedal, could use my sensor expression input or whatever else you want, should be able to mix&match/customize the setup however you wanted. Input: instrument signal thru TS jack (need high input impedance), TRS expression input. Outputs affected signal. DC barrel jack for power (std. size/voltage so its usable. 9V) 
- Starting with very simple things now, can work on building more different controllers/effects over time to mix/match 
-  protective from abstraction of experience (as opposed to abstracting/distilling experience into controllable chunks by consciously "translating" into symbolic representations? i mean it's still mapping thing to another tho) 
- [https://www.youtube.com/watch?v=IwBTNAq8Qy8](https://www.youtube.com/watch?v=IwBTNAq8Qy8) 
- [https://www.tecontrol.se/products/usb-midi-breath-controller](https://www.tecontrol.se/products/usb-midi-breath-controller) except no MIDI, no conversion to digital, i literally just want to use the analog sensor output to control an effect directly. So it’d be open you can use it for whatever you want i guess. I like the idea of the physical feeling of pressing/controlling something by expanding your ribs also I don’t know if I want it to just be a mouthpiece because then you have to breathe through your mouth. And the device in your mouth might feel like more of an intrusion and I want it to be as natural/comfortable as possible, like you could forget it’s there which is why I like a wearable band (plus you can’t sing/talk while playing using that, and anyway i think I want it to be tied more closely to the actual muscle movements of breathing than the “results” of contracting/expanding those muscles. plus i think this could be cool for a vocalist to use too)
- [https://nime.org/papers/](https://nime.org/papers/) 
- Potential PCB fab option [https://uwaterloo.ca/centre-for-intelligent-antenna-and-radio-systems/rapid-prototyping-lab](https://uwaterloo.ca/centre-for-intelligent-antenna-and-radio-systems/rapid-prototyping-lab) says there is a user fee though 
- [https://nime.org/proceedings/2025/nime2025_24.pdf](https://nime.org/proceedings/2025/nime2025_24.pdf)
# Possible control sources/ideas/sensor input: 

- jaw EMG ?? jaw muscles clenching -> distortion++
- Perlin noise!  bio signal as seed ?? or shaping the other parameters for it?? 
-  what if u could get everyone in a room to wear a sensor and collect all that data to generate/affect/shape some music/sound 
-  use breath to alter synthesizer velocity/volume
-  what about sensors that sit directly on the skin like, stickers, or even less invasive like those temporary tattoos that sink into ur skin? skin conductivity measure or something? 
-  temp sensors as well, indirectly measuring blood volume changes, combined w/ strain sensors 
- Gestures - IMUs? TENG??? (impractical .  . . )
- GI noise ?? mapping to some musical parameter or 
- For something unpredictable/not used as a practical “instrument” but as some other conceptual pretentious shit 
- Temporary tattoo electrodes???? PEDOT:PSS ?
- Obviously this is very ambitious and insane, would need some lab to give me space and money and probably a lot of help figuring it out but it’d be so cool 
- Other body-conformable electronics might be something to look into tho like tape/sticker type things? 
- [https://www.nature.com/articles/s41528-024-00356-6](https://www.nature.com/articles/s41528-024-00356-6) 
- also the idea of synaptic-like processing is interesting/cool . . . how could memristor based processing of the signal from the sensor be used to determine how the sound is affected? Thats an idea for later probably but that would be cool to try to use something like that for an effect. It could learn with you as you play, just as much as you’re learning it 
# BREATH 

-  resistive stretch band for “smooth” control 
- [https://www.adafruit.com/product/519?srsltid=AfmBOoqd_s7tdCOwnVQD_980hMsF13687YHxJFv0gqCWR1t-k1NaeS6Y](https://www.adafruit.com/product/519?srsltid=AfmBOoqd_s7tdCOwnVQD_980hMsF13687YHxJFv0gqCWR1t-k1NaeS6Y) 39 inches, should be more than enough for any average sized person? Would it still need to be adjustable? You want it to fit taught with a small bit of tension all the time, not being loose/hanging off anyone. 
- nylon/spandex/ some material to make a stretchable band that fits comfortably and snug
- Are there sewing machines i can use 
- Smart textiles, screen printed strain sensors w/ conductive ink? ($!!!)
- Silver NP conductive ink! Can print on a regular laserjet printer, find the tutorials found for rrl project? 
- Silver nps arent that hard to synthesize. But controlling for size so it doesnt clog printer nozzles might be difficult . . . 
- waste/disposal, health risks, environmental risks if it’s leaching into water from washing the garment 
- CNTs/graphene/conductive polymers or something ?? 
- would make more "base"/persistent sounds, maybe like reverb depth (???) changing w/ inhales or something, sweep a filter maybe 
-  maybe multiple sensors at different points layered for more "richness" ??? final product could be like a stretchy shirt/vest 
- what if there's conductive ink or something, strain sensing fabrics, so it'd have info about like muscle contraction in ur back/shoulders/diaphragm/etc. conductive ink or something? 
- Flex PCBs maybe for prototyping ?? no that sucks   
- do I want control of the sound to be from respiratory rate or per breath? or both i guess there can be layers 
- maybe use breath as a gate for some effect? like its on when inhaling, turns off as u exhale?
-  should intensity of breath affect things then? so how sudden/sharply you inhale would affect how suddenly the effect would come in/off, maybe? 
-  then for respiratory rate it could be like controlling drones in the background 
- then the rest of the music would have to shift with the drone as well otherwise it'll sound bad (??)
- maybe it gradually shifts the harmonics/overtones (???) like a boost around a specific frequency band, shifting that around? idk but just slowly shifting between different sounds in relation to resp. Rate (/heart rate) in a long sampling windows, and layered over that is the short-term effects from each breath
- use it for filter cutoff of a bandpass, it opens up more as u inhale ? (per-breath i guess but a subtler effect for that one)
- [https://www.sciencedirect.com/science/article/pii/S2468519424001307](https://www.sciencedirect.com/science/article/pii/S2468519424001307) 
- Resistive stretch band is noisy spikey signal - smoothing/filtering? Or will it be too bad that I can’t use it and need to look into the pneumatic bladders or inductance bands ? 

- Pneumatic bladder feels like it’d be bulky and awkward but maybe there is a way to design it that won’t feel awkward 

- I don’t want just the start on each inhale/exhale as discrete events, i want the breath to be a continuous control, like it would gradually shift the reverb wetness how the fuck can i do reverb analog 

- A bunch of looping feeding back the signal into itself, like a bunch of little echoing overlapping reflections, more like real/”natural” ”“reverb” in a literal sense 
- [https://www.experimentalistsanonymous.com/diy/Datasheets/MN3011.pdf](https://www.experimentalistsanonymous.com/diy/Datasheets/MN3011.pdf) 
- Smearing and saturation and fun reflections and weird nonlinear things and weird interactions that digital systems are trying to model, why not just actually use the physical systems !! instead of creating some weird indirect representation of the thing, lets just directly use the thing itself 
- Bucket brigade ?? a bunch of delay networks 
- As long as there’s no conversion to digital directly in the sound path i’m okay with it i guess 
- I guess it’s not really “reverb” that I want to make but like a bunch of echoey, delay loops feeding back. “Reverb” by literal accumulation of echoes, 
- [https://oldbloodnoise.com/pedals/p/dweller-phase-repeater?srsltid=AfmBOoqE6TcFPwf2adqMzhS6i7uTlZFXy28zq6bI5YMuOL4RTe6DqfCq](https://oldbloodnoise.com/pedals/p/dweller-phase-repeater?srsltid=AfmBOoqE6TcFPwf2adqMzhS6i7uTlZFXy28zq6bI5YMuOL4RTe6DqfCq) [https://youtu.be/V1spQIuSd4Q?si=idhsKbtcABerTEm9&t=76](https://youtu.be/V1spQIuSd4Q?si=idhsKbtcABerTEm9&t=76) 
- So a bunch of all-pass filters stacked into each other or something idk i’ll figure this out later 
- So this is one half of the project I guess. The effect and the sensor are separate parts. 

- Medical stuff uses [RIP](https://en.wikipedia.org/wiki/Respiratory_inductance_plethysmography#:~:text=Respiratory%20inductance%20plethysmography%20\(RIP\)%20is,coupled%20to%20the%20airway%20opening.) ([video](https://www.youtube.com/watch?v=vMgPrCn_1Uk)) which are expensive and also and ugly 

- Maybe thoracic band (ribs/chest) controls f1, abdominal band (belly) controls f2 ? 

- For “simpler” prototypes where it’s just doing a freq. sweep, not my kind of insane “analog reverb” bullshit . . . 

- TENGs - generate voltage from movement !! literally ur breath is creating the voltage how much more direct than that can u get?? 

- noisy/spikey weird jagged signal  which sounds like a signal processing nightmare but actually so rich with harmonics in a weird spikey signal ?? how to harvest them . . . 
-  op-amp buffer (probably needs to be pretty high impedance??)

-  Use TENG signal as a source of sound? like weird jumpy glitchy spike noises w/ breaths?? or modulation source ? like for distortion gain maybe
- for gestures, maybe? (ucalgary connection )
-  so layering the resistive stretch sensor for those “smooth” swelling base sounds and the TENG for spikey ! accenting for pops  

- skin conductivity?? 
- [https://zenodo.org/records/15028172](https://zenodo.org/records/15028172) 
# HEART RATE 

- heart rate sensors work thru photoplethysmography which detects changes in blood volume 
- light shines on the skin, the amount that is reflected back is related to the blood volume 
-  the frequencies that get reflected back is related to the oxygen saturation (oxygenated hemoglobin absorbs more infrared light, deoxygenated absorbs more red, less infrared) (learn exactly how oxygen saturation is calculated from this?why do i want oxygen saturation anyway)
- the signal that comes back from this is periodic w/ spikes at heart beats 
-  there will be noise from the user's movement needs to be filtered out 
- or does it . . . noise = cool sounds = good ?? 
- but probably we want a clean signal tho since we want direct control of the sound by heart rate not other random shit 
- if i get an off-the-shelf HR monitor it'll just give me a digital signal, like just the bpm? i think I might want the raw waveform tho am I going to have to make one myself? that could be fun . . .
  
  

# Controlling Eurorack modules:

Filter: [https://www.ericasynths.lv/shop/diy-kits-1/edu-diy-vcf/](https://www.ericasynths.lv/shop/diy-kits-1/edu-diy-vcf/)

Typical CV range: +/- 8V

Connect with 3.5mm plug

# Offset/Scaling:

  
  
  
  