Title: Create a Windows batch script
Date: 2017-09-07 10:43
Authors: José Aniceto


A batch file is a text file with the extension **.bat** that contains one or more command line commands to be run consecutively. 

## Some usefull commands:

**@echo** - This parameter will allow you to view your working script in the command prompt. This parameter is useful for viewing your working code. If any issues arise from the batch file, you will be able to view the issues associated with your script using the echo function. Adding a following off to this parameter will allow you to quickly close your script after it has finished.

**title** - This will provide a title for your batch script in your Command Prompt window.

**cls** - Clears your command prompt, best used when extraneous code can make what you’re accessing had to find.

**rem** OR **::** - Shorthand for remark. Rem statements are not entered into your code. Instead, they are used to explain and give information regarding the code.

**%%a** - Each file in the folder.

**(“.\”)** - The root folder. When using the command prompt, one must direct the prompt to a particular directory before changing a files name, deleting a file, and so on. With batch files, you only need to paste your .bat file into the directory of your choosing.

**pause** - Allows a break in the logical chain of your .bat file. This allows for users to read over command lines before proceeding with the code. The phrase “Press any key to continue…” will denote a pause.

**start “” [website]** - Will head to a website of your choice using your default web browser.

A complete list can be found [here](https://en.wikibooks.org/wiki/Windows_Batch_Scripting).

## Useful batch files:

### Start Flask server

The following script starts a Flask development server provided the batch file is located in the project root directory.

```
echo off
cd %localhost%
call venv\Scripts\activate.bat
start python dashboard\__init__.py
pause
```
