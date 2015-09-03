$stdout.sync = true

require 'faker'

while true
  puts "Hello #{Faker::Internet.email}"
  sleep 1
end
