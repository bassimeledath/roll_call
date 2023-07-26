# roll_call

## Description
This is a simple roll call application that calls out the names of students in the data folder (has to be provided) by running .mp3 files. The mp3 files are created by the text_to_speech.py script. The user can specify a lag time to determine time between name calls and can also specify what name to start with. All names are called in alphabetical order.

## Usage
Before you run the application make sure to have a names.txt file and data folder in the root. To populate the data folder with mp3 files of name calls, run the text_to_speech.py script:

```python
python3 text_to_speech.py
```

The names.txt file should contain the names of the students in the class, each one separated with a comma. For example:

```python
Raj, Priya, Ravi, Anjali, Rahul, Anushka, Rohan, Ananya, Rohit, Anika, Rakesh, Pooja
```

To run the application, simply run the following command in the terminal:

```python
python3 roll_call.py   
```

To begin roll call with a specific name run the below. Don't worry about getting the exact full name, the script will find the name that starts with the string you provide. The succeeding names will be called in alphabetical order.
    
```python
python3 roll_call.py <name>
```

