# Scripts

Some random scripts and small code snippets which I have written.

##LFSR Stream Cipher

We were introduced to Stream Ciphers in "Cryptography and Data security" -course in Aalto and I decided to implement a simple Stream cipher as part of learning. The method takes initial values in n, and puts size bits of data into res. It uses xoring previous 5th and 3rd value of n to create new values.


## SumOfTwo

This is a small snippet of python which I wrote to compare if using hashtables (=dicts in python) to find two list items which sum to target number is significantly faster than the naive way. Seems that the naive way may be even faster at some points than the dict, but it may also be orders of magnitude worse. This is quite the assumed result. This is also my first time timing function call times in python, but that's pretty simple.


## Joulu.py
A little christmas -themed script. It began as a thought about how to define a christmas tree mathematically and this was one idea. Not the shortest one as a program, but I think it's nice as a mathematical formula for a tree. The first for -loop can run n\*3 times, 12 happens to be a good example.


## Dyfi

This one is for dy.fi -address registrations. They must be frequently updated and it's quite nasty from command line. This script is for not having to store the password in plaintext anywhere. Update the needed fields, make sure you have a proper curl-dev -package installed and compile this with "gcc dyfi.c -lcurl" and then your dy.fi -address can be updated with just running the program without needing to have the password visible anywhere. Of course the password can be found from the executable, but it takes a bit more to just read the file (to be precise, open the file with vim, type ":% ! xxd" and find url, email and password from hex).