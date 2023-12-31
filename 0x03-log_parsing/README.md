# 0x03. Log Parsing

**Background context**

Log parsing is the process of analyzing and extracting meaningful information from log files generated by various software applications, systems, or devices. Log files contain a record of events, errors, and activities, and parsing them allows you to gain insights, monitor system behavior, troubleshoot issues, and generate reports. Log parsing is particularly important for system administrators, developers, and security professionals.

In Python, log parsing can be performed using various techniques and libraries.

## Task:page_with_curl:
- [0-stats.py](./0-stats.py): Python script that reads `stdin` line by line and computes metrics:
  - Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (if the format is not this one, the line must skips)
  - After every 10 lines and/or a keyboard interruption (`CTRL + C`), It prints these statistics from the beginning:
    - Total file size: `File size: <total size>`
    - where `<total size>` is the sum of all previous `<file size>` (see input format above)
    - Number of lines by status code:
      - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
      - if a status code doesn’t appear or is not an integer, it prints print nothing for this status code
      - format: `<status code>: <number>`
      - it prints stats code in ascending order
