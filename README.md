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
- [cv2](https://opencv.org/)
- [numpy](https://www.scipy.org/install.html)
- [google_images_download](https://github.com/hardikvasa/google-images-download)
  * ```$ pip install google_images_download```


### Running the program
* Create a folder
  - `training-data`
* Place your mystery face image into `your-picture` folder.
* Execute `python main.py PIC_FILE_NAME` (**Python 2.7**), where PIC_FILE_NAME is your mystery image's filename
* eg: `python main.py person1.jpg`

### Constants
- `string PIC_FILE_NAME` = Your picture's file name
- `int NUM_IMAGES` = Number of images downloaded per person
- `string CASCADE_NAME` = Face cascade used to detect a human face
- `int FACE_RECOGNISER_FUNC` = Choice of Face Recogniser Function:
  * 1 = Local Binary Patterns Histogram (LBPH)
  * 2 = EigenFace Recognizer
  * 3 = FisherFace Recognizer


## Acknowledgments

* [Google Images Download](https://github.com/hardikvasa/google-images-download)
