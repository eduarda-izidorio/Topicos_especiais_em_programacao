import os
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from groq import Groq
import pygame

# Initialize the Groq client
client = Groq()

# Initialize Pygame mixer
pygame.mixer.init()

def transcribe_audio():
    filename = file_path.get()
    if not filename:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo de áudio.")
        return

    try:
        with open(filename, "rb") as file:
            transcription = client.audio.transcriptions.create(
                file=(filename, file.read()),
                model="whisper-large-v3-turbo",
                prompt="Áudio",
                response_format="verbose_json",
                language="pt",
                temperature=0.0
            )
            transcription_text.delete(1.0, tk.END)
            transcription_text.insert(tk.END, transcription.text)
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")

def select_file():
    filename = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    file_path.set(filename)

def play_audio():
    filename = file_path.get()
    if not filename:
        messagebox.showerror("Erro", "Por favor, selecione um arquivo de áudio.")
        return
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao reproduzir: {str(e)}")

def pause_audio():
    pygame.mixer.music.pause()

def resume_audio():
    pygame.mixer.music.unpause()

def restart_audio():
    pygame.mixer.music.stop()
    play_audio()

def clear_transcription():
    transcription_text.delete(1.0, tk.END)

# Create main window
root = tk.Tk()
root.title("Transcrição de Áudio")
root.geometry("500x600")
root.configure(bg="#f7f9fc")

file_path = tk.StringVar()

# Interface components
header_frame = tk.Frame(root, bg="#4A90E2", pady=10)
header_frame.pack(fill=tk.X)
tk.Label(header_frame, text="Transcrição de Áudio", font=("Arial", 16), bg="#4A90E2", fg="white").pack()

tk.Label(root, text="Selecione um arquivo:", bg="#f7f9fc", font=("Arial", 12)).pack(pady=10)
tk.Entry(root, textvariable=file_path, width=40, font=("Arial", 12)).pack(pady=5)

# Buttons
controls_frame = tk.Frame(root, bg="#f7f9fc")
controls_frame.pack(pady=10)

tk.Button(controls_frame, text="Selecionar Arquivo", command=select_file, bg="#4A90E2", fg="white", font=("Arial", 10), relief=tk.FLAT).pack(side=tk.LEFT, padx=5)
tk.Button(controls_frame, text="Transcrever", command=transcribe_audio, bg="#5BBF8A", fg="white", font=("Arial", 10), relief=tk.FLAT).pack(side=tk.LEFT, padx=5)

# Audio controls
audio_controls = tk.Frame(root, bg="#f7f9fc")
audio_controls.pack(pady=10)

tk.Button(audio_controls, text="▶ Reproduzir", command=play_audio, bg="#F39C12", fg="white", font=("Arial", 10), relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
tk.Button(audio_controls, text="⏸ Pausar", command=pause_audio, bg="#E67E22", fg="white", font=("Arial", 10), relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
tk.Button(audio_controls, text="⏵ Retomar", command=resume_audio, bg="#27AE60", fg="white", font=("Arial", 10), relief=tk.FLAT).pack(side=tk.LEFT, padx=2)
tk.Button(audio_controls, text="⏹ Reiniciar", command=restart_audio, bg="#2980B9", fg="white", font=("Arial", 10), relief=tk.FLAT).pack(side=tk.LEFT, padx=2)

# Clear button
tk.Button(root, text="🧹 Limpar Transcrição", command=clear_transcription, bg="#E74C3C", fg="white", font=("Arial", 10), relief=tk.FLAT).pack(pady=10)

# Transcription area
transcription_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15, width=60, font=("Arial", 10), bg="#ffffff", fg="#333333")
transcription_text.pack(pady=10, padx=10)

root.mainloop()