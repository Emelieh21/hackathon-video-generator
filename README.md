# Hackathon Video Generator

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
