# A small script to list and download all pdf submissions from Hacker news

Build with:
`docker build -t hackernews .``


Run with

`docker run -it --mount type=bind,source="$(pwd)",target=/docker hackernews`

To eventually download the files to current directory
