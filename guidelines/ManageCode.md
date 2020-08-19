# Dice

## Add and Manage Options

**In the file [constant_options.py](../dice/options/constant_options.py)**

Add the letter keyletter to the apropriated string, whether it requires a number or argument inputed by the user or not

Be wary if the new keyletter is added in the *OptionsWithNumber* or in the middle of *OptionsOutNumber* as you will need to be careful in the next steps

**In the file [dice_main.py](../dice/dice_main.py)**

The Function *processoptionsReturnFinalStatement* calls each 