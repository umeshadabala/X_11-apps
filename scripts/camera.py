import tkinter as tk
import cv2
from PIL import Image, ImageTk
import os
import threading
import time

# Create a directory for the gallery
if not os.path.exists("gallery"):
    os.makedirs("gallery")

# Initialize image_thumbnails as a global list
image_thumbnails = []
video_thumbnails = []  # New list for video thumbnails

# Add a global variable to control camera feed updates
update_camera = True

def capture_image():
    ret, frame = cap.read()
    if ret:
        # Generate a unique filename with a timestamp
        timestamp = time.strftime("%Y%m%d%H%M%S")
        image_path = os.path.join("gallery", f"captured_image_{timestamp}.jpg")
        cv2.imwrite(image_path, frame)
        show_image(image_path)

def start_recording():
    global video_writer, recording_start_time, recording_stopped, update_camera
    if not video_writer:
        # Generate a unique filename with a timestamp
        timestamp = time.strftime("%Y%m%d%H%M%S")
        video_path = os.path.join("gallery", f"recorded_video_{timestamp}.mp4")
        # Use mp4v codec (or try other codecs)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        # Adjust frame rate and resolution if needed
        video_writer = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))
        recording_start_time = time.time()
        recording_stopped = False
        record_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)

        # Start a separate thread for recording and time-lapse display
        recording_thread = threading.Thread(target=record_and_display)
        recording_thread.start()

def stop_recording():
    global video_writer, recording_stopped
    if video_writer:
        video_writer.release()
        recording_stopped = True  # Set the recording_stopped flag to True
        record_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)

def record_and_display():
    global recording_stopped, update_camera
    while video_writer and not recording_stopped:
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Calculate elapsed time and add it to the frame
            elapsed_time = time.time() - recording_start_time
            timestamp = f"Time Elapsed: {int(elapsed_time)}s"
            cv2.putText(frame, timestamp, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            img = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=img)
            camera_feed.config(image=photo)
            camera_feed.image = photo

            video_writer.write(frame)
            time.sleep(0.05)  # Adjust the delay for the desired time-lapse effect
    camera_feed.after(10, update_camera_feed)  # Continue updating the camera feed

def show_image(image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image=image)
    camera_feed.config(image=photo)
    camera_feed.image = photo

def play_video(video_path):
    def close_video_player():
        video_player.destroy()
        global update_camera
        update_camera = True  # Resume updating the camera feed

    global update_camera
    update_camera = False  # Pause camera feed updates

    video_player = tk.Toplevel(root)
    video_player.title("Video Player")

    video_cap = cv2.VideoCapture(video_path)

    def update_video_frame():
        ret, frame = video_cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(image=img)
            video_label.config(image=photo)
            video_label.image = photo

            # Get the actual frame rate of the video
            frame_rate = video_cap.get(cv2.CAP_PROP_FPS)

            # Calculate the delay based on the original frame rate
            delay = int(1000 / frame_rate)

            video_player.after(delay, update_video_frame)  # Delay based on frame rate
        else:
            video_player.destroy()

    video_label = tk.Label(video_player)
    video_label.pack()

    update_video_frame()

    video_player.protocol("WM_DELETE_WINDOW", close_video_player)

def create_video_thumbnail(video_path):
    video_cap = cv2.VideoCapture(video_path)
    ret, frame = video_cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        thumbnail = Image.fromarray(frame).resize((100, 100))
        thumbnail_photo = ImageTk.PhotoImage(image=thumbnail)
        # Return both the thumbnail and filename
        return thumbnail_photo, os.path.basename(video_path)
    return None, None

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def play_video_from_thumbnail(video_path):
    play_video(video_path)

