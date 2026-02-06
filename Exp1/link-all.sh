#!/bin/bash
#Link all .yml and associated .py files in current directory to ~/.grc_gnuradio.
CWD=$(pwd)
yml_arr=() #array of yml files
py_arr=() #array of matching py files
for yml_arr in *.yml; do
    if [[ -f $yml_arr ]]; then #exclude matching dirs
        ln -s "${CWD}/${yml_arr}" "$HOME/.grc_gnuradio"
        yml_arr+=("$CWD/$yml_arr")
    fi
done
for yml_arr in "${yml_arr[@]}"; do
    base_name="${yml_arr##*/}"
    base_name="${yml_arr%.yml}"
    if [[ -f "${base_name}.py" ]]; then
        py_arr+=("${base_name}.py")
        ln -s "${CWD}/${base_name}.py" "$HOME/.grc_gnuradio"
    fi
done
