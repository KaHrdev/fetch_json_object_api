# fetch_json_object_api

A short Python script to:
- Fetch JSON Object via GET API Call to https://data.vatsim.net/v3/vatsim-data.json
- Extract only the objects called "controllers" and "atis"
- Then return the parsed object to give just the "callsign" and matching "frequency" for each sub-object within "controllers" and "atis".
[example]
"callsign": "1859105_OBS",
"frequency": "199.998",
[/example].

---

## Table of Contents

1. [Requirements](#requirements)  
2. [Installation](#installation)  
3. [Usage](#usage)  
4. [Features](#features)  
5. [FAQ](#faq)  
6. [Contact](#contact)  

---

## Requirements

Before running the script, ensure you have the following installed on your computer:  
- [Python](https://www.python.org/downloads/) (version 3.x or higher).  
- The ability to create a Python virtual environment (`venv`).  
- The `requirements.txt` file included in the project folder.  

---

## Installation

1. **Download or clone the repository**  
   ```bash
   git clone https://github.com/KaHrdev/fetch_json_object_api.git
   cd fetch_json_object_api

2. **Create and activate a virtual environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

---

## Usage

1. **Run the main script to fetch and process data**
   ```bash
   python main.py

2. **Output will display the initial and processed data in JSON format**

---

## Dependencies

#### This project requires the following Python packages
- certifi==2024.8.30
- charset-normalizer==3.4.0
- idna==3.10
- requests==2.32.3
- urllib3==2.2.3

All dependencies are listed in requirements.txt. Use pip install -r requirements.txt to install them.

---

## Additional Notes
- The .gitignore file excludes virtual environments (env/) and Python cache files (__pycache__/) to maintain a clean repository.