def open_gallery():
    global update_camera
    update_camera = False  # Pause camera feed updates

    gallery_window = tk.Toplevel(root)
    gallery_window.title("Gallery")

    def back_to_camera():
        gallery_window.destroy()
        global update_camera
        update_camera = True  # Resume updating the camera feed

    back_button = tk.Button(gallery_window, text="Back to Camera", command=back_to_camera)
    back_button.pack()

    gallery_dir = "gallery"
    image_files = [f for f in os.listdir(gallery_dir) if f.endswith(".jpg")]
    video_files = [f for f in os.listdir(gallery_dir) if f.endswith(".mp4")]

    # Clear the existing image_thumbnails and video_thumbnails lists
    del image_thumbnails[:]
    del video_thumbnails[:]

    for image_file in image_files:
        image_path = os.path.join(gallery_dir, image_file)
        thumbnail = Image.open(image_path).resize((100, 100))
        thumbnail_photo = ImageTk.PhotoImage(image=thumbnail)
        image_name = os.path.basename(image_file)

        def show_image_in_gallery(img_path, img_name):
            image_window = tk.Toplevel(gallery_window)
            image_window.title("Image")
            img = Image.open(img_path)
            img_photo = ImageTk.PhotoImage(img)
            img_label = tk.Label(image_window, image=img_photo)
            img_label.image = img_photo
            img_label.pack()

            img_label_name = tk.Label(image_window, text=img_name)
            img_label_name.pack()

            def delete_image():
                delete_file(img_path)
                image_window.destroy()
                gallery_window.destroy()
                open_gallery()

            delete_button = tk.Button(image_window, text="Delete", command=delete_image)
            delete_button.pack()

        thumbnail_label = tk.Label(gallery_window, image=thumbnail_photo)
        thumbnail_label.image = thumbnail_photo
        thumbnail_label.bind("<Button-1>", lambda event, img_path=image_path, img_name=image_name: show_image_in_gallery(img_path, img_name))
        thumbnail_label.pack()
        image_thumbnails.append(thumbnail_photo)  # Store the PhotoImage objects

        # Display the image filename below the thumbnail
        image_name_label = tk.Label(gallery_window, text=image_name)
        image_name_label.pack()

    for video_file in video_files:
        video_path = os.path.join(gallery_dir, video_file)

        # Create a video thumbnail and get the filename
        thumbnail_photo, video_name = create_video_thumbnail(video_path)

        if thumbnail_photo:
            # Create a button with the video thumbnail
            video_thumbnail_button = tk.Button(gallery_window, image=thumbnail_photo, command=lambda path=video_path: play_video_from_thumbnail(path))
            video_thumbnail_button.pack()
            # Store the video thumbnail PhotoImage objects
            video_thumbnails.append(thumbnail_photo)

            # Display the video filename below the thumbnail
            video_name_label = tk.Label(gallery_window, text=video_name)
            video_name_label.pack()

            def delete_video():
                delete_file(video_path)
                gallery_window.destroy()
                open_gallery()

            delete_button = tk.Button(gallery_window, text="Delete", command=delete_video)
            delete_button.pack()

# Create the main root window
root = tk.Tk()
root.title("Camera Application")

# Initialize variables
video_writer = None
recording_start_time = 0  # Initialize recording start time
recording_stopped = False  # Initialize recording_stopped flag

# Create buttons
capture_button = tk.Button(root, text="Capture", command=capture_image)
record_button = tk.Button(root, text="Record", command=start_recording)
stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
gallery_button = tk.Button(root, text="Gallery", command=open_gallery)
quit_button = tk.Button(root, text="Quit", command=root.quit)

# Grid layout for buttons
capture_button.grid(row=0, column=0, padx=10, pady=10)
record_button.grid(row=0, column=1, padx=10, pady=10)
stop_button.grid(row=0, column=2, padx=10, pady=10)
gallery_button.grid(row=0, column=3, padx=10, pady=10)
quit_button.grid(row=0, column=4, padx=10, pady=10)

# Create camera feed label
camera_feed = tk.Label(root)
camera_feed.grid(row=1, column=0, columnspan=5)

# Initialize the camera
cap = cv2.VideoCapture(0)

# Function to update the camera feed
def update_camera_feed():
    if update_camera:
        if not video_writer:
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(image=img)
                camera_feed.config(image=photo)
                camera_feed.image = photo
    root.after(10, update_camera_feed)

update_camera_feed()
root.resizable(0,0)
# Start the tkinter main loop
root.mainloop()
