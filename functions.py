#This file contains all the music-theory-related variables and functions for our Music Mentor app
#This file is imported to app.py

notes = ["A","B","C","D","E","F","G"]
key_sig = {"F":-1,"C":0,"G":1,"D":2,"A":3,"E":4,"B":5,}

def major_scale(scale):
	if scale == "A":
		return "A B C# D E F# G# A"
	elif scale == "A#" or scale == "Bb":
		return "Bb C D Eb F G A Bb"
	elif scale == "B":
		return "B C# D# E F# G# A# B"
	elif scale == "C":
		return "C D E F G A B C"
	elif scale == "C#" or scale == "Db":
		return "Db Eb F Gb Ab Bb C Db"
	elif scale == "D":
		return "D E F# G A B C# D"
	elif scale == "D#" or scale == "Eb":
		return "Eb F G Ab Bb C D Eb"
	elif scale == "E":
		return "E F# G# A B C# D# E"
	elif scale == "F":
		return "F G A Bb C D E F"
	elif scale == "F#" or scale == "Gb":
		return "F# G# A# B C# D# E# F#"
	elif scale == "G":
		return "G A B C D E F# G"
	elif scale == "G#" or scale == "Ab":
		return "Ab Bb C Db Eb F G Ab"
	else:
		return "No such scale exists."

def minor_scale(scale):
	if scale == "A":
		return "A B C D E F G A"
	elif scale == "A#" or scale == "Bb":
		return "A# C C# D# F F# G# A#"
	elif scale == "B":
		return "B C# D E F# G A B"
	elif scale == "C":
		return "C D Eb F G Ab Bb C"
	elif scale == "C#" or scale == "Db":
		return "C# D# E F# G# A B C#"
	elif scale == "D":
		return "D E F G A Bb C D"
	elif scale == "D#" or scale == "Eb":
		return "D# F F# G# A# B C# D#"
	elif scale == "E":
		return "E F# G A B C D E"
	elif scale == "F":
		return "F G Ab Bb C Db Eb F"
	elif scale == "F#" or scale == "Gb":
		return "F# G# A B C# D E F#"
	elif scale == "G":
		return "G A Bb C D Eb F G"
	elif scale == "G#" or scale == "Ab":
		return "G# A# B C# D# E F# G#"
	else:
		return "No such scale exists."

def harmonic_minor(scale):
	if scale == "A":
		return "A B C D E F G# A"
	elif scale == "A#" or scale == "Bb":
		return "A# C C# D# F F# Gx A#"
	elif scale == "B":
		return "B C# D E F# G A# B"
	elif scale == "C":
		return "C D Eb F G Ab B C"
	elif scale == "C#" or scale == "Db":
		return "C# D# E F# G# A B# C#"
	elif scale == "D":
		return "D E F G A Bb C# D"
	elif scale == "D#" or scale == "Eb":
		return "D# F F# G# A# B Cx D#"
	elif scale == "E":
		return "E F# G A B C D# E"
	elif scale == "F":
		return "F G Ab Bb C Db E F"
	elif scale == "F#" or scale == "Gb":
		return "F# G# A B C# D E# F#"
	elif scale == "G":
		return "G A Bb C D Eb F# G"
	elif scale == "G#" or scale == "Ab":
		return "G# A# B C# D# E Fx G#"
	else:
		return "No such scale exists."

def melodic_minor(scale):
	if scale == "A":
		return "A B C D E F# (F) G# (G) A"
	elif scale == "A#" or scale == "Bb":
		return "A# C C# Eb F G (F#) A (G#) A#"
	elif scale == "B":
		return "B C# D E F# G# (G) A# (A) B"
	elif scale == "C":
		return "C D Eb F G A (Ab) B (Bb) C"
	elif scale == "C#" or scale == "Db":
		return "C# Eb E F# G# A# (A) C (B) C#"
	elif scale == "D":
		return "D E F G A B (Bb) C# (C) D"
	elif scale == "D#" or scale == "Eb":
		return "D# F F# G# A# C (B) D (C#) D#"
	elif scale == "E":
		return "E F# G A B C# (C) D# (D) E"
	elif scale == "F":
		return "F G Ab Bb C D (Db) E (Eb) F"
	elif scale == "F#" or scale == "Gb":
		return "F# G# A B C# Eb (D) F (E) F#"
	elif scale == "G":
		return "G A Bb C D E (Eb) F# (F) G"
	elif scale == "G#" or scale == "Ab":
		return "G# A# B C# Eb F (E) G (F#) G#"
	else:
		return "No such scale exists."

