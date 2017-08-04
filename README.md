# Scripts

Some random scripts which I have written.

##Joulu.py
A little christmas -themed script. It began as a thought about how to define a christmas tree mathematically and this was one idea. Not the shortest one as a program, but I think it's nice as a mathematical formula for a tree. The first for -loop can run n*3 times, 12 happens to be a good example.


##Dyfi

This one is for dy.fi -address registrations. They must be frequently updated and it's quite nasty from command line. This script is for not having to store the password in plaintext anywhere. Update the needed fields, make sure you have a proper curl-dev -package installed and compile this with "gcc dyfi.c -lcurl" and then your dy.fi -address can be updated with just running the program without needing to have the password visible anywhere. Of course the password can be found from the executable, but it takes a bit more to just read the file (to be precise, open the file with vim, type ":% ! xxd" and find url, email and password from hex).