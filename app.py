from flask import Flask, render_template
import  cv2

app = Flask(__name__)
video_capture = cv2.VideoCapture(0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    frame = video_capture.read()
    return cv2.imshow('Video', frame)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, threaded=True)
