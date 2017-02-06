from flask import Flask, render_template, request
from functions import *

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/identifyscale', methods = ['POST', 'GET'])
def identifyscale():
	if request.method == 'POST':
		scale = request.form['scale']
		root = request.form['root']
		if scale == 'Major':
			result = major_scale(root)
		elif scale == 'Natural Minor':
			result = minor_scale(root)
		elif scale == 'Harmonic Minor':
			result = harmonic_minor(root)
		elif scale == 'Melodic Minor':
			result = melodic_minor(root)
		elif scale == 'Pentatonic Major':
			result = pentatonic_major(root)
		elif scale == 'Pentatonic Minor':
			result = pentatonic_minor(root)
		return render_template("identifyscale.html", 
			scale = scale,
			root = root,
			result = result)
	return render_template('identifyscale.html')

@app.route('/convertscale', methods = ['POST', 'GET'])
def convertscale():
	if request.method == 'POST':
		convert = request.form['convert']
		scale = request.form['scale']
		if convert == 'major2minor':
			result = major_to_minor(scale)
		elif convert == 'minor2major':
			result = minor_to_major(scale)
		elif convert == 'pentmajor2minor':
			result = major_to_minor_pent(scale)
		elif convert == 'pentminor2major':
			result = minor_to_major_pent(scale)
		return render_template("convertscale.html",
			convert = convert,
			scale = scale, 
			result = result)
	return render_template('convertscale.html')

@app.route('/buildchord', methods = ['POST', 'GET'])
def buildchord():
	if request.method == 'POST':
		chord = request.form['chord']
		root = request.form['root']
		if chord == 'Major':
			result = major_chord(root)
		elif chord == 'Natural Minor':
			result = minor_chord(root)
		return render_template("buildchord.html", result = result)
	return render_template('buildchord.html')

@app.route('/buildinterval', methods = ['POST', 'GET'])
def buildinterval():
	if request.method == 'POST':
		note = request.form['note']
		quality = request.form['quality']
		distance = request.form['distance']
		if note[-1] == "#":
			result = interval_sharp(note,quality,distance)
		elif note[-1] == "b":
			result = interval_flat(note,quality,distance)
		else:
			result = interval_natural(note,quality,distance)
		return render_template("buildinterval.html", result = result)
	return render_template('buildinterval.html')

@app.route('/privacypolicy')
def privacypolicy():
	return render_template('privacypolicy.html')

@app.route('/termsofservice')
def termsofservice():
	return render_template('termsofservice.html')

@app.route('/aboutpage')
def aboutpage():
	return render_template('aboutpage.html')

if __name__ == "__main__":
	app.run()