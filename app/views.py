from flask import Blueprint, render_template, request, redirect, url_for, session, flash, send_from_directory, jsonify
from . import db
from .models import Exercise,Category,Video, Appointment, ProductDetails
views = Blueprint('views', __name__)

# Home page
@views.route('/')
def index():
    exercises = Exercise.query.limit(3).all()
    categories = Category.query.limit(3).all()
    videos = Video.query.limit(3).all()
    return render_template('index.html', exercises=exercises, categories=categories, videos=videos)

# Doctor consultation page
@views.route('/doctor_consultation', methods=['GET', 'POST'])
def doctor_consultation():
    if request.method == 'POST':
        location = request.form.get('location')
        date = request.form.get('date')
        specialty = request.form.get('specialty')

        if not all([location, date, specialty]):
            return jsonify({'success': False, 'message': 'Please fill in all required fields.'}), 400

        appointment = Appointment(location=location, date=date, specialty=specialty)
        db.session.add(appointment)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': f'Appointment with {specialty} on {date} in {location} booked successfully!'
        })

    return render_template('doctor_consultation.html')

# Exercises page
@views.route('/exercises')
def exercises():
    exercises = Exercise.query.all()
    return render_template('exercises.html', exercises=exercises)

# Introduction page
@views.route('/introduction')
def introduction():
    return render_template('index.html')

# Maternal approaches page
@views.route('/maternal_approaches')
def maternal_approaches():
    return render_template('maternal_approaches.html')

# Products page
@views.route('/products')
def products():
    categories = Category.query.all()
    return render_template('products.html', categories=categories)

# Videos page
@views.route('/dietplan')
def dietplan():
    return render_template('dietplan.html')


# @views.route('/product-details')
# def product_details():
#     pd = ProductDetails(
#         name="Diapering & Potty Training Guide:Step by step instructions for proper diapering & potty training.",
#         description="1. Preparation:Gather all supplies (clean diaper, wipes, cream) before starting. Wash your hands thoroughly.;2. Position Baby:Lay baby on a flat, safe surface. Keep one hand on baby at all times for safety.;3. Remove Dirty Diaper:Unfasten the diaper tabs and fold the dirty diaper inward. Clean the area thoroughly with wipes.;4. Apply Cream:If needed, apply diaper rash cream to prevent irritation.;5. Put on New Diaper:Slide a clean diaper under baby, fasten securely but not too tight. Ensure it fits snugly around the legs.;6. Dispose of Dirty Diaper:Seal the dirty diaper in a plastic bag and dispose of it properly.;7. Clean Up:Wash your hands thoroughly after changing the diaper. Dispose of wipes and any other materials used.;8. Potty Training (if applicable):Encourage baby to sit on the potty regularly, especially after meals or naps. Use positive reinforcement for successful attempts."
#     )
#     db.session.add(pd)
#     db.session.commit()

#     pd = ProductDetails.query.first()
#     if pd:
#         pd_id = pd.id
#         pd_name = pd.name
#         pd_description = pd.description
#         main = pd_name.split(':')
#         points = pd_description.split(";")
#         para = [point.split(":") for point in points]
#         print(f"main[0] : {main[0]}")
#         print(f"main[1] : {main[1]}")
#         for i in range(len(para)):
#             print(i)
#             print(para[i][0])
#             print(para[i][1])
        

#     return render_template('product-details.html')

@views.route('/product-details/<int:product_id>')
def product_details(product_id):
    pd = ProductDetails.query.get_or_404(product_id)
    if pd:
        pd_id = pd.id
        pd_name = pd.name
        pd_description = pd.description
        main = pd_name.split(':')
        points = pd_description.split(";")
        para = [point.split(":") for point in points]
        # print(f"main[0] : {main[0]}")
        # print(f"main[1] : {main[1]}")
        # for i in range(len(para)):
        #     print(i)
        #     print(para[i][0])
        #     print(para[i][1])
    return render_template('product-details.html', length = len(para),main=main, para = para)
# 404 page
@views.route('/not_found')
def not_found():
    return render_template('not_found.html'), 404