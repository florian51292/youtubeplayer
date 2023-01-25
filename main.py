import pytube
import tkinter as tk
import cv2

def play_video():
    # Get the video url from the input field
    url = url_entry.get()

    # Create the video stream
    yt = pytube.YouTube(url)
    video_stream = yt.streams.first()

    # Open the video stream and set the video window to a quarter of the screen
    cap = cv2.VideoCapture(video_stream.url)
    cv2.namedWindow("Video", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Video", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

root = tk.Tk()
root.geometry("300x50")

url_label = tk.Label(root, text="Video URL:")
url_label.pack(padx=5, pady=5)

url_entry = tk.Entry(root)
url_entry.pack(padx=5, pady=5)

play_button = tk.Button(root, text="Play", command=play_video)
play_button.pack(padx=5, pady=5)

root.mainloop()
