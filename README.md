# First and Last Characters Extractor

## Overview

The First and Last Characters Extractor is a simple Python application that creates a new string by combining the first two and last two characters of a user-entered word. This project serves as a practical introduction to string slicing and basic string manipulation.

## Features

* Accepts a word from the user.
* Extracts the first two characters.
* Extracts the last two characters.
* Combines both parts into a new string.
* Uses a function to organize the logic.

## Technologies Used

* Python 3

## Project Structure

```text
First-Last-Characters-Extractor/
│
├── first_last_characters.py
└── README.md
```

## How to Run

1. Ensure Python 3 is installed.
2. Save the program as `first_last_characters.py`.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python first_last_characters.py
```

## Example

### Input

```text
Enter your word : Python
```

### Output

```text
Pyon
```

Explanation:

* First two characters: `Py`
* Last two characters: `on`
* Combined result: `Pyon`

### Additional Examples

| Input  | Output |
| ------ | ------ |
| Python | Pyon   |
| Hello  | Helo   |
| Coding | Cong   |
| World  | Wold   |

## How It Works

1. The program asks the user to enter a word.
2. The word is passed to the `first_last_characters()` function.
3. The function extracts:

   * The first two characters using:

```python
word[0:2]
```

* The last two characters using:

```python
word[-2:]
```

4. The two substrings are concatenated together.
5. The resulting string is returned.
6. The program displays the final result.

## Program Flow

```text
User Input
     ↓
Extract First Two Characters
     ↓
Extract Last Two Characters
     ↓
Combine Both Strings
     ↓
Display Result
```

## Concepts Demonstrated

* Functions
* String slicing
* String concatenation
* User input
* Return values
* Basic string manipulation

## Known Limitation

The current implementation assumes that the user enters a word containing at least two characters.

For example:

```text
Input: A
Output: AA
```

This occurs because Python's slicing behavior returns available characters even when the requested range exceeds the string length.

A possible improvement is to validate the input length:

```python
if len(word) < 2:
    return "Input must contain at least two characters."
```

## Future Improvements

* Handle short strings more gracefully.
* Allow users to process multiple words in one session.
* Display the extracted parts separately before combining them.
* Support sentences and phrases in addition to single words.
* Add options to extract a customizable number of characters.

## Author

Created as a Python practice project to demonstrate string slicing, concatenation, and function-based programming.
