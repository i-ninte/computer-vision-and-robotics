import cv2 as cv
import os
import numpy as np

# Define the list of people and the directory containing the training images
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfeld', 'Madonna', 'Mindy Kaling']
dir = r'D:\ROBOTICS AND COMPUTER VISION\CODE\Face Detector\Resources\Faces\train'

# Check and list the directories for each person
p = [i for i in os.listdir(dir) if os.path.isdir(os.path.join(dir, i))]
print(p)

features = []
labels = []

# Load the Haar Cascade file
haar_cascade_path = 'haar_face.xml'  # Ensure the correct path to haar_face.xml
haar_cascade = cv.CascadeClassifier(haar_cascade_path)

if haar_cascade.empty():
    print("Error loading Haar Cascade file. Check the file path.")
    exit()

def create_train():
    for person in p:
        path = os.path.join(dir, person)
        label = p.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            # Read the image
            img_array = cv.imread(img_path)
            if img_array is None:
                print(f"Error reading image {img_path}")
                continue

            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            # Detect faces
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

    # Convert lists to numpy arrays and save them
    features_np = np.array(features, dtype='object')
    labels_np = np.array(labels, dtype='int')
    print('Training Done')

    np.save('features.npy', features_np)
    np.save('labels.npy', labels_np)

# Create the training data
create_train()
print("Training data created")

# Load the saved data
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy')

# Create the face recognizer and train it
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train recognizer on the features list and the labels list
face_recognizer.train(features, labels)
print("Training complete")



face_recognizer.save('face_trained.yml')