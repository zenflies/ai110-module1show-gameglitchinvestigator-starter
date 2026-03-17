# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").

---

  One critical bug is the flipped logic for the hints, since making guesses will put you in the opposite direction.
  Another critical bug is that the number of attempts on screen does not match the amount of attempts you actually have. The game will terminate early by one attempt.
  A third bug is that the attempt counters are inconsistent when clicking between difficulties. 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

  For this project, I used Claude for help with bugfixes and code analysis. 
  One example where AI was correct was their integration with the logic_utils.py file for fixing the check_guess() function to have the hints correctly correspond with the user input. I verified this result through playtesting with the app at runtime.
  An example where the AI was slightly misleading was their suggestion for fixing the off-by-one error in attempt difficulties; the AI suggested changing the attempt incrementing subsystem, which would be more complicated than correctly setting the attempt state to zero. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

  I identified flawed bugs by comparing design intent to playtesting. Taking the objective of the game and service, I was able to find contradictions in the behavior and functionality of the program. One test I ran used pytest to check whether the hint returns matched the real feedback of the guess; if the guess was too high, the message should return that the guess was too high. AI helped in designing this test case, parsing what I wanted to assert and formulating that into proper syntax.

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

  Since the secret number was re-generated later on in the code, it would change because of how Streamlit re-runs the entire python file each time a modification to the page is made. This includes clicking a button or drop-down menu, causing the secret number to be calculated unintentionally. The variable had to be stored in a specific session state variable which would allow it to be consistent across all runs.

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit that I want to re-use was my continual commit and push of project progress to the GitHub, which allowed me to periodically save major changes in my code for remote work or restoring previous, working versions. Next time I work with AI on a coding task, I will contextualize my goals more to avoid follow-up questions, which minimize hallucinations. This project changed the way I think about AI generated code by qualifying the production value - it requires human verification to push and ensure the written logic is correct and suitable for development.
