import vlc
import tkinter as tk
from tkinter import filedialog

class VLCPlayer:
    def __init__(self, root):
        self.root = root
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # Set up the window
        root.title("Media player")
        root.geometry("800x600")

        # Create a video frame
        self.video_frame = tk.Frame(root, width=600, height=400, bg="black")
        self.video_frame.pack(pady=20)

        # Get the handle for the video frame to embed the video in it
        self.video_window = self.video_frame.winfo_id()

        # Create buttons
        self.play_button = tk.Button(root, text="Play", command=self.play_media)
        self.play_button.pack(side=tk.TOP, padx=10)

        self.pause_button = tk.Button(root, text="Pause", command=self.pause_media)
        self.pause_button.pack(side=tk.TOP, padx=10)

        self.stop_button = tk.Button(root, text="Stop", command=self.stop_media)
        self.stop_button.pack(side=tk.TOP, padx=10)

        self.open_button = tk.Button(root, text="Open File", command=self.open_file)
        self.open_button.pack(side=tk.TOP, padx=10)

    def open_file(self):
        # Open a file dialog to select video or audio files
        media_path = filedialog.askopenfilename(filetypes=[("Media Files", "*.mp3 *.mp4 *.avi *.mkv *.wav")])
        if media_path:
            self.media = self.instance.media_new(media_path)
            self.player.set_media(self.media)
            # Attach the player to the video frame (canvas)
            self.player.set_hwnd(self.video_window)

    def play_media(self):
        # Play the media
        self.player.play()

    def pause_media(self):
        # Pause the media
        self.player.pause()

    def stop_media(self):
        # Stop the media
        self.player.stop()

# Create the main application window
root = tk.Tk()
app = VLCPlayer(root)
root.resizable(0,0)
root.mainloop()
