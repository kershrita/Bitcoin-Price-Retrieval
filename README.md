# Bitcoin Price Retrieval GUI Program

This program is a simple graphical user interface (GUI) application that allows users to retrieve the historical price of Bitcoin based on a selected date. The program fetches the Bitcoin price data from a CSV file and displays it in the GUI.

## Table of Contents

- [Features](#features)
- [Getting Started](#getting-started)
- [Contributing](#contributing)

## Features

- Allows users to select a date using a calendar widget.
- Fetches the Bitcoin price for the selected date from a CSV file.
- Displays the retrieved Bitcoin price in the GUI.
- Shows an error message if the selected date is outside the valid range.

## Getting Started

To run the Bitcoin Price Retrieval GUI Program, you need to have the following:

1. Python (version 3.6 or higher) installed on your system.
2. Required Python libraries installed. You can install the necessary libraries by running the following command:
```
pip install pandas tk tkcalendar
```
3. Clone program's source code.
```
git clone https://github.com/kershrita/Bitcoin-Price-Retrieval.git
```
4. Make sure you have a CSV file named [bitcc.csv](bitcc.csv) containing the Bitcoin price data.
5. Run the code, the GUI window will appear, displaying a calendar widget.
6. Select a date from the calendar widget.
7. Click the "Submit" button to retrieve the Bitcoin price for the selected date.
8. If the selected date is within the valid range, the retrieved Bitcoin price will be displayed in the GUI.
9. If the selected date is outside the valid range, an error message will be shown.

## Contributing

Contributions to the Bitcoin Price Retrieval GUI Program are welcome. If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request. Please follow the contribution guidelines specified in the repository.