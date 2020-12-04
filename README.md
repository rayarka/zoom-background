# Create a (simple) customized zoom video background with your logo

## Output

Combine a **logo**

<img src=https://user-images.githubusercontent.com/25000887/101201783-3b749f80-36a3-11eb-9d57-9522d7929795.png height=200></img>

With a **video background**

<img src= https://user-images.githubusercontent.com/25000887/101202280-074dae80-36a4-11eb-907e-c562f459bdc4.gif height=200></img>

To get this background:

<img src=https://user-images.githubusercontent.com/25000887/96777212-a2543700-141c-11eb-93b2-b640a71a6e87.gif height=200></img>

*For the above, you can find the original background here: https://www.youtube.com/watch?v=mciTVPwF3Lw. Additionally, the actual logo used was white in colour*

**Another example**
This [background](https://www.youtube.com/watch?v=y2T_jfKLDR4) was made with this program. You can see it in use [here](https://youtu.be/NS3S5Mw43Ho?t=4473):

![b2](https://user-images.githubusercontent.com/25000887/96777680-34f4d600-141d-11eb-8031-b4a8ef70c14e.gif)

## What you'll need:
1. Download the video you wish to use (mp4 preferably). *A potential improvement would be to integrate the youtube_dl or another similar module and allow the user to select a video based on url*
2. Download the picture you wish to use (png preferably)
3. Clone this repo
4. Run **pip install -r requirements.txt** to download the moviepy module (You will probably need to install ImageMagick as well, separately)
5. Run **zoom_bkgrnd_logo.py**
6. Use the GUI to choose your video file
7. Use the GUI to choose your logo
8. Use the GUI to choose a save location
9. Patience (the longer the video, the more time it will take) *A potential improvment would be to allow the user to choose segments of the video to use as a background or to allow them to loop/reverse the video*
10. The video should be ready to use!

*Other possible improvements include:*
- making it a web app
- allowing the user to select the location of the logo
- allowing the user to use video logos instead of simple picture logos
- enabling addition of multiple logos


Disclaimer: This is my first proper github contribution to the world. Pardon me if I didn't follow certain conventions, as I'm probably unaware of them.
