 Working on a new design for the circuit. 

I will have an oscillator where the frequency of the oscillator is dependent on the inductor value. Then I will use an IC to convert the frequency to a voltage (a phase-locked loop IC). I am currently working on learning how those work and how to select the right part. The device should be able to output a voltage for devices with CV input. I think I will not really need to do anything to linearise it because it should be roughly linear enough and also I don't care. I want it to also be able to interface with devices that take an EXP (expression pedal) input, which means that I'm giving them a variable resistance, so a voltage-controlled resistance. I have read about some old analog gear that used to use an LED, which would get dimmer/brighter, facing a photoresistor/light-dependent resistor, and I happened to find a photoresistor on the ground about a week ago! 


# oscillator 
 Will be using a Colpitts oscillator circuit, where the inductor will be the breath band, following ([this](https://iopscience.iop.org/article/10.1088/0967-3334/15/2/009/pdf)) article. 

 Resources used for learning about how this works and figuring out how to design the circuit: 
 - https://www.youtube.com/watch?v=ES-kcNR4Ln0
 - https://www.youtube.com/watch?v=1fgw-ONlAcc&t=355s 
 - Sedra & Smith, pages 1396-1400 

Here are my notes on the schematic given in Cohen et al, 1994 figure 2
<image src="assets/IMG_5330.jpg" alt="photo of notes">
 
I decided on a 9V supply because that's what seems to be most common for pedals and synths. I also have a 9V battery sitting somewhere to use. I did some calculations for some of the resistor/capacitor values, and some I just picked based on vibes idk 

I simulated the circuit in LTspice. I did a transient simulation for 1 second and checked "Start DC supplies at zero". Here's what it looks like 
<image src="assets/oscillator_ltspice.png" alt="screenshot from ltspice">

I don't think that's how it's supposed to look. I expected to see oscillation at around 1 MHz, the initial weird stuff idk what causes that or what to do about it so I still think I need to learn more about how this circuit works to design it properly.  

What's left to do in the design: 
- finalse the oscillator design, picking suitable values for all components. the capacitor values C1 and C2 will also be dependent on what the inductance of the coil is, so I need to figure that out. Been (over)thinking about the coil geometry and trying to simulate in COMSOL to figure out how I want to wind it (orientation, number of turns, etc.) but it keeps crashing because I think I'm setting up the parameters incorrectly idk 
- figure out the PLL 
- figure out both of the output modes  
- once the full schematic is finished, order/gather whatever parts we need and start testing on breadboard to verify it actually works before ordering PCB 
- try to find a domestic PCB fab that adheres to ethical/labour standards (?) 
- also need a simple effect to test it with (I don't want to borrow a $100 pedal from someone to test my sensor on and accidentally fry it, can breadboard a simple effect)




