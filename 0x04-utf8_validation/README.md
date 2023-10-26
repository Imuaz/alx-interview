# 0x04. UTF-8 Validation

**Background context**

UTF-8 (Unicode Transformation Format - 8-bit) is a character encoding standard used to represent text in various scripts and languages using a variable number of bytes. It's widely used on the internet and in computing.

Here's how it works:
- **Basic Idea**: UTF-8 encodes characters as a sequence of bytes. The number of bytes used depends on the character being encoded, ranging from 1 to 4 bytes.
- **ASCII Compatibility**: The first 128 characters (0-127) are identical to the ASCII encoding. This means that regular ASCII text is also valid UTF-8.
- **Variable Length**: Characters outside the ASCII range (128-1,112,063) are encoded using multiple bytes. The first byte of a multibyte sequence starts with 11, followed by 0s, and the subsequent bytes start with 10.

UTF-8 is efficient for text that uses predominantly ASCII characters but is also capable of representing a vast array of characters from various languages and symbol sets. Its variable-length encoding allows it to be space-efficient while being highly versatile.

## Tasks:page_with_curl:
**0. UTF-8 Validation**
- [0-validate_utf8.py](./0-validate_utf8.py): A method that determines if a given data set represents a valid UTF-8 encoding.
  - Returns: True if data is a valid UTF-8 encoding, else returns False
  - A character in UTF-8 can be 1 to 4 bytes long
  - The data set can contain multiple characters
  - The data will be represented by a list of integers
  - Each integer represents 1 byte of data, therefore it only handles the 8 least significant bits of each integer


