# Regular Expression Project - 0x06

## Overview
This project focuses on mastering regular expressions using the Oniguruma library, commonly used in Ruby. The tasks involve creating Ruby scripts that leverage regular expressions to match specific patterns. The project is scheduled to start on Jan 30, 2024, at 6:00 AM and must conclude by Jan 31, 2024, at 6:00 AM. The checker will be released on Jan 30, 2024, at 12:00 PM, with an auto review launched at the deadline.

## Concepts
The primary concept explored in this project is Regular Expressions. Participants are expected to familiarize themselves with Oniguruma and use it to build regular expressions. A sample Ruby code is provided as a reference, demonstrating the usage of regular expressions with Oniguruma.

```ruby
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
```

## Resources
- [Regular expressions - basics](https://www.slideshare.net/neha_jain/introducing-regular-expressions)
- [Regular expressions - advanced](https://www.slideshare.net/neha_jain/advanced-regular-expressions-80296518)
- [Rubular](https://rubular.com/) - a helpful tool for testing and debugging regular expressions
- [Use a regular expression against a problem: now you have 2 problems](https://blog.codinghorror.com/regular-expressions-now-you-have-two-problems/)
- [Learn Regular Expressions with simple, interactive exercises](https://regexone.com/)

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files interpreted on Ubuntu 20.04 LTS
- All files end with a new line
- A mandatory README.md file at the root of the project folder
- All Bash scripts must be executable
- The first line of all Bash scripts should be `#!/usr/bin/env ruby`
- All regular expressions must be built for the Oniguruma library

## Tasks
### 0. Simply matching School
- Script: `0-simply_match_school.rb`
- Requirements:
  - Match the regular expression to "School"
  - Accept one argument and pass it to a regular expression matching method

### 1. Repetition Token #0
- Script: `1-repetition_token_0.rb`
- Requirements:
  - Find the regular expression that matches specified cases
  - Accept one argument and pass it to a regular expression matching method

### 2. Repetition Token #1
- Script: `2-repetition_token_1.rb`
- Requirements:
  - Find the regular expression that matches specified cases
  - Accept one argument and pass it to a regular expression matching method

### 3. Repetition Token #2
- Script: `3-repetition_token_2.rb`
- Requirements:
  - Find the regular expression that matches specified cases
  - Accept one argument and pass it to a regular expression matching method

### 4. Repetition Token #3
- Script: `4-repetition_token_3.rb`
- Requirements:
  - Find the regular expression that matches specified cases
  - Accept one argument and pass it to a regular expression matching method
  - The regex should not contain square brackets

### 5. Not quite HBTN yet
- Script: `5-beginning_and_end.rb`
- Requirements:
  - Match a string that starts with "h," ends with "n," and can have any single character in between
  - Accept one argument and pass it to a regular expression matching method

### 6. Call me maybe
- Script: `6-phone_number.rb`
- Requirements:
  - Match a 10-digit phone number
  - Accept one argument and pass it to a regular expression matching method

### 7. OMG WHY ARE YOU SHOUTING?
- Script: `7-OMG_WHY_ARE_YOU_SHOUTING.rb`
- Requirements:
  - Match only capital letters in a given string
  - Accept one argument and pass it to a regular expression matching method

## Copyright
© 2024 ALX, All rights reserved.
