import os

class Config:
    SECRET_KEY = os.urandom(24)  # Secret key for security
    TEMP_FOLDER = "/tmp"  # Use temporary storage in cloud environments
    ALLOWED_EXTENSIONS = {'pdf'}  # Allowed file types