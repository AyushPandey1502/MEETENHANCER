import cv2
import mediapipe as mp
import numpy as np
import requests
from shapely.geometry import box
from shapely.geometry import Polygon

# Initialize the MediaPipe Face Detection and Pose Estimation models
mp_face_detection = mp.solutions.face_detection.FaceDetection(min_detection_confidence=0.5)
mp_pose = mp.solutions.pose.Pose(min_detection_confidence=0.5)

# Load the encoded faces from the file
encoded_faces = []
with open("encoded_faces.txt") as f:
    for line in f:
        encoded_face = line.strip()
        encoded_faces.append(encoded_face)

# Start the Google Meet video stream capture
cap = cv2.VideoCapture(0)

# Define the function to check if the person's face and shoulder are in the camera view
def is_person_in_camera_view(face_landmarks, pose_landmarks):
    # Get the face bounding box
    face_bbox = calculate_face_bounding_box(face_landmarks)

    # Check if the face bounding box intersects with the shoulder bounding box
    shoulder_bbox = calculate_shoulder_bounding_box(pose_landmarks)
    if face_bbox.intersects(shoulder_bbox):
        return True
    else:
        return False

# Define the function to calculate the face bounding box
def calculate_face_bounding_box(face_landmarks):
    points = [(lm.x, lm.y) for lm in face_landmarks]
    face_polygon = Polygon(points)
    return face_polygon.bounds

# Define the function to calculate the shoulder bounding box
def calculate_shoulder_bounding_box(pose_landmarks):
    shoulder_landmarks = [pose_landmarks.landmark[mp_pose.PoseLandmark.LEFT_SHOULDER],
                           pose_landmarks.landmark[mp_pose.PoseLandmark.RIGHT_SHOULDER]]

    points = [(lm.x, lm.y) for lm in shoulder_landmarks]
    shoulder_polygon = Polygon(points)
    return shoulder_polygon.bounds

# Define the function to turn on the camera and microphone
def turn_on_camera_and_microphone():
    # Make an API call to turn on the camera and microphone
    # Implement your logic or use an external service to control camera and microphone
    print("Turning on camera and microphone")

# Define the function to turn off the camera and microphone
def turn_off_camera_and_microphone():
    # Make an API call to turn off the camera and microphone
    # Implement your logic or use an external service to control camera and microphone
    print("Turning off camera and microphone")

while True:
    # Capture a frame from the video stream
    ret, frame = cap.read()

    # Convert the frame to RGB format
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect faces in the frame
    face_results = mp_face_detection.process(rgb_frame)

    # Detect poses in the frame
    pose_results = mp_pose.process(rgb_frame)

    # Check if there are any faces detected
    if face_results.detections:
        for face in face_results.detections:
            # Get the face landmarks
            face_landmarks = face.location_data.relative_bounding_box

            # Encode the face
            encoded_face = str(face_landmarks)

            # Check if the encoded face matches any of the encoded faces in the file
            if encoded_face in encoded_faces:
                # Get the pose landmarks
                pose_landmarks = pose_results.pose_landmarks

                # Check if the person's face and shoulder are in the camera view
                if is_person_in_camera_view(face_landmarks, pose_landmarks):
                    print("Person's face and shoulder are in the camera view.")

                    # Turn on the camera and microphone
                    turn_on_camera_and_microphone()
                else:
                    print("Person's face and shoulder are not in the camera view.")

                    # Turn off the camera and microphone
                    turn_off_camera_and_microphone()
            else:
                print("Face not recognized.")
    else:
        print("No face detected.")

    # Display the frame
    cv2.imshow('Frame', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
