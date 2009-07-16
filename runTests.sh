#!/bin/bash
nosetests -v -d --with-xunit --processes 2 --process-timeout 5 --with-coverage --cover-package server --cover-erase --cover-html
