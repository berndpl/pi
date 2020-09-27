#!/usr/bin/ruby
#encoding: utf-8

list =  [   
			['Quit', 'q'], 
			['Display Time', 'display "$(timestamp)"'],
			['Display Speed','display "$(speed)"'],
			['Display IP','display "$(ipaddress)"'],			
			['System Log','sudo tail -f /var/log/syslog'],
			['Reboot','display "Restarting…" && sudo reboot'],
			['🛑 Shutdown','display "x $(timestamp)" && sudo halt']
]

i = 0

list.each do |command|
	print "\n [#{i}] #{command[0]}"
	i = i + 1
end 

puts "\n\n Yes, please ..."

tty_param = `stty -g`
system 'stty raw'
input = IO.read '/dev/stdin', 1
system "stty #{tty_param}"

selection = input.to_i

if selection == 0
	puts "Nevermind, bye."
	exit
end

selectedCommand = list[selection][1]
print "\r → #{selectedCommand} \r"
system(selectedCommand)
exit
