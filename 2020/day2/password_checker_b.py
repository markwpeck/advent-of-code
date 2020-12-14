from datetime import datetime
import re

startTime = datetime.now()
entry_pat = re.compile("^(?P<first_position>\d+)-(?P<second_position>\d+) (?P<letter>\w): (?P<password>\w+)$")
pass_db = open("passwords.txt", "r").readlines()
valid_entries = 0
invalid_entries = 0
for entry in pass_db:
	m = entry_pat.match(entry)
	first_position = int(m.group('first_position')) - 1
	second_position = int(m.group('second_position')) - 1
	letter = m.group('letter')
	password = m.group('password')
	if (password[first_position] == letter) and (password[second_position] != letter):
		valid_entries += 1
	elif(password[first_position] != letter) and (password[second_position] == letter):
		valid_entries += 1
	else:
		invalid_entries += 1
print('Found {} valid entries and {} invalid entries.'.format(valid_entries,invalid_entries))
print(datetime.now() - startTime)