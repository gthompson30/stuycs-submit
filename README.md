# stuycs-submit

This is a program I designed for submitting assignments to bert.stuy.edu via the Terminal, for conveniency. It works on MacOS, but is currently .

## Installation

While I originally designed this program for myself, anyone is welcome to install this on their computer! To do so, do the following:

To download all the prequisites, run: ```pip3 install requests beautifulsoup4 PyInquirer``` ([if you don't have pip](https://pip.pypa.io/en/stable/installing/)).

Download and run [this](https://github.com/gthompson30/stuycs-submit/blob/main/stuycs-submit.py) file (using ```python3```).

Open the directory of the download in Terminal, and run ```python3 stuycs-submit.py setup```. Then follow the instructions below to add ```stuycs-submit``` as a Terminal command:

```
cp stuycs-submit.py stuycs-submit
cd ~/
```

Next, to add the custom command for ```stuycs-submit```, do the following:

Run the command ```pwd```, and copy its output to clipboard.

Then, run the following command:
```
nano .bash_profile
```
This will open up a GUI to edit .bash_profile. Go to the bottom of the file with the arrow keys, or via Ctrl+V.

At the bottom, write: ```alias stuycs-submit="{}/stuycs-submit"```, pasting what you copied previously in place of the curly braces (```{}```}. IMPORTANT: If there are any spaces (" ") in what you copied to clipboard, add a backslash ("\") before them.

Do Ctrl+X to save the file. When prompted to "Save modified buffer", type ```y```. When prompted to edit the filename, don't change it, and press enter.

Congratulations! You should now have stuycs-submit installed on your computer! To test if this is working, 
