#!/bin/bash

grep -cri "mediguest" . | fgrep -v :0 | fgrep -v .git
