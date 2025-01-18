# Higher or Lower Game in Python

This project is a Python-based **Higher or Lower** game where players compare the follower counts of two accounts and guess which account has more followers. The game dynamically pulls account data and provides an interactive experience with a scoring system.

---

## Features

1. **Dynamic Account Data**:
   - Includes a list of accounts with names, follower counts, descriptions, and countries.
   - Randomly selects accounts for comparison.

2. **Interactive Gameplay**:
   - Players input guesses based on account follower counts.
   - Immediate feedback on whether the guess is correct.

3. **Scoring System**:
   - Keeps track of the player's score.
   - Ends the game when the player guesses incorrectly.

4. **Artistic UI**:
   - Displays ASCII art for the logo and comparison (via `higherloergame_art`).

5. **Clean Console Output**:
   - Clears the screen after each round for better readability (using `os.system('cls')`).

---

## How It Works

1. **Initialization**:
   - The game imports data from `database_higherlower_game` and `higherloergame_art`.
   - Starts with a score of `0`.

2. **Gameplay Loop**:
   - Two random accounts are selected from the `data` list for comparison.
   - Players guess which account has more followers by typing `1` or `2`.

3. **Feedback**:
   - If the guess is correct, the score increments, and a new account is selected for comparison.
   - If incorrect, the game ends and the final score is displayed.

4. **Account Comparison**:
   - The follower counts of the two accounts are compared to determine correctness.

---

## Code Structure

### **Data Source**
The `data` list contains dictionaries with account details:
```python
{
    'name': "harii",
    "follower_count": 1,
    "description": "youtuber",
    "country": "india"
},
```

### **Functions**
1. **`display_accountinfo(account)`**:
   - Formats and displays account details (name, description, country).

2. **`check_answer(guess, follower_count1, follower_count2)`**:
   - Compares the follower counts and validates the player's guess.

3. **`os.system('cls')`**:
   - Clears the console for a clean UI after each round (on Windows systems).

---

## How to Run

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```bash
   cd <project-directory>
   ```

3. Run the script:
   ```bash
   python higher_lower_game.py
   ```

---

## Example Usage

### Sample Output:
```plaintext
 _____ _     _                       _              
|  |  |_|___| |_ ___ ___ ___ ___ ___| |_ ___ ___ ___
|  |  | |   |  _| .'|   | .'|  _| -_|  _| . |  _| -_|
 \___/|_|_|_|_| |__,|_|_|__,|_| |___|_| |___|_| |___|

Compare1: harii a youtuber from india
  _    _
 | |  | |
 | |__| | ___  _ __ ___   ___  _ __
 |  __  |/ _ \| '_ ` _ \ / _ \| '_ \
 | |  | | (_) | | | | | | (_) | | | |
 |_|  |_|\___/|_| |_| |_|\___/|_| |_|

Compare2: messi a footballer from aregentina
Who has more follower? Type 1 or 2:
```

### Correct Guess:
```plaintext
You are right and your score is 1
```

### Incorrect Guess:
```plaintext
You are wrong and your score is 3
```

---

## Customization

### Adding New Accounts:
To add more accounts to the game:
1. Update the `data` list with new dictionaries:
   ```python
   data.append({
       'name': "New Account",
       "follower_count": 100,
       "description": "profession",
       "country": "country_name"
   })
   ```

### Modifying ASCII Art:
Update the art in `higherloergame_art` to customize the logo or other visuals.

---

## Dependencies
- Python 3.6 or higher
- `os` module (for clearing the console)
- `random` module (for selecting accounts)

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---



## Contact
For questions or feedback, please contact Shajan J Jacob.

