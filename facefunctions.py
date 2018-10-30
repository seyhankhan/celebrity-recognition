######### Seyhan Van Khan
######### Facial Recognition
######### Explore using 3rd party libraries, specifically OpenCV, to experiment with your own creative projects
######### October 2018
######### Python 2.7
""" FUNCTIONS:
        detect_face(image, CASCADE_NAME) - Detects face using OpenCV
        prepare_training_data(data_folder_path, CASCADE_NAME) - Detects faces from training images, returning the faces and its labels
        draw_rectangle(image, box) - Draws a rectangle around given image
        write_text(image, text, xcor, ycor) - Places text over certain (x, y) coordinates on an image
        predict(test_img, face_recognizer, subjects, CASCADE_NAME) - Predicts the person in image and labels it
"""

import cv2
import os # Read training data directories & paths
import numpy as np # Convert python lists to numpy arrays as needed by OpenCV face recognizers



# Detects face using OpenCV
def detect_face(img, CASCADE_NAME):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # LBP cascade - fast
    # Haar classifier - slow but more accurate
    face_cascade = cv2.CascadeClassifier(CASCADE_NAME)

    # Multiscale can detect multiple different sized faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

    # If no faces are detected:
    ### return original image
    if len(faces) == 0:
        return None, None

    # Only returns image of first face found
    (x, y, w, h) = faces[0]
    return gray[y:y+w, x:x+h], faces[0]



# Reads training images & detects face from each image
# Returns 2 equally sized lists: faces and face labels
def prepare_training_data(data_folder_path, CASCADE_NAME):
    # Returns all directories (1 per subject) in listed under training-data folder
    dirs = os.listdir(data_folder_path)

    faces = []
    labels = []

    # For each folder (eg: s1)
    for dir_name in dirs:
        # Only look at those starting with "s" in beginning
        if not dir_name.startswith("s"):
            continue;

        label = int(dir_name.replace("s", ""))

        # The directory path for current subject's images
        # eg: "training-data/s1"
        subject_dir_path = data_folder_path + "/" + dir_name

        # Extracts all image names inside given subject folder
        subject_images_names = os.listdir(subject_dir_path)

        # For every image:
        ### Detect & add face to list of faces
        for image_name in subject_images_names:

            # Ignore files like .DS_Store
            if image_name.startswith("."):
                continue;

            # eg: training-data/s1/1.jpg
            image_path = subject_dir_path + "/" + image_name

            image = cv2.imread(image_path)

            # Displays the current image being prepared.
            cv2.imshow("Training on image...", cv2.resize(image, (400, 500)))
            cv2.waitKey(100)

            # Detect a face
            face, rect = detect_face(image, CASCADE_NAME)

            # If there is a face
            if face is not None:
                # Add face and label to faces & labels list
                faces.append(face)
                labels.append(label)

    cv2.destroyAllWindows()
    cv2.waitKey(1)
    cv2.destroyAllWindows()

    return faces, labels



# Draws a box around image
def draw_rectangle(img, rect):
    (x, y, w, h) = rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)



# Puts text on image
def write_text(img, text, x, y):
    cv2.putText(img, text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)



# Predicts the person in image and labels it
def predict(test_img, face_recognizer, subjects, CASCADE_NAME):
    img = test_img.copy()
    # Detect face from image
    face, rect = detect_face(img, CASCADE_NAME)

    # Predict face using our face recognizer
    label, confidence = face_recognizer.predict(face)
    # Find name of label returned by the face recognizer function
    label_text = subjects[label]

    draw_rectangle(img, rect)
    write_text(img, label_text, rect[0], rect[1]-5)

    return img, label_text
    
################# www.github.com/seyhanvankhan/celebrity-recog #################
