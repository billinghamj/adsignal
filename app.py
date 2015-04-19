from flask import Flask, render_template
import json
app = Flask(__name__)

@app.route("/")
def show_root():
	return render_template('root.html')

@app.route("/videos/")
def show_videos():
	return render_template('videos.html')

@app.route("/videos/<int:video_id>/")
def show_video(video_id):
	return render_template('video.html')

@app.route("/videos/<int:video_id>/test/")
def show_test(video_id):
	return render_template('test.html')

@app.route("/videos/<int:video_id>/results/")
def show_results(video_id):
	return render_template('results.html')

@app.route("/videos/<int:video_id>/results/<int:result_id>/")
def show_result(video_id, result_id):
	file = open('./data/videos/' + str(video_id) + '/results/' + str(result_id) + '/data.json', 'r')
	return render_template('result.html', result=json.load(file))

if __name__ == "__main__":
	app.run(debug=True)
