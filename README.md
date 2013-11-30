Python Scripts
==============


makeicons
---------

Generates list of icons for use within mobile app development from image (iOS & Android).
Requires RMagick

    makeicons.py filename


resizepng
---------

For dynamic image resizing using Texture Packer, Corona requires all HD assets must be 
dividable by 2 to even number at 100%, 50% and 25% to avoid blurring. 

This script resizes all PNGs in the current script folder and increases the width and 
height accordingly. Requires RMagick