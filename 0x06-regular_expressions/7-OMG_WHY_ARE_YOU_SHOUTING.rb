#!/usr/bin/env ruby
# Regex that matches: CAPITAL/UPPERCASE LETTERS only

puts ARGV[0].scan(/[A-Z]/).join
