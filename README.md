python-scripts
==============

Various scripts for Web and Corona SDK mobile development.


makeicons
---------

Generates list of icons for use within mobile app development from image (iOS & Android).
Requires RMagick.

    makeicons.py [filename]


newproject
----------

Script to create new project based on following structure:

    newproject.py [project-name]
    
    - web
        - downloads html5boilerplate from git
    - corona
        - assets
            - downloads python-scripts from git
            - removes git files
        - [project-name]
            - downloads corona-boilerplate from git
            - copies /corona/assets/makeicons.py to /corona/[project-name]
            - removes git files
        - physics
        - distribution
            - v1.0

resizepng
---------

For dynamic image resizing using Texture Packer, Corona requires all HD assets must be 
dividable by 2 to even number at 100%, 50% and 25% to avoid blurring. 

This script resizes all PNGs in the current script folder and increases the width and 
height accordingly. Requires RMagick.
