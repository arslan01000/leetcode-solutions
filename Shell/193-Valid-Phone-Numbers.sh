#!/bin/bash
grep -E '^(\([0-9]{3}\) [0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$' file.txt


# This script filters valid phone numbers from file.txt
# Valid formats: (xxx) xxx-xxxx or xxx-xxx-xxxx
