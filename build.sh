#!/bin/bash
vulnerable_deps=$(safety check --bare -r requirements.txt)
if [[ $? != 0 ]]; then
  echo "Vulnerabilities found in packages:" $vulnerable_deps
fi
