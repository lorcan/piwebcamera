import os

from flask import Flask, flash, redirect, render_template, url_for

import camera

from . import app


def get_photos():
  filenames = os.listdir('project/static/photos')
  photo_filenames = []
  for filename in filenames:
    if filename.endswith(".png"):
      photo_filenames.append('photos/' + filename)
  return photo_filenames

@app.route("/")
def index():
  photos = get_photos()
  return render_template('index.html', photos=photos)

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
