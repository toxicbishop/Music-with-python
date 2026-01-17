import customtkinter as ctk
import pygame
from tkinter import filedialog
import os

class MusicPlayer(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Music Player - GUI Version 1")
        self.geometry("450x300")
        
        # Initialize pygame mixer
        pygame.mixer.init()

        self.current_song = None
        self.is_paused = False

        # Appearance
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # UI Elements
        self.label_title = ctk.CTkLabel(self, text="Music Player v1", font=("Roboto", 24))
        self.label_title.pack(pady=20)

        self.label_song = ctk.CTkLabel(self, text="No song selected", font=("Roboto", 14))
        self.label_song.pack(pady=10)

        self.btn_select = ctk.CTkButton(self, text="Select Song", command=self.select_song)
        self.btn_select.pack(pady=5)

        self.frame_controls = ctk.CTkFrame(self)
        self.frame_controls.pack(pady=20)

        self.btn_play_pause = ctk.CTkButton(self.frame_controls, text="Play", width=100, command=self.play_pause_song)
        self.btn_play_pause.grid(row=0, column=0, padx=10)

        self.btn_stop = ctk.CTkButton(self.frame_controls, text="Stop", width=100, command=self.stop_song)
        self.btn_stop.grid(row=0, column=1, padx=10)

    def select_song(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.current_song = file_path
            self.label_song.configure(text=os.path.basename(file_path))
            self.stop_song()
            self.play_song()

    def play_song(self):
        if self.current_song:
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()
            self.btn_play_pause.configure(text="Pause")
            self.is_paused = False

    def play_pause_song(self):
        if not self.current_song:
            self.select_song()
            return

        if not pygame.mixer.music.get_busy() and not self.is_paused:
             self.play_song()
        elif self.is_paused:
            pygame.mixer.music.unpause()
            self.btn_play_pause.configure(text="Pause")
            self.is_paused = False
        else:
            pygame.mixer.music.pause()
            self.btn_play_pause.configure(text="Resume")
            self.is_paused = True

    def stop_song(self):
        pygame.mixer.music.stop()
        self.btn_play_pause.configure(text="Play")
        self.is_paused = False

if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()
