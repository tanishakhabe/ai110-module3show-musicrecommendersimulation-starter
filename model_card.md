# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

Music Match 1.0
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

This recommender is designed to generate top-ranked song suggestions based on a user’s unique preferences, including genre, mood, and audio traits including energy, tempo, valence, danceability, and acousticness. It assumes users can describe their taste in a structured way that reflect what they like in a song. It also assumes that songs with closer feature values are better matches and that exact genre/mood labels are meaningful signals.

This project is best framed as a classroom exploration, where the goal is to understand recommendation logic, tradeoffs, and bias, rather than to serve real users in production.


---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

My recommender looks at each song’s genre, mood, energy, tempo, valence (positivity), danceability, and acousticness, then compares those values to what the user says they want. It uses user preferences for the same fields, so a song gets rewarded when it is close to the target and penalized when it is far away. Genre and mood are treated like direct label matches, while the numeric features are scored by how close they are to the user’s target range. After scoring every song, the model sorts them from highest score to lowest and returns the top results, along with short reasons for why each song ranked well. 

From the starter logic, I replaced it with a full weighted scoring system, included mismatch penalities for the features, and tested a weight experiment where we increased the effect of energy and decreased the effect of genre on a scoring. 


---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  


There are 18 songs in the catalog. The genres epresented are pop, lofi, ambient, jazz, synthwave, classical, funk, metal, soul, EDM, country, reggaeton, and folk. The moods represented are happy, chill, intense, focused, relaxed, upbeat, aggressive, warm, nostalgic, etc. 

Because the the original catalogue was small, I ended up adding more data to create a more diverse data set. However, the dataset does miss real-world taste diversity, including multilingual music and context-specific preferences (for example: listening to classical when studying, pop when working out, etc.).
---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

For really distinct user profiles (pop lovers, lofi chill, etc.) the system gives recommendations with very high confidence and high scores. For those instances, the model is good at recommending songs that match both the user's preferred genre and mood. 

For example for the hype profile, the system recommended "Gym Hero" which makes sense and matches my intuition. 

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The current scorer can create a filter bubble because it gives a large bonus to exact genre and mood matches, so recommendations tend to cluster around a user’s stated identity rather than exploring nearby alternatives. It also has a binary bias toward exact string matches, which means small input differences like casing or a slightly different genre label can drop a song out of the bubble entirely instead of treating it as close. The weakness that showed up during experimentation was the sparse lofi profile: with only genre = lofi, Focus Flow, Library Rain, and Midnight Coding all tied, and the alphabetical tie-break in recommender.py picked Focus Flow, so the output was driven more by naming than by any deeper preference signal. In practice, that means the system can over-concentrate results and still look precise even when it is mostly just sorting on one dominant feature.

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

The user profiles we tested were high energy pop, chill lofi, deep intense rock, hype sad, intense pop with chill, and lofi with missing features.

What surprised me about the results is that a lot of the same songs were being recommended for all of the profiles, such as Gym Hero was being recommended for the high energy pop, hype sad, and intense pop with chill profile. 

The chill lofi profile has very different song rankings from the high-energy pop profile because it lowers energy and shifts both genre and mood toward a calmer, more acoustic sound. 

The deep intense rock profile outputs louder, faster, and less mellow songs than chill lofi. 

Hype sad still outputs energetic tracks, especially after the experiment, probably because genre and mood carry a lot of weight. 

Intense pop with chill preferences produced more mixed results because it included high-intensity pop tracks with low energy and high acousticness, probably due to competing signals in the score.

The missing features lofi profile mostly just returns results that match the corresponding genre because there were no other preferences provided. 
---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

In the future, I would add time of day or context feature as well to the model. So the system can recommend different songs based on whether the user is studying, working out, or sleeping, etc. 

I would also maybe look at the artist feature because I didn't use it in the original system. In the future, matching artist preference could be a tie breaker amongst songs that are similarly ranked. 

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

I learned how the architecture of recommender systems is organized and what the inputs and outputs of the system look like. Something interested I discovered is how recommendations can sometimes be forced to be binary or siloed if the model is not very flexible. I also learned about the importance of data quality and variety, since we want to train the model on a diverse set of songs and user preferences to improve generalization to new, unseen user profiles. 

I have a bigger appreciation of music recommendation systems now, like the systems on apps such as Spotify and Apple Music, because of the large amounts of data they handle and use to make perfectly curated recommendations and playlists for each user.