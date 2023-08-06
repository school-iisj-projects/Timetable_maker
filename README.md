# Python on Replit
# Bit ly link - https://bit.ly/3isVrR1
This is a template to get you started with Python on Replit. It's ready to go so you can just hit run and start coding!

## Running the repl

1. Setup a new secret environment variable (the lock icon) where the key is `SECRET_KEY` and the value is
   a randomly generated token of 32 bits of randomnese. To generate such a token type this into the shell and hit Enter:
```
python
import secrets
secrets.token_urlsafe(32)
```
2. Hit run!

See this 1 minute video for a walkthrough: [https://www.loom.com/share/ecc4e738149f4d1db3bcff01758b3e71](https://www.loom.com/share/341b5574d12040fb9fcbbff150777f1c)

## Installing packages

To add packages to your repl, you can just import directly in the file you want to use the package in, and it will automatically be installed when you press the run button. Like below:
```python
import math
import pandas as pd
```

You could also install packages by using the Replit packager interface in the left sidebar.

## Help

If you need help you might be able to find an answer on our [docs](https://docs.replit.com) page. Feel free to report bugs and give us feedback [here](https://replit.com/support).


https://replit.com/join/pzumrpypub-rishitverma1






# TODO:
1. connect frontend with backend so that we can get input in the backend
2. update frontend UI using bootstrap
3. add code for database in models file so that the backed can save the data in the database
4. Add sorting algorithm
5. make a base for displaying the timetable as the number of columns and periods is not the same (using django template language to duplicate the number of rows using a class)
   -
   - use a for loop to make a new row for each class
   - put data in the table column by column for each class
   - if needed add different colour for different subject (colour can be random)
   - show the table at a new url
   - add button for saving the timetable (code added in js file)
   - add return button
   - add button for different timetable with the same subjects/teachers
     - might not always be possible, but the program can try
       - for that, each timetable class would need a separate identifier
       - probaby a string in the format "Grade[0]-period1[0]"
       - which combines the first letter of every grade and period and then comparing the string tells if the timetable is the same
         - eg:
           - if timetable = {"grade_1":{"maths":""}}