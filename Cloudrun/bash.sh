#!/usr/bin/env bash

#
# using '${!var_name}'
#
VARIN = VALUE_IN1
VAROUT = VALUE_OUT1

VAR_IN = VALUE_IN2
VAR_OUT = VALUE_OUT2

foo()
{
    local
base_name =$1;
shift;
local
suffix =$1;
shift;

local
var_name = "${base_name}_${suffix}"

echo
"${!var_name}"
}

bar()
{
    local
base_name =$1;
shift;

local
inv =$(foo ${base_name} IN)
local
outv =$(foo ${base_name} OUT)

echo
"${inv}:${outv}"
}

# question: what's result in console?
# echo "$(bar VAR)"
