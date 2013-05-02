#!/bin/bash

export POPCLIP_TEXT="1000$"
printf "$POPCLIP_TEXT is:"
python currency.py

export POPCLIP_TEXT="1,000€"
printf "$POPCLIP_TEXT is:"
python currency.py

export POPCLIP_TEXT="1000円"
printf "$POPCLIP_TEXT is:"
python currency.py

export POPCLIP_TEXT="1000£"
printf "$POPCLIP_TEXT is:"
python currency.py

export POPCLIP_TEXT="35,000€"
printf "$POPCLIP_TEXT is:"
python currency.py

export POPCLIP_TEXT="円300,000"
printf "$POPCLIP_TEXT is:"
python currency.py

export POPCLIP_TEXT="299.99£"
printf "$POPCLIP_TEXT is:"
python currency.py