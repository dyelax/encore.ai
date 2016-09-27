#encore.ai
Generate new lyrics in the style of any artist using Deep Learning. <br/>
Winner of "Best Machine Learning Hack" at HackMIT!

Check it out at http://encore.ai.

<img src="https://github.com/dyelax/encore.ai/blob/development/assets/devpost_img_2-01.png" style="width: 100%"/>


##Music Lives Forever.
From Elvis to The Beatles, Nirvana to Tupac, many of the musicians we love are no longer creating. encore.ai lets you revive the spirit of your favorite artists in the modern age.

##We are impatient.
Cant wait for the next Kanye album to drop? Were you part of the public outcry over the delayed release of Frank Ocean's new record? Fret no more – encore.ai delivers your favorite artist's next single at the touch of a button.

##But How Does It Work?!
We used TensorFlow to create an LSTM (Long Short Term Memory) Neural Network that reads all of the lyrics of any musical artist. The network learns the style of how the artist writes – the context of words, rhymes, line/stanza breaks, etc. Given a seed word or phrase, it will generate a new song in that artist's style.

##Some Examples:

###Kanye West

Never I admit I can't do I see a drug som... <br />
I’m ’bout to re-united <br />
I'll need have to play me alone <br />
I'll fade back O extra until they cover from an ultralight beam <br />

Because you do her money before my Sean harder <br />
Now, 2 West I one away<br />
I’m up, so quit, One:] <br />
yeah, I will <br />
You see, you need)<br /> 
All your mic from a moment<br /> 
I'm saying, violate<br />

Let’s got no goodbyes to a dem me <br />
now? <br />
I been nothing funny but we go n****<br />
Get all my racks steps <br />

And rockin' (Grandma) watch my strippers got getting this bitch a shot, is like somebody It's old shit <br />
And oh precious *<br />
Cause we call that ready for not <br />

[Hook] <br />
It's an room 2 now, in the restaurant, clothing on. <br />
Standing dem my money <br />

[Kanye West:] <br />
Let's fly off beats that I’m at these good life with you <br />
keep the big ass, take my things and throw my shit’s is stronger<br />


###Taylor Swift

paper lying here <br />
'Cause I swear out there ain't where <br />
You outta be <br />
And you flashback to when he said forever and always <br />
Oh, and it rains in your bedroom <br />
Everything is wrong <br />
It rains when the sun came up, you were lookin' at me <br />
Santa baby, forgot to mention one little thing <br />
A ring

And I don't think it all through? All these things will change<br />
Can you feel it now? <br />
I fall in love with you <br />
Give me a photograph to hang on my wall, superstar <br />

How'd we got problems <br />
And I don't think we can solve them <br />
You were the prince <br />
I used to see <br />
The one we danced to all night long <br />

Cause you got me a nice new apartment <br />
In a city, wouldn't you have to make me go back there again." <br />

Find the wrong wrong <br />
On our last night <br />
Ooh, ooh, love's like this <br />
It's something I missed <br />
Ooh, ooh, ooh, ooh <br />
It was the best night, never would forget how he moved.

##  Instructions to Train:

If you want to use our model to train your own artists, follow these steps:

1. Pick an artist – it should be someone with a lot of lyrics. (Over 100,000 words).
2. Collect all of the artist's lyrics from your favorite lyrics website. Save each song as a text file in `data/artist_name/`. We recommend leaving newlines in as a special token so that the network will learn line and stanza breaks.
3. Train by navigating to the `code` directory and running  `python runner.py -a <artist_name> -m <model_save_name>`.
  - Our models were all trained for 30,000 steps.
4. Generate new songs by  running  <br />`python runner.py -a <artist_name> -l ../save/models/<model_save_name>/<ckpt_file> -t`.
  - Optional: If you would like to specify "prime text"  – the initial text that the model will generate from – pass in a string with the `-p` flag.
5. Share your trained models with us so we can feature them on our website! Create an issue with a link to a public Dropbox or Google Drive containing your model's .ckpt file.
