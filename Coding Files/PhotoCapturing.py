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
        file_path = filedialog.askopenfilename(title="Choose a Photo",
                                               filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        if file_path:
            # Read the image and convert it to grayscale
            img = cv2.imread(file_path)
            gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # Use the pre-trained face detection model from cv2
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=8)

            if len(faces) > 0:
                self.label.config(text="Image loaded successfully with a frontal face!")
                self.display_photo(file_path)
            else:
                self.label.config(text="No frontal face detected in the loaded image. Please choose another image.")

    def capture_photo(self):
        cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera
        ret, frame = cap.read()

        if ret:
            # Convert the captured frame to grayscale
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Use the pre-trained face detection model from cv2
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

            if len(faces) > 0:
                self.label.config(text="Image captured successfully with a frontal face!")
                save_path = "captured_photo.png"
                cv2.imwrite(save_path, gray_frame)
                cap.release()
                self.display_photo(save_path)
            else:
                self.label.config(text="No frontal face detected. Please capture the image again.")

    def display_photo(self, file_path):
        img = Image.open(file_path)
        img.thumbnail((400, 400))  # Resize the image to fit in the canvas
        self.photo_path = file_path
        self.photo = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def save_photo(self):
        if self.photo_path:
            # Check if the photo has a frontal face before saving
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            img = cv2.imread(self.photo_path)
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)

            if len(faces) > 0:
                save_directory = "Images"
                save_path = os.path.join(save_directory, "saved_photo.png")

                if not os.path.exists(save_directory):
                    os.makedirs(save_directory)

                # Open the image using Image from PIL and save it
                img_pil = Image.open(self.photo_path)
                img_pil.save(save_path, format="png")
                os.remove("captured_photo.png")
                # Close the Tkinter window after saving
                self.root.destroy()
            else:
                self.label.config(text="No frontal face detected. Cannot save the photo.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PhotoDialog(root)
    root.mainloop()
