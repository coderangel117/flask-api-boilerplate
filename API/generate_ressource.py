import os
import sys

TEMPLATE = {
    "model": '''from datetime import datetime
from api.extensions import db

class {class_name}(db.Model):
    __tablename__ = "{table_name}"
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
''',

    "schema": '''from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from api.model.{file_name}_model import {class_name}

class {class_name}Schema(SQLAlchemyAutoSchema):
    class Meta:
        model = {class_name}
        load_instance = True
''',

    "route": '''from flask import Blueprint

{file_name}_bp = Blueprint("{file_name}", __name__)

@{file_name}_bp.route("/{file_name}", methods=["GET"])
def list_{file_name}s():
    return "List of {file_name}s"
''',

    "service": '''# Business logic for {class_name}
def example_service():
    pass
'''
}

def snake_to_pascal(name):
    return ''.join(word.capitalize() for word in name.split('_'))

def generate(name):
    class_name = snake_to_pascal(name)
    table_name = name + "s"

    for key, content in TEMPLATE.items():
        dir_path = f"api/{key}"
        file_path = f"{dir_path}/{name}_{key}.py"
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "w") as f:
            f.write(content.format(file_name=name, class_name=class_name, table_name=table_name))
        print(f"✅ Created: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_resource.py <resource_name>")
    else:
        generate(sys.argv[1])
