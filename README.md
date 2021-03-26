# stuycs-submit

This is a program I designed for submitting assignments to bert.stuy.edu via the Terminal, for conveniency. It works on MacOS, but currently doesn't work on Windows, and may or may not work on Linux
.

## Installation

While I originally designed this program for myself, anyone is welcome to install this on their computer! To do so, do the following:

To download all the prequisites, run: ```pip3 install requests beautifulsoup4 PyInquirer``` ([if you don't have pip, follow this](https://pip.pypa.io/en/stable/installing/)).

Download the code by running ```curl https://raw.githubusercontent.com/gthompson30/stuycs-submit/main/stuycs-submit.py --output stuycs-submit.py```

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

At the bottom, write: ```alias stuycs-submit="{}/stuycs-submit"```, pasting what you copied previously in place of the curly braces (```{}```}. IMPORTANT: If there are any spaces (" ") in what you copied to clipboard (after the "alias" part of the command), add a backslash ("\") before them.

Do Ctrl+X to save the file. When prompted to "Save modified buffer", type ```y```. When prompted to edit the filename, don't change it, and press enter.

Congratulations! You should now have stuycs-submit installed on your computer! To test if this is working, 

## Authentication

stuycs-submit stores your information login information permanently on your computer, so you only need to log in once.

To log in, run the following:

```stuycs-submit authenticate```

This will prompt you for period, name, and password, to log in. To answer any prompt, use the up and down arrows, and press enter to submit the answer.

If you enter any of your information wrong, the program will alert you, and you'll have to rerun the command to authenticate again.

After authentication, you will be able to submit any file to assignment!

## How to Submit

To submit any file, run the following:

```stuycs-submit [FILE]```, replacing "[FILE]" with your file name (you need to be in the same directory, or give the relative file path).

The program will then prompt you which assignment to submit to, and then will prompt you to make a comment to teacher, similarly to on the homework server.

To make no comment, simply press enter without typing anything.

This should submit your file to the specified assignment! The program will give you a link to view the assignment on the homework server, and you can also check on the homework server to verify that the assignment was submitted.

## Do I steal your passwords?

No (:
