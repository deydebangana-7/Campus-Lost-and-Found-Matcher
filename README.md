## Campus Lost & Found Matcher

## Overview

Campus Lost & Found Matcher is a Python-based console application designed to help college students report lost and found items and identify possible matches between them.

The application stores item reports in a JSON file and compares details such as item name, brand, color, location, date, and description to calculate a match percentage.

## Features

* Report a lost item
* Report a found item
* Automatically generate report IDs
* Validate user input
* Validate dates in DD/MM/YYYY format
* Store reports using JSON
* Compare lost and found items
* Calculate a match percentage
* Classify matches as Strong Match, Good Match, or Possible Match
* View all lost and found reports
* Sort possible matches by match percentage

## Technologies and Tools Used

* **Python 3.11.9**
* **JSON** for data storage
* **VS Code** for development
* **Git and GitHub** for version control and project submission

## Project Structure

```text
Campus_Lost_&_Found_Matcher
│
├── main.py
├── matching.py
├── storage.py
├── validation.py
├── reports.py
├── data.json
├── README.md
├── statement.md
└── .gitignore

### File Description

* `main.py` – Controls the main menu and overall program flow.
* `matching.py` – Contains the item matching and scoring logic.
* `storage.py` – Handles loading and saving data in JSON format.
* `validation.py` – Handles input and date validation.
* `reports.py` – Displays reports and matching results.
* `data.json` – Stores lost and found item reports.
* `statement.md` – Contains the problem statement, scope, target users, and high-level features.
* `.gitignore` – Specifies files that should not be uploaded to GitHub.

## How the Project Works

1. The user starts the application.
2. The user chooses an option from the main menu.
3. The user can report a lost item or a found item.
4. The entered information is validated.
5. The report is saved in `data.json`.
6. The user can select **Find Matches**.
7. The application compares lost and found reports.
8. A match percentage is calculated based on the available details.
9. Possible matches are displayed from highest to lowest score.

## Match Criteria

| Criteria    | Maximum Score |
| ----------- | ------------: |
| Item        |            30 |
| Brand       |            15 |
| Color       |            15 |
| Location    |            15 |
| Date        |            10 |
| Description |            15 |
| **Total**   |       **100** |

### Match Classification

* **80–100%** → Strong Match
* **65–79%** → Good Match
* **50–64%** → Possible Match
* **Below 50%** → Not displayed as a possible match

## How to Install and Run

### Requirements

Python 3.11 or later should be installed on the system.

### Running the Project

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python main.py
```

5. Select an option from the menu.

## Testing Instructions

The application can be tested by:

1. Adding a lost item report.
2. Adding a found item report.
3. Entering similar details in both reports.
4. Selecting **Find Matches**.
5. Checking the calculated match percentage.
6. Selecting **View Reports** to verify stored reports.
7. Testing invalid inputs such as blank fields, invalid dates, and invalid menu choices.

## Data Storage

The project uses a `data.json` file to store lost and found item reports. The data is automatically updated whenever a new report is submitted.

## Future Enhancements

Possible future improvements include:

* A graphical user interface
* A web-based version
* User authentication
* Image-based item matching
* Notifications when a possible match is found
* Database-based storage
* Search and filtering options

## Author

**Debangana Dey**

B.Tech Computer Science and Engineering
VIT Bhopal University