def pentatonic_minor(scale):
	if scale == "A":
		return "A C D E G A"
	elif scale == "A#" or scale == "Bb":
		return "A# C# D# E# G# A#"
	elif scale == "B":
		return "B D E F# A B"
	elif scale == "C":
		return "C Eb F G Bb C"
	elif scale == "C#" or scale == "Db":
		return "C# E F# G# B C#"
	elif scale == "D":
		return "D F G A C D"
	elif scale == "D#" or scale == "Eb":
		return "D# F# G# A# C# D#"
	elif scale == "E":
		return "E G A B D E"
	elif scale == "F":
		return "F Ab Bb C Eb F"
	elif scale == "F#" or scale == "Gb":
		return "F# A B C# E F#"
	elif scale == "G":
		return "G Bb C D F G"
	elif scale == "G#" or scale == "Ab":
		return "G# B C# D# F# G#"
	else:
		return "No such scale exists."

def pentatonic_major(scale):
	if scale == "A":
		return "A B C# E F# A"
	elif scale == "A#" or scale == "Bb":
		return "A# C D F G A#"
	elif scale == "B":
		return "B C# D# F# G# B"
	elif scale == "C":
		return "C D E G A C"
	elif scale == "C#" or scale == "Db":
		return "C D E G A C"
	elif scale == "D":
		return "D E F# A B D"
	elif scale == "D#" or scale == "Eb":
		return "D# F G A# C D#"
	elif scale == "E":
		return "E F# G# B C# E"
	elif scale == "F":
		return "F G A C D F"
	elif scale == "F#" or scale == "Gb":
		return "F# G# A# C# D# F#"
	elif scale == "G":
		return "G A B D E G"
	elif scale == "G#" or scale == "Ab":
		return "G# A# C D# F G#"
	else:
		return "No such scale exists."

#make a dictionary for conv
maj2min = {"C":"Am","C#":"Bbm","D":"Bm","D#":"Cm","E":"C#m","F":"Dm","F#":"Ebm","G":"Em","G#":"Fm","A":"F#m","A#":"Gm","B":"Abm"}

def major_to_minor(scale):
	if scale in maj2min:
		return ("The relative key for the {} major scale is the {} minor scale".format(scale,maj2min[scale]),
		 "The {} scale is {}".format(scale,major_scale(scale)),
		 "The {} scale is {}".format(maj2min[scale],minor_scale(maj2min[scale].replace("m",""))))
	else:
		return "No such scale exists."
def minor_to_major(scale):
	for major, minor in maj2min.iteritems():
		if (scale + "m") == minor:
			return ("The relative key for the {} minor scale is the {} major scale".format(scale,major),
			 "The {} scale is {}".format(scale,minor_scale(scale.replace("m",""))),
			 "The {} scale is {}".format(major,major_scale(major)))
	else:
		return "No such scale exists."

def major_to_minor_pent(scale):
	if scale in maj2min:
		return ("The relative key for the {} pentatonic major scale is the {} pentatonic minor scale\n".format(scale,maj2min[scale]),
		 "The {} scale is {}\n".format(scale,pentatonic_major(scale)),
		 "The {} scale is {}".format(maj2min[scale],pentatonic_minor(maj2min[scale].replace("m",""))))
	else:
		return "No such scale exists."
def minor_to_major_pent(scale):
	for major, minor in maj2min.iteritems():
		if (scale + "m") == minor:
			return ("The relative key for the {} pentatonic minor scale is the {} pentatonic major scale\n".format(scale,major),
			 "The {} scale is {}\n".format(scale,pentatonic_minor(scale.replace("m",""))),
			 "The {} scale is {}".format(major,pentatonic_major(major)))
	else:
		return "No such scale exists."

half_steps = {0:"C",1:"C#",2:"D",3:"D#",4:"E",5:"F",6:"F#",7:"G",8:"G#",9:"A",10:"A#",11:"B",12:"C",13:"C#",14:"D",15:"D#",16:"E",17:"F",18:"F#",19:"G",20:"G#",21:"A",22:"A#",23:"B"}
def major_chord(note):
	for num, root in half_steps.iteritems():
		if note == root:
			return "The major chord for {} is {} {} {}".format(root,root,half_steps[int(num)+4],half_steps[int(num)+7])
	else:
		return "No such chord exists."

def minor_chord(note):
	for num, root in half_steps.iteritems():
		if note == root:
			return "The natural minor chord for {} is {} {} {}".format(root,root,half_steps[int(num)+3],half_steps[int(num)+7])
	else:
		return "No such chord exists."

