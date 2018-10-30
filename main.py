######### Seyhan Van Khan
######### Celebrity Facial Recognition
######### Tells you who a given picture is of, given several possible famous people's name, with facial recognition & google images
######### Python 2.7

################################### CONSTANTS ##################################


# Rename this to your picture's file name
PIC_FILE_NAME = "unknownperson.jpg"

# Number of pictures downloaded of each person
NUM_IMAGES = 20

# Cascade used to detect faces
CASCADE_NAME = 'haarcascade_frontalface_default.xml'

# Face Recogniser function used (choice of 3)
FACE_RECOGNIZER_FUNC = 1
'''
1 : Local Binary Patterns Histogram (LBPH)
2 : EigenFace Recognizer
3 : FisherFace Recognizer
'''


################################### LIBRARIES ##################################


import cv2
import numpy as np

from facefunctions import *
from searchimages import *

# your-picture folder: the folder containing the image the user wants to find the face of
# training-data folder: each sub folder is multiple pics of the same person, providing training data for facial recognition


########################### PREPARING TRAINING DATA ############################


subjects = GetImages(NUM_IMAGES)

print("All training data downloaded.")
raw_input("You may check the pictures now for any incorrect if you wish. Hit enter to continue. ")

print("Preparing training data")
faces, labels = prepare_training_data("training-data", CASCADE_NAME)

print("Total faces : " + str(len(faces)))
print("Total labels: " + str(len(labels)))


############################# TRAIN FACE RECOGNISER ############################


if FACE_RECOGNIZER_FUNC == 1:
    # Local Binary Patterns Histogram (LBPH)
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

elif FACE_RECOGNIZER_FUNC == 2:
    # EigenFace Recognizer:
    face_recognizer = cv2.face.EigenFaceRecognizer_create()

else:
    # FisherFace Recognizer:
    face_recognizer = cv2.face.FisherFaceRecognizer_create()

"""
OpenCV accepts 2 vectors:
1: People's faces
2: Respective integer labels for each face

Eg:

PERSON-1    PERSON-2
img1        img1
img2        img2

FACES                        LABELS
person1_img1_face              1
person1_img2_face              1
person2_img1_face              2
person2_img2_face              2

Train face recognizer method: train(faces_vector, labels_vector)
"""
face_recognizer.train(faces, np.array(labels))


################################## PREDICTION ##################################


print("Predicting image...")

# Load test image
test_img = cv2.imread("your-picture/" + PIC_FILE_NAME)

# Make a prediction
predicted_img, name = predict(test_img, face_recognizer, subjects, CASCADE_NAME)

# Display image
cv2.imshow(name, cv2.resize(predicted_img, (400, 500)))
print("\nAh of course, it was " + name + "!\n")

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
cv2.destroyAllWindows()

################# www.github.com/seyhanvankhan/celebrity-recog #################
