'''
Using OpenCV takes a mp4 video and produces a number of images.
Requirements
----
You require OpenCV 3.2 to be installed.
Run
----
Open the main.py and edit the path to the video. Then run:
$ python main.py
Which will produce a folder called data with the images.
There will be 2000+ images for example.mp4.
'''
import cv2
import numpy as np
import os
import sys
sys.path.insert( 0, 'D:\Super-Resolution-master\SR_Project\Application')
import cnn


def handle_uploaded_file(testfile):
    print(testfile)
# Playing video from file:
    cap = cv2.VideoCapture(testfile)
    # print(type(testfile))
    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    currentFrame = 0
    while(True):

        # Capture frame-by-frame
        ret, frame = cap.read()
        if not ret: break
        # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.png'
        print('Creating...' + name)
        cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    cnn.process()





