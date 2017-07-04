Logs analysis project
=====================

### By Alberto Miravete

## Description

This application logs an analysis of a news website showing the most viewed news, the most popular authors and the daily error rate when it's significant.

## How to run it

You need to load test cases into your postgresql with the command *psql -d news -f newsdata.sql*

To run the program just type in *python logs.py*

There's a second version of the program that initializes a web server and displays the logs at *<server_addres:8000>*. To run it use *python logs_web.py*

## Design

*logsdb.py* file contains query methods to fetch the information from database.

*logs.py* file only calls these methods and prints them in plain text.

*output.txt* file contains a sample output of the program *logs.py*

## Notes

You can redirect the output to a file using python *logs.py > output.txt*