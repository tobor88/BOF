#!/bin/bash
# Not perfect but saves a few time consuming steps when it comes to making a custom python fuzzer

# Get parmaeters to fuzz from end of file
PARAM=$(tail -1 POST.txt | sed -e 's/^/content = /')

# Substitute PV place value with POST parameters
sed -i "s/PV/${PARAM}/" discovercrash.py
sed -i 's/PV/" + inputBuffer + "/' discovercrash.py
printf "Do not forget to add an appersand between parameter values\n"

# Create buffer value from POST
sed -e 's/^/buffer+= /g' POST.txt > bufferPOST.txt

# Append \n\r to the end of each line in POST request
printf "Add \\n\\r to the end of each POST request line\n"
