def morsecode(char):
	if char == 'a':
		return ".-"
	elif char == 'b':
		return "-..."
	elif char == 'c':
		return "-.-."
	elif char == 'd':
		return "-.."
	elif char == 'e':
		return "."
	elif char == 'f':
		return "..-."
	elif char == 'g':
		return "--."
	elif char == 'h':
		return "...."
	elif char == 'i':
		return ".."
	elif char == 'j':
		return ".---"
	elif char == 'k':
		return "-.-"
	elif char == 'l':
		return ".-.."
	elif char == 'm':
		return "--"
	elif char == 'n':
		return "-."
	elif char == 'o':
		return "---"
	elif char == 'p':
		return ".--."
	elif char == 'q':
		return "--.-"
	elif char == 'r':
		return ".-."
	elif char == 's':
		return "..."
	elif char == 't':
		return "-"
	elif char == 'u':
		return "..-"
	elif char == 'v':
		return "...-"
	elif char == 'w':
		return ".--"
	elif char == 'x':
		return "-..-"
	elif char == 'y':
		return "-.--"
	elif char == 'z':
		return "--.."
	else:
		return "0"

def decode(string):
	code = ""
	for i in string:
		code = code + morsecode(i)
	return code

def count(lst):
	count = {}
	for i in lst:
		code = decode(i)
		if code in count:
			count[code] += 1
		else:
			count[code] = 1
	return len(count)

print(count(["gin", "zen", "gig", "msg"]))
print(count(["a", "z", "g", "m"]))
print(count(["bhi", "vsv", "sgh", "vbi"]))
print(count(["a", "b", "c", "d"]))
print(count(["hig", "sip", "pot"]))