from flask import Flask, render_template
from os import listdir
from os.path import isdir, join
import json
app = Flask(__name__)

@app.route("/")
def show_root():
	return render_template('root.html')

@app.route("/videos/")
def show_videos():
	path = './data/videos/'
	dirs = [ f for f in listdir(path) if isdir(join(path, f)) ]
	videos = []
	for f in dirs:
		x = json.load(open(join(path, f, 'data.json'), 'r'))
		x['id'] = f
		videos.append(x)
	return render_template('videos.html', videos=videos)

@app.route("/videos/<int:video_id>/")
def show_video(video_id):
	video = json.load(open('./data/videos/' + str(video_id) + '/data.json', 'r'))
	video['id'] = video_id
	return render_template('video.html', video=video)

@app.route("/videos/<int:video_id>/test/")
def show_test(video_id):
	video = json.load(open('./data/videos/' + str(video_id) + '/data.json', 'r'))
	video['id'] = video_id
	return render_template('test.html', video=video)

@app.route("/videos/<int:video_id>/results/")
def show_results(video_id):
	video = json.load(open('./data/videos/' + str(video_id) + '/data.json', 'r'))
	video['id'] = video_id
	path = './data/videos/' + str(video_id) + '/results/'
	dirs = [ f for f in listdir(path) if isdir(join(path, f)) ]
	results = []
	for f in dirs:
		x = json.load(open(join(path, f, 'data.json'), 'r'))
		x['id'] = f
		results.append(x)
	return render_template('results.html', results=results, video=video)

@app.route("/videos/<int:video_id>/results/<int:result_id>/")
def show_result(video_id, result_id):
	video = json.load(open('./data/videos/' + str(video_id) + '/data.json', 'r'))
	video['id'] = video_id
	path = './data/videos/' + str(video_id) + '/results/' + str(result_id) + '/data.json'
	result = json.load(open(path, 'r'))
	return render_template('result.html', result=result, video=video)

if __name__ == "__main__":
	app.run(debug=True)
