# BookBot

BookBot is a simple Python program that analyzes text files and provides statistics about them.

## Features

- Counts the total number of words in a text file
- Counts the frequency of each character (case-insensitive)
- Displays results sorted by character frequency

## Usage

Run the program from the command line with a path to a text file:

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.txt
```

## Output

The program will display:
- The file path being analyzed
- Total word count
- Character frequency count (alphabetic characters only, sorted by frequency)

## Requirements

- Python 3.x

## Project Structure

- `main.py` - Main program entry point
- `stats.py` - Statistics calculation functions
- `books/` - Directory for text files (gitignored)

## License

This project is part of the Boot.dev curriculum.
