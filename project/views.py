import os

from flask import Flask, flash, redirect, render_template, url_for
import camera
from . import app

def get_paths_from_directory_with_suffix(directory, suffix):
  paths = []
  for filename in os.listdir('project/static/' + directory):
    if filename.endswith(suffix):
      paths.append(directory + '/' + filename)
  return paths

@app.route("/")
def index():
  photos = get_paths_from_directory_with_suffix('photos', '.jpg')
  videos = get_paths_from_directory_with_suffix('videos', 'mjpeg')
  return render_template('index.html', photos=photos, videos=videos)

@app.route("/capture/", methods=['POST'])
def capture():
  camera.capture()
  flash('Successfully took a picture')
  return redirect(url_for('index'))

@app.route("/start/", methods=['POST'])
def start():
  camera.start()
  flash('Successfully started the camera')
  return redirect(url_for('index'))

@app.route("/video/", methods=['POST'])
def video():
  camera.video(10)
  flash('Successfully took a video')
  return redirect(url_for('index'))
