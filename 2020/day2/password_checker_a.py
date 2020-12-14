from datetime import datetime
import re

startTime = datetime.now()
entry_pat = re.compile("^(?P<mincount>\d+)-(?P<maxcount>\d+) (?P<letter>\w): (?P<password>\w+)$")
pass_db = open("passwords.txt", "r").readlines()
valid_entries = 0
invalid_entries = 0
for entry in pass_db:
	m = entry_pat.match(entry)
	mincount = int(m.group('mincount'))
	maxcount = int(m.group('maxcount'))
	letter = m.group('letter')
	password = m.group('password')
	occurrences = password.count(letter)
	if (occurrences <= maxcount) and (occurrences >= mincount):
		valid_entries += 1
	else:
		invalid_entries += 1
print('Found {} valid entries and {} invalid entries.'.format(valid_entries,invalid_entries))
print(datetime.now() - startTime)