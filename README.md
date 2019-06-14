# PyCompare
Python Compare Tool

This compare script is used for comparing multiple files (in this case defect query results within csv files) line by line to identify any changes from the oldest dated file. If there are differences, then a Compare_xxx report is created with the differences. The differences are first written, then a line to state the file being compared and any results above are new entries and then it loops through to the next defect to compare.

For my use case, this creates two seperate reports - PPP and WUPS. The two reports use two seperate list of defects to report on and compare.

Most recently, PySimpleGUI has been added to this to combine the two scripts and wrap them in a popup window prompting for the dates to compare the newest and oldest. Both reports use almost the same logic, with WUPS doing an additional step to copy the files to an 'Attachment' folder.







