#Lab 1 Report

##Bounding box tracking

So my goal for lab 1 was largely to be able to track the green Beaglebone box that I have lying around as it is a fairly contrasting green to everything else.

I started messing with the boilerplate provided by the OpenCV website and was able to figure out that trying to mess with the threshold was the main thing to do. First approach was of course to use grayscale brightness but that quickly proved futile, too much noise. Next attempt was trying to isolate the green spectrum from the BGR set which worked better except that white contains green, which I also did not want and the glare from my lights to my wall partiucularly caused issues.

I tried some other methods with BGR such as subtracting out the B and R but that proved unsuccessful, probably because of unsigned int overflows. I also messed around with HSV a little bit. I recognized the ideal way to do this was to isolate the correct view but I did not think there was a easy way to do it so I tried just doing it with saturation and value but that proved to fail as well.

Eventually I found the inRange function and that basically gave me what I needed, was able to isolate a decent range for the green hue and the bounding box works pretty well now. After some trial and error correcting the upper and lower bounds I was able to get it to work very well, though I'm sure I could get it better with a little more trial and error. 


This works fairly well in different lighting conditions at this point due to hue isolation, but of course low light has more difficulties but not much. I've also made it work very well with a lit green screen from my phone, and works basically in any brightness due to the use of hue. 


##Color Checker

I also did the k-means dominant color finder, mainly by doing some light modification to the code linked to in the PDF. Its fairly crude, apparently the algorithm takes a while, but regardless I was able to slide show my webcam scanning various colors in various lighting conditions, good enough to experiment with color values. I sampled the center 40 by 40 square of the image and put various things in front of it. 

RGB behaved mostly as I supposed it would behave, brighter is greater values, dimmer is smaller valeues. But I also printed HSV values, which were far more interesting as I could mostly see the changes without any sort of statistical analysis like RGB would need. 

Brighter colors leant themselves to more accurate results, with the 3 dominant color values being closer together, hue being at most 1 off. Dimming the brightness as expected brought down the value of the HSV data, saturation seemed mostly clumped together as well, with a little more variance when the surrounding was dimmer, and hue did similar, but I did notice that the hue seemed to consistently drop a little when dimmed, after having had tested a few different colors.

For the most part it behaved as expected, hue and saturation didn't change much between brightness conditions, value did. RGB rose mostly uniformly with an increase in light.