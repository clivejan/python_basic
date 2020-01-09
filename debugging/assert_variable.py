#!/usr/bin/env python3 -O
# Assertion is used for programmer errors and 
# should not use try except to handle it.

# Status well
job_title = 'DevOps'
assert job_title == "DevOps", "Tansform from SE to DevOps"

# Status wrong
job_title = 'Systems Engineer'
assert job_title == "DevOps", "Tansform from SE to DevOps"

print(job_title)
