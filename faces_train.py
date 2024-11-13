import cv2 as cv
import numpy as np
import os

# List of people
p = []
for i in os.listdir(r'E:\\Courses\\OpenCV freeCodeCamp\\opencv-course-master\\Resources\\Faces\\train'):
    p.append(i)

print(p)
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

# Default dir
DIR = r'E:\\Courses\\OpenCV freeCodeCamp\\opencv-course-master\\Resources\\Faces\\train'

# Load Haar Cascade pre-trained model
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# List of image arrays and labels
features = []
labels = []

# Face detection function
def create_train():
    '''Function finds path of each folder and each image inside the folder. 
    Loops over each image, converts to grayscale and detects face using Haar Cascades.
    Finds the region of interest from the image to return a list of array of image
    called features and corresponding labels'''
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)


# Run create_train function
create_train()
print('Training done----------------')

# Convert features and labels list to numpy arrays
features = np.array(features, dtype='object')
labels = np.array(labels)

# Initiate face recognizer using Local Binary Patterns Histogram algorithm
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train face recognizer on features and labels list
face_recognizer.train(features, labels)

# Save model
face_recognizer.save('face_trained.yml')
np.save('Features.npy', features)
np.save('Labels.npy', labels)





