<p align="center">
	<img src="assets/logo.png" alt="drawing" width="160"/>
</p>
<h1 align="center">
  Hackathon Video Generator
</h1>

By team _ScriptinQuarantino_ for the Hacklarious Hackathon 2020

### Introduction
Everytime Jaime and I join a hackathon, we need to **calculate half a day or even a full day for making a short video about our hackathon project**. It is lots of fun, but in general we always end up using a similar concept:

* We present out team
* We name our project & show the logo
* We say what is the problem we are trying to solve
* We list three points of how we solve it
* We show a demo
* We explain the solution architecture
* And finally, we thank the hackathon organizers

And in the background we put a suitable, royalty free commercial song that makes everything sound credibe.

With **Hackathon Video Generator** we want to **save ourselves a bit of time that we have before the hackathon deadlines**, so we can use it on optimizing our solutions instead.

Now we had less than 20 hours to figure out how to finish this hackathon project... if only we had a solution that could make the video for us so we would have enough time?

### How it works
Hackathon Video Generator works in the following way:

1. It takes an input configuration yaml file which contains all necessary details about the project & which language the video should be in. Often, most information can be copy pasted from your gitlab repo, if it is properly documented
2. It looks for images based on keyword extraction, that it can use in the presentation.
3. It generates an mp3 and slides that can directly be used for your video.

### Technical setup

Our solution works with a python script ([hackathon-video-creator.py](hackathon-video-creator.py)) to generate the video audio and an R script ([generate-slides.R](generate-slides.R)) to generate the slides.

The details about the hackathon project can be specified in the [config.yaml](config.yaml) file. 

Once that is done, you can generate the markdown for the slides by running:

```R
R generate-slides.R
```
For this you need to have R and the yaml package installed. You also need a Giphy API key.

This fills in the markdown template with the hackathon details, to generate the slides, run:

```bash
darkslide slides.md -i
```
For this command you need python & the darkslide package (`pip install darkslide`) for more info see [link](https://pypi.org/project/darkslide/).

To generate the mp3 with the audio, run:

```python
python hackathon-video-creator.py
```
This script requires the following packages installed: [...]