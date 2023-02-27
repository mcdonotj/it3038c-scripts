#!/bin/bash


my_atk=$((RANDOM % 20 + 1))
echo "$atk"
 if [ "$my_atk" > 18 ]; then
	echo "$my_atk is greater than 18, you hit the enemy!"
elif [ "$my_atk" = 18 ]; then
	echo "$my_atk is equal to 18, you hit the enemy!"
else
	echo "$my_atk is less than 18, your attack misses..."
fi
