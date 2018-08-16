import picamera
import time
from datetime import datetime

def now_string():
  return datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

def start():
  print("starting camera!")

def capture():
  timestamp = now_string()
  with picamera.PiCamera() as camera:
    camera.annotate_text = timestamp
    filename = '{}/{}.jpg'.format('project/static/photos', timestamp)
    camera.capture(filename)
    return filename

def video(seconds=10):
  timestamp = now_string()
  with picamera.PiCamera() as camera:
    camera.resolution = (640,480)
    filename = '{}/{}.mjpeg'.format('project/static/videos', timestamp)
    camera.start_recording(filename)
    camera.wait_recording(seconds)
    camera.stop_recording()
    return filename
