#!/usr/bin/env ruby
#
# Check if the script is provided with the correct number of arguments
if ARGV.length != 1
  puts "Usage: #{$PROGRAM_NAME} 'log_entry'"
  exit 1
end
# Extract relevant information from the log entry using regular expressions
log_entry = ARGV[0]
match_data = log_entry.match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
# Check if the log entry matches the expected format
if match_data.nil?
  puts "Invalid log entry format."
  exit 1
end
# Extract sender, receiver, and flags from the match data
sender = match_data[1]
receiver = match_data[2]
flags = match_data[3]
# Output the result in the specified format
puts "#{sender},#{receiver},#{flags}"
