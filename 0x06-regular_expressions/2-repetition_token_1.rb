#!/usr/bin/env ruby
# Regex that'll match: 'htn', 'hbtn' only

puts ARGV[0].scan(/hb?tn/).join
