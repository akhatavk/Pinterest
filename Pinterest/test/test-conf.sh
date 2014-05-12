#!/bin/bash
#
# test the domain logic of the web service 
#

# working direct to set the path to our modules (not 
# the most efficient but it works)
export MOO_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}/"/)" && cd .. && pwd )"

echo -e "\n** TEST $MOO_HOME TEST **\n"

# configuration
export PYTHONPATH=${MOO_HOME}/src:${PYTHONPATH}

# run
python ${MOO_HOME}/src/service.py ${MOO_HOME} ${MOO_HOME}/conf/moo.conf
