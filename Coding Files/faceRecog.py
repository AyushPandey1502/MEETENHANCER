import face_recognition
import os
import numpy as np
import PhotoCapturing as pc

def encode_faces(image_path):
    # Load the image
    image = face_recognition.load_image_file(image_path)

    # Find all face locations in the image
    face_locations = face_recognition.face_locations(image)

    # If no faces are found, return an empty list
    if not face_locations:
        return []

    # Encode the faces found in the image
    face_encodings = face_recognition.face_encodings(image, face_locations)

    return face_encodings

def save_encodings_to_file(face_encodings, output_file):
    with open(output_file, 'w') as file:
        for face_encoding in face_encodings:
            # Convert the face encoding to a comma-separated string
            encoding_str = ','.join(map(str, face_encoding))
            file.write(encoding_str + '\n')

def main():
    root = pc.tk.Tk()
    pc.PhotoDialog(root)
    root.mainloop()

    # Specify the path to the Images folder
    images_folder = "Images"

    # Specify the name of the image file
    image_filename = "saved_photo.png"  # Replace with the actual image filename

    # Construct the full path to the image file
    image_path = os.path.join(images_folder, image_filename)

    # Check if the image file exists
    if os.path.exists(image_path):
        # Perform face encoding
        face_encodings = encode_faces(image_path)

        if face_encodings:
            # Save face encodings to a file
            output_file = "encoded_faces.txt"
            save_encodings_to_file(face_encodings, output_file)
            print(f"Face encodings saved to '{output_file}'.")
        else:
            print("No faces found in the image.")
    else:
        print(f"The image file '{image_path}' does not exist.")

if __name__ == "__main__":
    main()
