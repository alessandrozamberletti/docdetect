# docdetect

[![Build Status](https://travis-ci.org/alessandrozamberletti/docdetect.svg?branch=master)](https://travis-ci.org/alessandrozamberletti/docdetect)
[![Build status](https://ci.appveyor.com/api/projects/status/l1gjc8g7c1q3846j/branch/master?svg=true)](https://ci.appveyor.com/project/alessandrozamberletti/docdetect/branch/master)
[![codecov](https://codecov.io/gh/alessandrozamberletti/docdetect/branch/master/graph/badge.svg)](https://codecov.io/gh/alessandrozamberletti/docdetect)
[![Maintainability](https://api.codeclimate.com/v1/badges/a9aa496faab72437e650/maintainability)](https://codeclimate.com/github/alessandrozamberletti/docdetect/maintainability)
[![PyPI version](https://badge.fury.io/py/docdetect.svg)](https://badge.fury.io/py/docdetect)

<p align="center"> 
  <img src="./res/01.gif" alt="sample_01"/>
  <img src="./res/02.gif" alt="sample_02"/>
  <img src="./res/03.gif" alt="sample_03"/>
</p>

Simple real-time detection of documents in images using MSER, Canny Edge Detection, Hough Transform and Depth First Search.

# Installation

To install, use `pip` or `easy_install`:

```bash
$ pip install --upgrade docdetect
```
or
```bash
$ easy_install --upgrade docdetect
```

# Instructions

TBD

# Examples

Process an ```image```:
```python
import docdetect

rects = docdetect.process(image)
image = docdetect.draw(rects, image)
```

Process a ```video```:

```python
import cv2
import docdetect

video = cv2.VideoCapture(video_path)
cv2.startWindowThread()
cv2.namedWindow('output')
while video.isOpened():
    ret, frame = video.read()
    if ret:
        rects = docdetect.process(frame)
        frame = docdetect.draw(rects, frame)
        cv2.imshow('output', frame)
        cv2.waitKey(1)
video.release()
```

# Resources  
* [Fast and Accurate Document Detection for Scanning](https://blogs.dropbox.com/tech/2016/08/fast-and-accurate-document-detection-for-scanning/)
