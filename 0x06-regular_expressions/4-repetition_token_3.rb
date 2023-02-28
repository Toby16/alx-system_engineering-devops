#!/usr/bin/env ruby
# Regex that'll match 'hbn', 'hbtn', 'hbttn', 'hbtttn', 'hbtttttn', ...

puts ARGV[0].scan(/(hbn|hbt+n)/).join
