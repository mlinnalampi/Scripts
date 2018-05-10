#!/bin/bash

# Get pagecount to first column and filename to second and sort based on page count
exiftool -T -PageCount -filename -s3 -ext pdf . |sort -h
