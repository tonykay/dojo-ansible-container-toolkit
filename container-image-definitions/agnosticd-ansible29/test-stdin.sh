#!/usr/bin/env bash



#[ test -s /dev/stdin ] && echo 'pipe has data' || echo 'pipe is empty' 

#if read -t 0
#then
#  cat - > /tmp/vars.yml
#fi

#cat - > /tmp/vars.yml

#if [ -f /tmp/vars.yml ] 
#fail (waits) cat - > /tmp/vars.yml
# [ -t 1 ] && cat - > /tmp/vars.yml || echo empty
# [ test -s /dev/stdin ] && echo 'pipe has data' || echo 'pipe is empty' 
if [[ -p /dev/stdin ]]
then
  cat - > /tmp/foo.yml
fi

date
#cd ~devops/agnosticd


# exec "$@"
