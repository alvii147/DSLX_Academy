# HackTX 2020
## Inspiration
Children with dyslexia often have problems with reading and writing skills, including differentiating sounds in speech, learning letters, reversing sounds in words, and often confuse words that sound alike. This often leads to dyslexic children falling below academic expectations. 
  
![Infographic](https://www.readinghorizons.com/Media/Default/Images/Resources/dyslexia_infographic3-01.jpg)
*[flickr](https://www.flickr.com/photos/55512706@N03/30427492672)*  
  
We want to help these children by providing them with a dyslexic-friendly environment with activities that can support their growth and development of skills. By designing a simple interface, we want to support children, as they are just beginning to explore and work with their disability.

## What it does
The page consists of 4 pages: Home, About, Handwriting, and Practice. The home page is a user-friendly page that shows the name of the project: ***DSLX Academy.***

The Handwriting page includes a game where the user is given a word to practice writing with the mouse as a pencil. The user then receives a response regarding accuracy from Google Cloud Vision.

The Practice page includes two games. The first is a game where the user is given a word and is asked to repeat it. It then returns if the user said the correct word. It also asks the user to enter the number of syllables in the word. The second is a game that provides statistics regarding the user's accuracy in reading a paragraph, including number of pauses and articulation rate.  
  
Click image below for demo video (or click [here](https://youtu.be/zFMFPs3CKh0))
[![Video_Thumbnail](http://i3.ytimg.com/vi/zFMFPs3CKh0/maxresdefault.jpg)](https://youtu.be/zFMFPs3CKh0)

## How we built it
This was built using **Flask** and **JavaScript** for the back-end, and **Bootstrap,** **HTML,** and **CSS** for the front-end. **Google Cloud Vision** and **Microsoft Azure Cognitive Services** Speech-to-Text were used for the handwriting and speaking features, respectively. The Python library used for the speech analysis was **my-voice-analysis.** We designed the webpage to be simple and concise, so as to ensure the least distraction possible. We also designed the logo as an upward-angled plant that symbolizes growth.

## Challenges we ran into
We had issues with centering on the webpage using CSS. Additionally, since we had never used the my-voice-analysis before, we faced a challenge in debugging to determine why the voice file was not being parsed. 

## Accomplishments that we're proud of and what we learned
We were proud of ourselves for figuring out how to use Microsoft Azure's Speech-to-Text service and implementing the my-voice-analysis library. Additionally, we were proud that we were able to develop a simply, dyslexic-friendly website.

## What's next for ***DSLX Academy***
We want to bring ***DSLX Academy*** to the classroom, where teachers can introduce the activities to students who have dyslexia.  
  
![logo](dslx_logo.gif)