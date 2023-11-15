import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import os

class PhotoDialog:
    def __init__(self, root):
        self.root = root
        self.root.title("Photo Dialog")

        self.label = tk.Label(root, text="Choose a photo or capture one:")
        self.label.pack(pady=10)

        self.choose_button = tk.Button(root, text="Choose Photo", command=self.choose_photo)
        self.choose_button.pack(pady=5)

        self.capture_button = tk.Button(root, text="Capture from Webcam", command=self.capture_photo)
        self.capture_button.pack(pady=5)

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

        self.save_button = tk.Button(root, text="Save Photo", command=self.save_photo)
        self.save_button.pack(pady=10)

        self.photo_path = None  # To store the path of the current photo

    def choose_photo(self):
        file_path = filedialog.askopenfilename(title="Choose a Photo", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.display_photo(file_path)

    def capture_photo(self):
        # self.label.config(text="Face towards the webcam")
        cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera
        ret, frame = cap.read()

        if ret:
            # Convert the captured frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Use the pre-trained face detection model from cv2
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

            if len(faces) > 0:
                # Display message if a frontal face is detected
                self.label.config(text="Image captured successfully with a frontal face!")
                save_path = "captured_photo.png"
                cv2.imwrite(save_path, gray_frame)
                cap.release()
                self.display_photo(save_path)
                # os.remove(save_path)
            else:
                # Display message if no frontal face is detected
                self.label.config(text="No frontal face detected. Please capture the image again.")

    def display_photo(self, file_path):
        img = Image.open(file_path)
        img.thumbnail((400, 400))  # Resize the image to fit in the canvas
        self.photo_path = file_path
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def save_photo(self):
        if self.photo:
            save_directory = "Images"
            save_path = os.path.join(save_directory, "saved_photo.png")  # Change the filename as needed

            # Check if the directory exists, create it if not
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)

            img = Image.open("captured_photo.png")  # Open the image using Image from PIL
            img.save(save_path, format="png")
            os.remove("captured_photo.png")

            # Close the Tkinter window after saving
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoDialog(root)
    root.mainloop()
