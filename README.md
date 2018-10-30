# Celebrity Recognition


### Problem:
You can't tell from looking at a celebrity's photo whether its person A or person B

### Usage:
1. User places his mystery person image in your-picture directory.
2. User inputs the names of every possible celebrity it could be

### Solution:
Using facial recognition & Google Images, it tells you who it is


## Getting Started
These instructions will get you a copy of the project up and running on your local machine for usage.

### Installing
- **[Python 2.7](https://www.python.org/download/releases/2.7/)**
- [os](https://docs.python.org/3/library/os.html)
- [cv2](https://opencv.org/)
- [numpy](https://www.scipy.org/install.html)
- [google_images_download](https://github.com/hardikvasa/google-images-download)
  * `$ pip install google_images_download`


### Running the program
* Create 2 folders
  - your-picture
  - training-data
* Download and place your mystery face image into your-picture folder.
* Go to the CONSTANTS section of main.py and rename PIC_FILE_NAME to your picture's.
* Execute `main.py` in **Python 2.7**.


### Constants
- `string PIC_FILE_NAME` = Your picture's file name
- `int NUM_IMAGES` = Number of images downloaded per person - 
- `string CASCADE_NAME` = Face cascade used to detect a human face
- `int FACE_RECOGNISER_FUNC` = Choice of Face Recogniser Function
  * 1 = Local Binary Patterns Histogram (LBPH)
  * 2 = EigenFace Recognizer
  * 3 = FisherFace Recognizer


## Author

* **Seyhan Van Khan**

## Acknowledgments

* [Google Images Download](https://github.com/hardikvasa/google-images-download)
