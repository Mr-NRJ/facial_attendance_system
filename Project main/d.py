import serial
ser = serial.Serial('/dev/ttyUSB0')
ser.write(b'hello')
import face_recognition
import cv2
import numpy as np
import time
from espeak import espeak
previous ="unkno"
# This is a demo of running face recognition on live video from your webcam. It's a little more complicated than the
# other example, but it includes some basic performance tweaks to make things run a lot faster:
#   1. Process each video frame at 1/4 resolution (though still display it at full resolution)
#   2. Only detect faces in every other frame of video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)


# Load a sample picture and learn how to recognize it.
ash_image = face_recognition.load_image_file("ash.jpg")
ash_face_encoding = face_recognition.face_encodings(ash_image)[0]

# Load a second sample picture and learn how to recognize it.
alhil_image = face_recognition.load_image_file("Alhil.jpg")
alhil_face_encoding = face_recognition.face_encodings(alhil_image)[0]

# Load a sample picture and learn how to recognize it.
atul_image = face_recognition.load_image_file("Atul.jpg")
atul_face_encoding = face_recognition.face_encodings(atul_image)[0]

# Load a second sample picture and learn how to recognize it.
gaurav_image = face_recognition.load_image_file("Gaurav.jpg")
gaurav_face_encoding = face_recognition.face_encodings(gaurav_image)[0]


# Load a sample picture and learn how to recognize it.
mukul_image = face_recognition.load_image_file("Mukul.jpg")
mukul_face_encoding = face_recognition.face_encodings(mukul_image)[0]

# Load a second sample picture and learn how to recognize it.
savita_image = face_recognition.load_image_file("savita.jpg")
savita_face_encoding = face_recognition.face_encodings(savita_image)[0]

# Load a sample picture and learn how to recognize it.
rahul_image = face_recognition.load_image_file("Rahul chopra.jpg")
rahul_face_encoding = face_recognition.face_encodings(rahul_image)[0]

# Load a second sample picture and learn how to recognize it.
shipra_image = face_recognition.load_image_file("shipra.jpg")
shipra_face_encoding = face_recognition.face_encodings(shipra_image)[0]

vinay_image = face_recognition.load_image_file("vinay.jpg")
vinay_face_encoding = face_recognition.face_encodings(vinay_image)[0]



# Load a sample picture and learn how to recognize it.
vinita_image = face_recognition.load_image_file("vinita.jpg")
vinita_face_encoding = face_recognition.face_encodings(vinita_image)[0]

# Load a second sample picture and learn how to recognize it.
parul_image = face_recognition.load_image_file("parul.jpg")
parul_face_encoding = face_recognition.face_encodings(parul_image)[0]

# Load a sample picture and learn how to recognize it.
tanyaaneja_image = face_recognition.load_image_file("tanyaaneja.jpg")
tanyaaneja_face_encoding = face_recognition.face_encodings(tanyaaneja_image)[0]

# Load a second sample picture and learn how to recognize it.
deba_image = face_recognition.load_image_file("deba.jpg")
deba_face_encoding = face_recognition.face_encodings(deba_image)[0]

tanya_image = face_recognition.load_image_file("tanya.jpg")
tanya_face_encoding = face_recognition.face_encodings(tanya_image)[0]


reshu_image = face_recognition.load_image_file("reshu.jpg")
reshu_face_encoding = face_recognition.face_encodings(reshu_image)[0]

astha_image = face_recognition.load_image_file("astha.jpg")
astha_face_encoding = face_recognition.face_encodings(astha_image)[0]

akhilesh_image = face_recognition.load_image_file("akhilesha.jpg")
akhilesh_face_encoding = face_recognition.face_encodings(akhilesh_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    ash_face_encoding,
    alhil_face_encoding,
    atul_face_encoding,
    gaurav_face_encoding,
    mukul_face_encoding,
    savita_face_encoding,
    rahul_face_encoding,
    shipra_face_encoding,
    vinay_face_encoding,
    vinita_face_encoding,
    parul_face_encoding,
    tanyaaneja_face_encoding,
    deba_face_encoding,
    tanya_face_encoding,
    reshu_face_encoding,
    astha_face_encoding,
    akhilesh_face_encoding,
    
    
]
known_face_names = [
    "Ashwini kumar",
    "Akhil ",
    "Atul",
    "gaurav Lo",
    "mukul",
    "shavita",
    "rahul",
    "shipra",
    "vinay",
    "vinita",
    "parul",
    "tanya ",
    "deba",
    "tanya",
    "reshu",
    "astha",
    "akhilesh"
]


# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.33, fy=0.33)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            

            # # If a match was found in known_face_encodings, just use the first one.
            # if True in matches:
            #     first_match_index = matches.index(True)
            #     name = known_face_names[first_match_index]

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
                if previous != name:
                    previous=name
                    print(name)
                    #espeak.synth("Hey I Can Identify your face")
                    #espeak.synth("Your name is")
                    #espeak.synth(name)
                    espeak.set_voice("En")
                    espeak.set_voice("whisper")
                    espeak.synth("Hey hello ")
                    espeak.synth(name)
                    espeak.synth("Your attendance is marked")
                    espeak.synth("have a nice day")
                    ser.write(name.encode())
                    

                else:
                    print("old same")
               

            face_names.append(name)
            

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
