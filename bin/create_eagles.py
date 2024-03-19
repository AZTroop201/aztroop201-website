#!/bin/env python3
import pandas as pd
from jinja2 import Template
from datetime import datetime
import re

df = pd.read_csv('input.csv')

with open('temp.md','r') as _file:
    template = Template(_file.read())

for index, row in df.iterrows():
    name = row['Name']
    date = row['Date']
    mydate = datetime.strptime(date, "%m/%d/%Y")
    mydate_str = mydate.isoformat() + "-07:00"

    filename = name.lower().replace(" ", "-").replace("\"", "").replace("'", "").replace(".", "") + ".md"
    print(f"Filename:{filename} Name:{name} Date:{mydate_str}")

    with open('tmp/' + filename, 'w') as _output:
        _output.write(template.render({'name': name, 'date': mydate_str}))
