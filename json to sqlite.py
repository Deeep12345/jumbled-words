# -*- coding: utf-8 -*-
"""
Created on Sun May 26 02:53:19 2019

@author: ASUS
"""

import json
import sqlite3


with open ('heart.json','r') as f:
    data = json.loads(f.read())
with sqlite3.connect("some.db") as conn:

    # Create the table if it doesn't exist.
    conn.execute(
        """CREATE TABLE IF NOT EXISTS tab(
                age int,
                sex int,
                cp int,
                trestbps int,
                chol int,
                fbs int,
                restecg int,
                thalach int,
                exang int,
                oldpeak int,
                slope int,
                ca int,
                thal int,
                target int
                
            );"""
        )
    keys=["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal","target"]
    for entry in data:

        # This will make sure that each key will default to None
        # if the key doesn't exist in the json entry.
        values = [entry.get(key, None) for key in keys]

        # Execute the command and replace '?' with the each value
        # in 'values'. DO NOT build a string and replace manually.
        # the sqlite3 library will handle non safe strings by doing this.
        cmd = """INSERT INTO tab VALUES(
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?,
                    ?
                    
                );"""
        conn.execute(cmd, values)

    conn.commit()
