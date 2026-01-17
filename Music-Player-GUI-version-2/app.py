import customtkinter as ctk
import pygame
import os
from tkinter import filedialog
from PIL import Image

class MusicPlayerV2(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Music Player - GUI Version 2")
        self.geometry("900x500")
        
        # Initialize pygame mixer
        pygame.mixer.init()

        self.music_dir = "../music_files"
        if not os.path.exists(self.music_dir):
            os.makedirs(self.music_dir)

        self.playlist = []
        self.current_index = -1
        self.is_paused = False

        # Appearance
        ctk.set_appearance_mode("Dark")
        ctk.set_default_color_theme("blue")

        # Configure Grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar (Playlist) ---
        self.sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(2, weight=1)

        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="My Playlist", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.btn_refresh = ctk.CTkButton(self.sidebar_frame, text="Refresh Library", command=self.load_music)
        self.btn_refresh.grid(row=1, column=0, padx=20, pady=10)

        self.scrollable_playlist = ctk.CTkScrollableFrame(self.sidebar_frame, label_text="Songs")
        self.scrollable_playlist.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        self.song_buttons = []

        # --- Main Content ---
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        self.main_frame.grid_rowconfigure(1, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Now Playing Label
        self.label_now_playing = ctk.CTkLabel(self.main_frame, text="Select a song to play", font=ctk.CTkFont(size=22, weight="bold"))
        self.label_now_playing.grid(row=0, column=0, pady=(40, 0))

        # Visualizer Placeholder / Image
        self.visualizer_frame = ctk.CTkFrame(self.main_frame, height=200, fg_color="#2b2b2b")
        self.visualizer_frame.grid(row=1, column=0, padx=40, pady=40, sticky="nsew")
        self.vis_label = ctk.CTkLabel(self.visualizer_frame, text="🎵", font=("Roboto", 100))
        self.vis_label.place(relx=0.5, rely=0.5, anchor="center")

        # Control Panel
        self.controls_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.controls_frame.grid(row=2, column=0, pady=20)

        self.btn_prev = ctk.CTkButton(self.controls_frame, text="⏮", width=40, command=self.prev_song)
        self.btn_prev.grid(row=0, column=0, padx=10)

        self.btn_play_pause = ctk.CTkButton(self.controls_frame, text="▶ Play", width=120, height=40, 
                                            font=ctk.CTkFont(size=16, weight="bold"), command=self.toggle_play)
        self.btn_play_pause.grid(row=0, column=1, padx=10)

        self.btn_next = ctk.CTkButton(self.controls_frame, text="⏭", width=40, command=self.next_song)
        self.btn_next.grid(row=0, column=2, padx=10)

        # Volume Slider
        self.volume_frame = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.volume_frame.grid(row=3, column=0, pady=10)
        
        self.label_vol = ctk.CTkLabel(self.volume_frame, text="Volume")
        self.label_vol.grid(row=0, column=0, padx=10)
        
        self.slider_volume = ctk.CTkSlider(self.volume_frame, from_=0, to=1, command=self.set_volume)
        self.slider_volume.set(0.7)
        self.slider_volume.grid(row=0, column=1, padx=10)
        pygame.mixer.music.set_volume(0.7)

        # Load initial music
        self.load_music()

    def load_music(self):
        # Clear existing buttons
        for btn in self.song_buttons:
            btn.destroy()
        self.song_buttons = []
        self.playlist = []

        # Find songs
        if os.path.exists(self.music_dir):
            files = [f for f in os.listdir(self.music_dir) if f.endswith(('.mp3', '.wav'))]
            for i, file in enumerate(files):
                full_path = os.path.join(self.music_dir, file)
                self.playlist.append(full_path)
                
                # Create button for each song
                btn = ctk.CTkButton(self.scrollable_playlist, text=file, anchor="w", 
                                   fg_color="transparent", text_color="white", hover_color="#3b3b3b",
                                   command=lambda path=full_path, idx=i: self.select_from_playlist(path, idx))
                btn.pack(fill="x", pady=2)
                self.song_buttons.append(btn)

    def select_from_playlist(self, path, index):
        self.current_index = index
        self.play_specific(path)

    def play_specific(self, path):
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        self.label_now_playing.configure(text=os.path.basename(path))
        self.btn_play_pause.configure(text="⏸ Pause")
        self.is_paused = False
        
        # Highlight active song in playlist
        for i, btn in enumerate(self.song_buttons):
            if i == self.current_index:
                btn.configure(fg_color="#1f538d")
            else:
                btn.configure(fg_color="transparent")

    def toggle_play(self):
        if self.current_index == -1 and self.playlist:
            self.select_from_playlist(self.playlist[0], 0)
            return

        if self.is_paused:
            pygame.mixer.music.unpause()
            self.btn_play_pause.configure(text="⏸ Pause")
            self.is_paused = False
        else:
            pygame.mixer.music.pause()
            self.btn_play_pause.configure(text="▶ Play")
            self.is_paused = True

    def next_song(self):
        if not self.playlist: return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play_specific(self.playlist[self.current_index])

    def prev_song(self):
        if not self.playlist: return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play_specific(self.playlist[self.current_index])

    def set_volume(self, value):
        pygame.mixer.music.set_volume(value)

if __name__ == "__main__":
    app = MusicPlayerV2()
    app.mainloop()
