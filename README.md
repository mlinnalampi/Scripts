# Scripts

Some random scripts which I have written.



##Dyfi

This one is for dy.fi -address registrations. They must be frequently updated and it's quite nasty from command line. This script is for not having to store the password in plaintext anywhere. Update the needed fields, make sure you have a proper curl-dev -package installed and compile this with "gcc dyfi.c -lcurl" and then your dy.fi -address can be updated with just running the program without needing to have the password visible anywhere.