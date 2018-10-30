######### Seyhan Van Khan
######### Celebrity Facial Recognition
######### Tells you who a given picture is of, given several possible famous people's name, with facial recognition & google images
######### October 2018
######### Python 2.7
""" FUNCTIONS:
        InputNames() - Asks user for celebrities names'
        GetImages(NUM_IMAGES) - Searches Google Images for names and downloads them
"""

# Library used to access google from python:
# $ pip install google_images_download
# https://github.com/hardikvasa/google-images-download#usage-from-another-python-file
from google_images_download import google_images_download



# Introduces user to usage of code
# Asks for names of people in order to download training data images of them
def InputNames():
    print("""\tTHE CELEBRITY IDENTIFIER
    Please enter the names of all the celebrities the picture could be.
    When complete, just hit enter.
    """)

    people = [""]
    while True:
        person_name = raw_input("Name: ")

        # If user just entered nothing
        if person_name == "":
            if len(people) < 3:
                print("You must enter at least 2 names.")
                continue

            # If length is sufficient, return list of names
            return people

        people.append(person_name)



# Searches Google Images for names given
# Each person's pics are placed in 1 subfolder of training-data
def GetImages(NUM_IMAGES):
    people = InputNames()

    # For each name user gave
    for person in people[1:]:
        response = google_images_download.googleimagesdownload()
        # Create subfolder name for each person
        subject_folder = "s" + str(people.index(person))
        # Search Google Images for name and download a certain number of images
        # Must be jpg
        absolute_image_paths = response.download({"keywords":person,
                                            "limit":NUM_IMAGES,
                                            "format":"jpg",
                                            "type":"face",
                                            "output_directory":"training-data",
                                            "image_directory":subject_folder
                                            })

    return people

################# www.github.com/seyhanvankhan/celebrity-recog #################
