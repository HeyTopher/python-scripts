# Copyright (c) 2013 Christopher Martin / Hey Topher

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# @title:       Mobile app icon generator
# @author:      Christopher Martin, Hey Topher
# @description: Generates list of icons for use within mobile app development (iOS & Android)
# @version:     1.0

# rvm use 2.0.0
# gem install rmagick
# bundle install

require 'rubygems'
require 'RMagick'
include Magick


# Throw error if filename not supplied
if (ARGV[0].to_s == "")
    puts "Error: No image specified!"
    puts "Usage: ruby makeicons.py -- filename"
    exit
end

# Throw error if filename does not exist
if (File.exist?(ARGV[0].to_s) == false) 
    puts "Error: '" + ARGV[0].to_s + "' does not exist!"
    puts "Usage: ruby makeicons.py -- filename"
    exit    
end

# Curent icon set
iconset = [
    {:width => 60, :height => 60, :filename => "Icon-60.png"},
    {:width => 120, :height => 120, :filename => "Icon-60@2x.png"},
    {:width => 72, :height => 72, :filename => "Icon-72.png"},
    {:width => 76, :height => 76, :filename => "Icon-76.png"},
    {:width => 152, :height => 152, :filename => "Icon-76@2x.png"},
    {:width => 120, :height => 120, :filename => "Icon-120.png"},
    {:width => 512, :height => 512, :filename => "Icon-512.png"},
    {:width => 72, :height => 72, :filename => "Icon-hdpi.png"},
    {:width => 36, :height => 36, :filename => "Icon-ldpi.png"},
    {:width => 48, :height => 48, :filename => "Icon-mdpi.png"},
    {:width => 57, :height => 57, :filename => "Icon.png"},
    {:width => 114, :height => 114, :filename => "Icon@2x.png"}    
]

# For each item in iconset - load filename, resize to item width & height and save as item filename
iconset.each do |item|
    image = Magick::Image.read(ARGV[0].to_s).first
    image.resize(item[:width], item[:height]).write(item[:filename])
    puts "Generating: '" + item[:filename] + "' -> " + item[:width].to_s + "x" + item[:height].to_s
end