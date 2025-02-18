import threading
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, filedialog, messagebox
import customtkinter as ctk
from yt_dlp import YoutubeDL

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / path

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window.winfo_width()) // 2
    y = (screen_height - window.winfo_height()) // 2
    window.geometry(f"+{x}+{y}")

def select_directory():
    selected_directory = filedialog.askdirectory(title="Select Output Directory")
    if selected_directory:
        entry_2.configure(state="normal")
        entry_2.delete(0, "end")
        entry_2.insert(0, selected_directory)
        entry_2.configure(state="readonly")

def download_video():
    url = entry_1.get()
    output_path = entry_2.get()
    quality = quality_dropdown.get()
    filetype = filetype_dropdown.get()

    if not url or not output_path or quality == "QUALITY" or filetype == "FILETYPE":
        messagebox.showerror("Input Error", "Please provide valid inputs.")
        return

    ydl_opts = {
        'format': f'bestvideo[height<={quality[:-1]}]+bestaudio/best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'ffmpeg_location': str(OUTPUT_PATH / "bin"),  # Specify location of ffmpeg executable
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': filetype.lower()
        }]
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Download Error", f"An error occurred: {e}")

def threaded_download_video():
    threading.Thread(target=download_video).start()

# Create main window
window = Tk()
window.title("𝗩𝗜𝗗𝗖𝗔𝗣 𝗛𝗗 𝘃𝟭.𝟬𝟬𝟭")
window.geometry("450x585")
window.configure(bg="#FFFFFF")

canvas = Canvas(window, bg="#FFFFFF", height=585, width=450, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

# Images and buttons for the UI
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(225.0, 303.0, image=image_image_1)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=select_directory, relief="flat")
button_1.place(x=386.0, y=295.0, width=44.0, height=48.0)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
canvas.create_image(70.0, 567.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
canvas.create_image(225.0, 90.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
canvas.create_image(225.0, 90.0, image=image_image_4)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=threaded_download_video, relief="flat")
button_2.place(x=145.0, y=501.0, width=159.0, height=61.0)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
canvas.create_image(393.0, 564.0, image=image_image_5)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
canvas.create_image(227.5, 257.0, image=entry_image_1)
entry_1 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
entry_1.place(x=25.0, y=232.0, width=405.0, height=48.0)

entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
canvas.create_image(227.5, 363.0, image=entry_image_2)
entry_2 = Entry(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0, state="readonly")
entry_2.place(x=25.0, y=338.0, width=405.0, height=48.0)

# Dropdown menus using CustomTkinter
ctk.set_appearance_mode("dark")
quality_dropdown = ctk.CTkOptionMenu(
    window,
    values=["QUALITY", "480p", "720p", "1080p"],
    width=120,
    height=30,
    fg_color="gray",
    button_color="dark gray",
    button_hover_color="light gray"
)
quality_dropdown.place(x=100, y=455)

filetype_dropdown = ctk.CTkOptionMenu(
    window,
    values=["FILETYPE", "MP4", "MOV", "AVI", "WMV"],
    width=120,
    height=30,
    fg_color="gray",
    button_color="dark gray",
    button_hover_color="light gray"
)
filetype_dropdown.place(x=230, y=455)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
canvas.create_image(85.0, 326.0, image=image_image_6)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
canvas.create_image(81.0, 220.0, image=image_image_7)

image_image_8 = PhotoImage(file=relative_to_assets("image_8.png"))
canvas.create_image(224.0, 432.0, image=image_image_8)

image_image_9 = PhotoImage(file=relative_to_assets("image_9.png"))
canvas.create_image(224.0, 403.5, image=image_image_9)

image_image_10 = PhotoImage(file=relative_to_assets("image_10.png"))
image_10 = canvas.create_image(225.0, 81.0, image=image_image_10)

image_image_11 = PhotoImage(file=relative_to_assets("image_11.png"))
canvas.create_image(22.0, 563.0, image=image_image_11)

image_image_12 = PhotoImage(file=relative_to_assets("image_12.png"))
image_12 = canvas.create_image(225.0, 145.0, image=image_image_12)

canvas.tag_raise(image_10)
canvas.tag_raise(image_12)

center_window(window)
window.resizable(False, False)
window.mainloop()
