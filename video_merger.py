import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

def merge_videos(video_list, output_filename):
    clips = []
    for video in video_list:
        clips.append(VideoFileClip(video))
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_filename)

if __name__ == '__main__':
    videos_to_merge = ['video1.mp4', 'video2.mp4', 'video3.mp4']  # Add your video files here
    output_file = 'merged_video.mp4'
    merge_videos(videos_to_merge, output_file)