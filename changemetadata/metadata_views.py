import os
import random
import string
from datetime import datetime
from flask import Blueprint, render_template, request, send_file, current_app, redirect, url_for, flash
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime
# Initialize Blueprint
metadata_blueprint = Blueprint('metadata', __name__)

# Allowed extensions
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    """Check if the uploaded file has a valid extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def generate_random_keywords(length=16):
    """Generate a random string of specified length."""
    return ','.join([''.join(random.choices(string.ascii_letters + string.digits, k=length)) for _ in range(2)])


@metadata_blueprint.route('/')
def index():
    """Render the file upload page."""
    return render_template('index.html')

@metadata_blueprint.route('/upload', methods=['POST'])
def upload_file():
    """Handle file upload, metadata addition, and return processed file."""
    if 'file' not in request.files:
        flash("No file uploaded.", "error")
        return redirect(url_for('metadata.index'))

    file = request.files['file']

    if file and allowed_file(file.filename):
        filename = file.filename
        temp_folder = "/tmp"  # Temporary storage for cloud deployment

        input_path = os.path.join(temp_folder, filename)
        output_path = os.path.join(temp_folder, f"processed_{filename}")

        # Save the uploaded file temporarily
        file.save(input_path)

        from datetime import datetime

        # Define the expected date format
        DATE_FORMAT = "%Y-%m-%d %I:%M:%S %p"

        # Retrieve 'creation_date' and ensure consistent formatting
        creation_date = request.form.get('creation_date')

        if creation_date:
            try:
                # Convert existing date to a consistent format
                creation_date = datetime.strptime(creation_date, DATE_FORMAT).strftime(DATE_FORMAT)
            except ValueError:
                print("Invalid date format received, using default timestamp.")
                creation_date = datetime.now().strftime(DATE_FORMAT)
        else:
            # Use default formatted timestamp
            creation_date = datetime.now().strftime(DATE_FORMAT)

        print("creation date>>>>>", creation_date)


        # Extract metadata from form
        metadata = {
            '/Title': request.form.get('title', f"Updated_{filename}"),
            '/Author': request.form.get('author', 'Unknown'),
            '/Creator': request.form.get('creator', 'Flask App'),
            '/Keywords': request.form.get('keywords', generate_random_keywords()),
            '/Producer': request.form.get('producer', 'Custom PDF Processor'),
            '/CreationDate': creation_date  # Use the provided or default 'CreationDate'
        }

        try:
            # Read the PDF
            reader = PdfReader(input_path)
            writer = PdfWriter()

            for page in reader.pages:
                writer.add_page(page)

            # Apply metadata
            writer.add_metadata(metadata)

            # Write updated PDF
            with open(output_path, "wb") as output_file:
                writer.write(output_file)

            # Delete original file to save space
            os.remove(input_path)

            # Serve the processed file and delete after sending
            return send_file(output_path, as_attachment=True, download_name=f"updated_{filename}")

        except Exception as e:
            flash(f"Error processing file: {e}", "error")
            return redirect(url_for('metadata.index'))

        finally:
            # Ensure processed file is deleted after sending
            if os.path.exists(output_path):
                os.remove(output_path)

    flash("Invalid file format. Please upload a PDF.", "error")
    return redirect(url_for('metadata.index'))