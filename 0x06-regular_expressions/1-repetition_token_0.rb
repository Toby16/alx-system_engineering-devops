#!/usr/bin/env ruby
# Regex that'll match: 'hbttn', 'hbtttn', 'hbttttn', 'hbtttttn' only

puts ARGV[0].scan(/hbt{2,5}n/).join
