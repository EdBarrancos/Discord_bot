# Dice

## Add and Manage Options

### StepOne

**In the file [constant_options.py](../dice/options/constant_options.py)**

Add the letter keyletter to the apropriated string, whether it requires a number or argument inputed by the user or not

Be wary if the new keyletter is added in the *OptionsWithNumber* or in the middle of *OptionsOutNumber* as you will need to be careful in the next steps

### StepTwo

**In the file [options_impl.py](../dice/options/options_impl.py)**

Add the new option to the Enum *Options* and make sure the values are curresponding to the indexes of *AllOptions* in [constant_options.py](../dice/options/constant_options.py)

Create the treatment routine for the new option. It returns the an instance of the class *processedOutput*. Make sure you initialize the values you will be using.

### StepThree

**In the file [dice_main.py](../dice/dice_main.py)**

The Function *processoptionsReturnFinalStatement* calls each treatment routine

Add a if statement testing if the current *optionIndex* being checked curresponds to the Enum *Options* of your in the process of creation option

Add a *final = treatment routine*
