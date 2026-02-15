import os
import cv2
from moviepy.editor import *

def create_video_from_images(image_folder, output_video_file, audio_file=None, fps=30):
    # Collect images from the folder
    images = [img for img in os.listdir(image_folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
    images.sort()  # Ensure the images are in order

    # Create video from images
    clips = [ImageClip(os.path.join(image_folder, img)).set_duration(1/fps) for img in images]
    video = concatenate_videoclips(clips, method='compose')
    
    # Add audio if provided
    if audio_file:
        audio = AudioFileClip(audio_file)
        video = video.set_audio(audio)

    # Write video file
    video.write_videofile(output_video_file, fps=fps)

if __name__ == '__main__':
    create_video_from_images('path/to/images', 'output/video.mp4', 'path/to/audio.mp3')