intervals = {
	0:["P1","d2"],
	1:["m2","A1"],
	2:["M2","d3"],
	3:["m3","A2"],
	4:["M3","d4"],
	5:["P4","A3"],
	6:["A4","d5"],
	7:["P5","d6"],
	8:["m6","A5"],
	9:["M6","d7"],
	10:["m7","A6"],
	11:["M7","d8"],
	12:["P8","A7"]
}

whole_steps = {0:"C",1:"D",2:"E",3:"F",4:"G",5:"A",6:"B",7:"C",8:"D",9:"E",10:"F",11:"G",12:"A",13:"B"}
whole_steps_sharps = {0:"C#",1:"D#",2:"E#",3:"F#",4:"G#",5:"A#",6:"B#",7:"C#",8:"D#",9:"E#",10:"F#",11:"G#",12:"A#",13:"B#"}
whole_steps_flats = {0:"Cb",1:"Db",2:"Eb",3:"Fb",4:"Gb",5:"Ab",6:"Bb",7:"Cb",8:"Db",9:"Eb",10:"Fb",11:"Gb",12:"Ab",13:"Bb"}
P = [1,4,5,8]
M = [2,3,6,7]

# works for any natural note entered
def interval_natural(note,quality,interval):
	if int(interval) in P:
		for num,root in whole_steps.iteritems():
			if note == root:
				for steps,inter in intervals.iteritems():
					if quality+str(interval) in inter:
						if quality == "A":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps[int(num)+int(interval)-1]+"#", steps)
						elif quality == "P":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps[int(num)+int(interval)-1], steps)
						elif quality == "d":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps[int(num)+int(interval)-1]+"b", steps)
						else:
							return "One of your inputs is incorrect."
	elif int(interval) in M:
		for num,root in whole_steps.iteritems():
			if note == root:
				for steps,inter in intervals.iteritems():
					if quality+str(interval) in inter:
						if quality == "A":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps[int(num)+int(interval)-1]+"#", steps)
						elif quality == "M":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps[int(num)+int(interval)-1], steps)
						elif quality == "m":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps[int(num)+int(interval)-1]+"b", steps)
						elif quality == "d":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps[int(num)+int(interval)-1]+"bb", steps)
						else:
							return "One of your inputs is incorrect."		
	else:
		return "One of your inputs is incorrect."

def interval_sharp(note,quality,interval):
	if int(interval) in P:
		for num,root in whole_steps_sharps.iteritems():
			if note == root:
				for steps,inter in intervals.iteritems():
					if quality+str(interval) in inter:
						if quality == "A":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_sharps[int(num)+int(interval)-1]+"x", steps)
						elif quality == "P":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_sharps[int(num)+int(interval)-1], steps)
						elif quality == "d":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_sharps[int(num)+int(interval)-1].replace("#",""), steps)
						else:
							return "One of your inputs is incorrect."
	elif int(interval) in M:
		for num,root in whole_steps_sharps.iteritems():
			if note == root:
				for steps,inter in intervals.iteritems():
					if quality+str(interval) in inter:
						if quality == "A":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_sharps[int(num)+int(interval)-1].replace("#","x"), steps)
						elif quality == "M":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_sharps[int(num)+int(interval)-1], steps)
						elif quality == "m":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_sharps[int(num)+int(interval)-1].replace("#",""), steps)
						elif quality == "d":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_sharps[int(num)+int(interval)-1].replace("#","b"), steps)
						else:
							return "One of your inputs is incorrect."
	else:
		return "One of your inputs is incorrect."

def interval_flat(note,quality,interval):
	if int(interval) in P:
		for num,root in whole_steps_flats.iteritems():
			if note == root:
				for steps,inter in intervals.iteritems():
					if quality+str(interval) in inter:
						if quality == "A":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_flats[int(num)+int(interval)-1].replace("b",""), steps)
						elif quality == "P":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_flats[int(num)+int(interval)-1], steps)
						elif quality == "d":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_flats[int(num)+int(interval)-1]+"b", steps)
						else:
							return "One of your inputs is incorrect."
	elif int(interval) in M:
		for num,root in whole_steps_flats.iteritems():
			if note == root:
				for steps,inter in intervals.iteritems():
					if quality+str(interval) in inter:
						if quality == "A":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_flats[int(num)+int(interval)-1].replace("b",""), steps)
						elif quality == "M":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_flats[int(num)+int(interval)-1], steps)
						elif quality == "m":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_flats[int(num)+int(interval)-1].replace("#","bb"), steps)
						elif quality == "d":
							return "The {} interval for {} is {} to {} with {} half steps".format(quality+str(interval),note,note,whole_steps_flats[int(num)+int(interval)-1].replace("#","bbb"), steps)
						else:
							return "One of your inputs is incorrect."	
	else:
		return "One of your inputs is incorrect."	
