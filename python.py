import tkinter as tk
from tkinter import messagebox
import lyricsgenius

# Initialize the Genius API client
GENIUS_API_TOKEN = 'your_genius_api_token_here'
genius = lyricsgenius.Genius(GENIUS_API_TOKEN)

# Function to fetch lyrics
def fetch_lyrics():
    artist = entry_artist.get()
    song = entry_song.get()

    if not artist or not song:
        messagebox.showwarning("Input Error", "Both fields are required!")
        return

    try:
        song_lyrics = genius.search_song(song, artist)
        if song_lyrics:
            lyrics_text.config(state=tk.NORMAL)
            lyrics_text.delete(1.0, tk.END)
            lyrics_text.insert(tk.END, song_lyrics.lyrics)
            lyrics_text.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", "Lyrics not found!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Lyrics Finder")

# Create and place the labels and entry widgets
tk.Label(root, text="Artist").grid(row=0, column=0, padx=10, pady=10)
entry_artist = tk.Entry(root)
entry_artist.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Song").grid(row=1, column=0, padx=10, pady=10)
entry_song = tk.Entry(root)
entry_song.grid(row=1, column=1, padx=10, pady=10)

# Create and place the fetch lyrics button
fetch_button = tk.Button(root, text="Fetch Lyrics", command=fetch_lyrics)
fetch_button.grid(row=2, columnspan=2, pady=10)

# Create and place the text widget to display lyrics
lyrics_text = tk.Text(root, wrap=tk.WORD, state=tk.DISABLED, height=15, width=50)
lyrics_text.grid(row=3, columnspan=2, padx=10, pady=10)

# Run the main event loop
root.mainloop()
