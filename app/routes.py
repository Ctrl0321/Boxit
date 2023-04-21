from flask import render_template, url_for, flash, redirect, request
from app import app
import logging
from app.DB import Country, Calculation
from app.Services.Calculate import Calculate

logger = logging.getLogger("app")
FINAL_STANDARD_WEIGHT = 1000
FINAL_PREMIUM_WEIGHT = 10000


@app.route("/health", methods=["GET"])
def health():
    return {'Health': 'Success'}, 200


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calculate', methods=['GET', 'POST'])
def calculate():
    countries = Country.query.all()
    if request.method == "POST":
        try:
            from_country = request.form.get('from_country')
            to_country = request.form.get('to_country')
            from_country_id = Country.query.filter_by(name=from_country).first()
            to_country_id = Country.query.filter_by(name=to_country).first()
            weight = float(request.form.get('Number'))
            express = bool(request.form.get('express'))

            calculate_query = Calculation.query.filter_by(from_country_id=from_country_id.id,
                                                          to_country_id=to_country_id.id).first()
            if calculate_query is not None:
                if express:
                    if weight <= FINAL_STANDARD_WEIGHT:
                        final_calculation = Calculate(kg_weight=calculate_query.express_one_kg, weight=weight, express=True)
                    elif FINAL_STANDARD_WEIGHT <= weight <= FINAL_PREMIUM_WEIGHT:
                        final_calculation = Calculate(kg_weight=calculate_query.express_one_kg, weight=weight,
                                                      additional_per_kg=calculate_query.express_additional_per_kg,
                                                      express=True)
                    else:
                        final_calculation = Calculate(kg_weight=calculate_query.express_above_ten_kg, weight=weight,
                                                      express=True)
                else:
                    if weight <= FINAL_STANDARD_WEIGHT:
                        final_calculation = Calculate(kg_weight=calculate_query.normal_one_kg, weight=weight)
                    elif FINAL_STANDARD_WEIGHT <= weight <= FINAL_PREMIUM_WEIGHT:
                        final_calculation = Calculate(kg_weight=calculate_query.normal_one_kg,
                                                      additional_per_kg=calculate_query.normal_additional_per_kg,
                                                      weight=weight)
                    else:
                        final_calculation = Calculate(kg_weight=calculate_query.normal_above_ten_kg, weight=weight)

                return render_template('calculator.html', final_calculation=str(final_calculation.final_calculation),
                                       countries=countries, ex=True if express else False)
            else:
                logger.debug("Error in country tracking")
                flash('Tracking for these countries is not yet available!', 'error')
                return redirect(url_for('calculate'))
        except Exception as e:
            logger.debug(e)
            flash('An Error has Occurred, Please contact Admin', 'error')
    elif request.method == "GET":
        return render_template('calculator.html', countries=countries)


@app.route('/about-us')
def about_us():
    return render_template('about.html')
