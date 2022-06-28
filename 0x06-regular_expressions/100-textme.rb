#!/usr/bin/env ruby

puts ARGV[0].scan(/(?<=from:).+?(?=\])/).join
puts ARGV[0].scan(/(?<=to:).+?(?=\])/).join
puts ARGV[0].scan(/(?<=flags:).+?(?=\])/).join
