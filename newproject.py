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


# @title:       New Corona SDK project script
# @author:      Christopher Martin, Hey Topher
# @description: Create a new corona project based on project setup
#               using html5 boilerplate, corona boilerplate and python scripts
# @version:     1.0

# rvm use 2.0.0
# sudo gem install git

require 'rubygems'
require 'git'


# Throw error if filename not supplied
if (ARGV[0].to_s == "")
    puts "Error: Project name not specified"
    puts "Usage: ruby newproject.py -- projectname"
    exit
end

puts 'Building new ' + ARGV[0].to_s + ' project...'
puts 'Creating /web folder'
puts 'Cloning https://github.com/h5bp/html5-boilerplate.git'
Git.clone('https://github.com/h5bp/html5-boilerplate.git', 'web', :repository => true)
puts 'Success!'

Dir.mkdir("corona");
Dir.chdir("corona");
puts "Creating /corona folder"

puts "Creating /corona/assets folder"
puts "Cloning https://github.com/HeyTopher/python-scripts.git"
Git.clone('https://github.com/HeyTopher/python-scripts.git', 'assets', :index => 'resizepng.py')
puts 'Success!'

puts "Cloning https://github.com/HeyTopher/corona-boilerplate.git"
Git.clone('https://github.com/HeyTopher/corona-boilerplate.git', ARGV[0].to_s, :repository => true)
puts 'Success!'

puts "Creating /corona/physics folder"
Dir.mkdir("physics");

puts "Creating /corona/distribution folder"
Dir.mkdir("distribution");

puts "Creating /corona/distribution/v1.0 folder"
Dir.chdir("distribution");
Dir.mkdir("v1.0");
Dir.chdir("../../");

puts "Copying makeicons.py to " + ARGV[0].to_s + " folder "
FileUtils.mv 'corona/assets/makeicons.py', "corona/" + ARGV[0].to_s + '/makeicons.py'

puts "Cleanup"
FileUtils.rm %w(web/humans.txt)
FileUtils.rm Dir.glob('web/*.md')
FileUtils.rm Dir.glob('corona/assets/*.md')
FileUtils.rm Dir.glob('corona/assets/LICENSE')
FileUtils.rm Dir.glob('corona/' + ARGV[0].to_s + '/*.md')
FileUtils.rm Dir.glob('corona/' + ARGV[0].to_s + '/LICENSE')

puts "Setup complete!"