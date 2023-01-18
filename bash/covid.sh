#!/bin/bash
#This script downloads covid data and displays it

POSITIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].negative')
PENDING=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].pending')
DEATHS=$(curl https://api.covidtracking.com/v1/us/current.json | jq '.[0].death')

echo "On $TODAY, there were $POSITIVE positive COVID cases with $DEATHS deaths:"
echo "There are also $NEGATIVE negative cases with $PENDING tests pending results"

