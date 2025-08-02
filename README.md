# UK Mobile Phone Number Detector

This Python script scans through a block of text to detect UK mobile phone numbers in common formats. It supports both international (`+447...`) and domestic (`07...`) formats.

## 📌 Features

- Detects valid UK mobile numbers in:
  - International format: `+447XXXXXXXXX`
  - Domestic format: `07XXXXXXXXX`
- Ignores invalid or malformed numbers.
- Prints all found numbers to the console.

## 🧠 How It Works

The core function `isUkMobilePhoneNumber(text)` checks whether a given string matches a valid UK mobile number format. The script then iterates over every possible substring of length 11 or 13 in the input text to find valid numbers.

### Formats Checked:

- `+447XXXXXXXXX` (13 characters)
- `07XXXXXXXXX` (11 characters)

### Example:
```python
message = "Call me on +447377427818 tomorrow. 415-555-9999 is my office line. But +447939939049 is my alternative mobile number. Also, try 07700123456 or 07123456789."
```

#### Output:
```
Phone number found: +447377427818
Phone number found: 07700123456
Done
```

## 📂 Files

- isUkMobilePhoneNumber.py: Main script containing phone number detection logic.
- README.md: This documentation file.

## ✅ Requirements

- Python 3.x
- No external libraries required. The script uses only built-in functions.

## 🧪 Testing & Customisation
- Modify or expand the ```isUkMobilePhoneNumber()``` function to support additional formats like:
  - Numbers with spaces ```(+44 7123 456789)```
  - Numbers with dashes or brackets

- Use this function in:
  - Web form validation
  - Chat and message filtering
  - Contact info extraction tools
  - Data-cleaning pipelines
