from flask import render_template, redirect, request, url_for, current_app
from app import application, db, models
from app.models import FoodSecurityIndex
import os
from sqlalchemy import text
# data processing
import numpy as np 
import pandas as pd


@application.route('/')
@application.route('/home/')
def home():
    prefix_voc = application.wsgi_app.prefix[:-1]


    # Get food_security_and_selfsufficiency_index.csv
    target_path = os.path.join(current_app.root_path, 'static', 'datasets', 'food_security_and_selfsufficiency_index.csv')
    df: pd.DataFrame = pd.read_csv(target_path)
    df.dropna(inplace=True, axis=0, how='any') # Drop rows with NaN values

    # Drop table if exists and reinitialize
    db.session.execute(text("DROP TABLE IF EXISTS fsi"))
    db.session.commit()
    db.create_all()

    # Add records into SQL
    for index, row in df.iterrows():
        record = FoodSecurityIndex()
        record.security_index = row['Security index']
        record.self_sufficiency = row['Self-sufficiency rate']
        record.years = row['Year']
        db.session.add(record)
    db.session.commit()

    all_records = FoodSecurityIndex.query.all()
    print(all_records)

    return render_template('/home.html', title='Home', prefix=prefix_voc, target=df)
