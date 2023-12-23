# Streamlit Resource Management
(Piffy title will come with time)
A Streamlit-based Resource Management application project


## Repository structure
Anything noteworthy to discuss about the repo structure?

## New user setup
To get started with this course repository, clone this repository and install the requirements.

### 1. Clone this repository:
```
git clone https://github.com/chris-cannon90/streamlit_resource_management
```

### 2. Change into the project directory:
```
cd streamlit_resource_management
```

### 3. Make a virtual environment:

Exactly where depends on where you cloned the repository to locally, but eg:
```
python3 -m venv ~/Documents/Projects/streamlit_resource_management/venv
```
   
### 4. Activate the venv and install required packages for Streamlit to run:

Note: if you receive `PermissionError: [Errno 1] Operation not permitted` ... errors when activating the venv or installing packages, check out [this resource](https://stackoverflow.com/questions/58479686/permissionerror-errno-1-operation-not-permitted-after-macos-catalina-update).

Activate with:
```
source venv/bin/activate
```

Install packages in the requirements.txt file
```
pip install -r requirements.txt
```

### 5. Enter an app! -- Optional

From the streamlit_resource_management folder (you should already be there) and inside the venv you just activated, the command is:
```
streamlit run <folder_name_here>/Home.py
```

Once this command runs, a browser window should pop up and you'll now be able to access the application.  But again, going back to the Repository structure section of this Readme, that is atypical.  Normally you would enter an app once and only in one place (from a .py located in the root of the project). So it would be more like `streamlit run Home.py`.

### 6. To exit/shut down an app:
```
ctrl + c
```