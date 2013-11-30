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


# @title:       PNG image resizer
# @author:      Christopher Martin, Hey Topher
# @description: For dynamic image resizing, Corona requires all HD (@4x) assets 
#               to be dividable by 2 to even number at @4x, @2x and @1x.
#               This script checks files and increases the width and height of a folder.
# @version:     1.0

# rvm use 2.0.0
# sudo gem install rmagick
# bundle install


require 'rubygems'
require 'RMagick'
include Magick


# Function to resize image to be evenly diviable 3 times  
def round_to_factorial4(value)
    c = 0
	value += (value % 2);
    while c < 3
        if value / 2 % 4 != 0
            value += 2
            c = 0
        else
            c += 1
        end
    end  
   return value
end

# For each PNG image in folder
Dir.glob('*.png') do |rb_file|

    # Get image object
    img = Magick::Image.read(rb_file)

    # Calculate factorial width and height
    w = round_to_factorial4(img[0].columns)
    h = round_to_factorial4(img[0].rows)
        
    # Only resize to fill if width/height has changed as result of calculation
    if img[0].columns != w || img[0].rows != h

		# Create new transparent image, extend crop and save
		thumb = Magick::ImageList.new(rb_file)
		thumb.background_color = "Transparent"
		thumb.extent(w, h, -((w - img[0].columns) / 2).ceil, -((h - img[0].rows) / 2).ceil).write(rb_file)

		puts "Resizing: '" + rb_file + "' " + img[0].columns.to_s + " -> " + w.to_s + "; " + img[0].rows.to_s + " -> " + h.to_s
	else
		puts "Ignoring: '" + rb_file + "' " + img[0].columns.to_s + " x " + img[0].rows.to_s
    end        
end