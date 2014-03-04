steppercontrol
==============

Python module for controlling a stepper motor with the Raspberry Pi

based on Matt Hawkins tutorial: http://www.raspberrypi-spy.co.uk/2012/07/stepper-motor-control-in-python/

Description
===========
This module helps you to control your stepper motor 28BJY-48 with ULN2003 control board in an easy way.
You can rotate your stepper clockwise by using `rotate_clockwise(numberOfSteps)` or counterwise by
`rotate_counterwise(numberOfSteps)`. One step is a full cycle of an 4 or 8 sequence of 4 bit. The following code shows the 4 and 8 sequence which
are included in the module. As default `Seq2` is set.
```python
 		# Define simple sequence
        self.StepCount1 = 4
        self.Seq1 = []
        self.Seq1 = range(0, self.StepCount1)
        self.Seq1[0] = [1,0,0,0]
        self.Seq1[1] = [0,1,0,0]
        self.Seq1[2] = [0,0,1,0]
        self.Seq1[3] = [0,0,0,1]
        
        # Define advanced sequence
        # as shown in manufacturers datasheet
        self.StepCount2 = 8
        self.Seq2 = []
        self.Seq2 = range(0, self.StepCount2)
        self.Seq2[0] = [1,0,0,0]
        self.Seq2[1] = [1,1,0,0]
        self.Seq2[2] = [0,1,0,0]
        self.Seq2[3] = [0,1,1,0]
        self.Seq2[4] = [0,0,1,0]
        self.Seq2[5] = [0,0,1,1]
        self.Seq2[6] = [0,0,0,1]
        self.Seq2[7] = [1,0,0,1]
```


Stepper Control Usage
====================

```python
    import StepperControl.stepper
    import time
    
    # initialize GPIO24,GPIO25,GPIO8,GPIO7
    stepper = StepperControl.stepper.Stepper(24,25,8,7)
    # number of steps
    steps = 165

    while True:
       stepper.rotate_clockwise(steps)
       time.sleep(5)
       stepper.rotate_counterwise(steps)
```

Installation
==============================

To install this module as a system-wide python module, you can do it as follows:

```
git clone https://github.com/sbiermann/steppercontrol.git
cd steppercontrol
sudo python setup.py install
```