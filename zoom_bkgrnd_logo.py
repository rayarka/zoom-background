from moviepy.editor import *
from moviepy.video.fx import *
import os
from tkinter.filedialog import askopenfilename, asksaveasfile 

def save():
    files = [('MP4 Video File', '*.mp4')]
    savefile = asksaveasfile(filetypes = files, defaultextension = files) 
    return savefile.name
    
#parameters
source_video_path = askopenfilename(title = "Select The Background Video File", filetypes = (("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi"), ("png", "*.png")))
video_clip = VideoFileClip(source_video_path, audio=False)

source_logo_path = askopenfilename(title = "Select The Foreground Picture File", filetypes = (("png", "*.png"), ("jpg", "*.jpg")))
logo_clip = ImageClip(source_logo_path)

#file details (needed for calculations later)
vidwidth,vidheight = moviesize = video_clip.size
fps = video_clip.fps
picwidth, picheight = logo_clip.size

# print(f'vidwidth = {vidwidth}\nvidheight = {vidheight}\npicture width = {picwidth}\npicture height = {picheight}\nnew pic width = {int(vidwidth/3)}\nnew pic height = {int((vidwidth*picheight)/(3*picwidth))}')
logo_clip = logo_clip.resize((int(vidwidth/3), int((vidwidth*picheight)/(3*picwidth))))
logo_clip = logo_clip.margin(top = 80, left = 80, opacity=0)

outputfilepath = save()

# FINAL ASSEMBLY
final = CompositeVideoClip([video_clip,logo_clip])
final.subclip(0, video_clip.duration).write_videofile(outputfilepath,fps=video_clip.fps,codec='libx264')
