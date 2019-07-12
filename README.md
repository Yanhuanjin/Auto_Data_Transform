# Auto_Data_Transform
A script to transform .csv file (containing strings) to fully digital .csv

Usage: python auto_data_transform.py *target*.csv

OUT: *target_out*.csv

## Example 1

Here I download a sheet online, and it looks like this in *pandas*:

<img src= "img/input.png"  height="300">

And after performing auto_data_transform, it will be like this:

<img src= "img/output.png" height="230">

Note: The date data form has been transfered into day_of_year

## Example 2

An input file like this,

<img src="img/input_2.png">

And the output file like this,

<img src="img/output_2.png" height=230>