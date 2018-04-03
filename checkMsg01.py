import gmail, time # import modules

g = gmail.login('yvan.esc@gmail.com', 're23coule')
unread_messages = g.inbox().mail(unread=True)
total_messages = 0

for message in unread_messages:
	total_messages += 1

if total_messages > 0:
	# there are unread emails, turn light on
	#GPIO.output(14, True)
	print ("New unread msg")
#else:
	# there are no unread emails, turn light off
	#GPIO.output(14, False)
