#!/bin/bash
#This script downloads covid data and displays it
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA  | jq '.[0].negative')
PENDING=$(echo $DATA  | jq '.[0].pending')
DEATHS=$(echo $DATA | jq '.[0].death')

echo "On $TODAY, there were $POSITIVE positive COVID cases with $DEATHS deaths:"
echo "There are also $NEGATIVE negative cases with $PENDING tests pending results"

