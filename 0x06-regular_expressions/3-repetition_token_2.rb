#!/usr/bin/env ruby
# Regex that'll match: 'hbtn', 'hbttn', 'hbtttn', 'hbttttn', ...

puts ARGV[0].scan(/hbt+n/).join
