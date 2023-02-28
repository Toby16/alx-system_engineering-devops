#!/usr/bin/env ruby
# Regex that'll match a string that starts with 'h' and 'n' and can have any single character in-between

puts ARGV[0].scan(/h.n/).join
