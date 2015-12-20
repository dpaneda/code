read
n=1

while read FILTER; do
  list=`grep "$FILTER" students | sort | awk -F , 'BEGIN { ORS=","} {print $1}' | sed 's/,$//'`

  echo -n "Case #$((n++)): "

  if [[ -z "$list" ]]; then
    echo NONE
  else
    echo $list
  fi
done
