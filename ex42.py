class laserWeaaponArmory(scenr):
	
	def enter(self):
		print "You do a dive roll in  a weapon armory, crouch and scan the room."
		print "for more gothons that might be hiding. It's dead quiet, too quiet"
		print "You stand up and run to the far side of the room and find the"
		print "neutron bomb in the container. There's is keypad lock on the box"
		print "and you need a code to get the bomb out. If you get the code"
		print "wrong 10 times  then the lock closes forevr and you cant get the bomb."
		print "The code is three digits"
		code = "%d%d%d" %(randint(1,9), randint(1,9), randint(1,9)
		guess = raw_input("[keypad]>")
		guesses = 0
		
		while guess != code and guesses < 10:
			print "BZZZZZEDDD"
			guesses += 1
			guess = raw_input("[keypad]> ")
			
		if guess == code:
			print "The container clicks open and the seal breaks, letting gas out"
			print "you grab the neutron bomb run as fast as you can to the"
			print "bridge where you must place it in the right spot"
			return 'the_bridge'
			
		else:
			print
		