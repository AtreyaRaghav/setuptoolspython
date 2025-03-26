# pip install setuptools

from setuptools import setup, find_packages

setup(
    name="ResumeOcr",  # Replace with the name of your project
    version="0.1.0",  # Initial version of your package
    packages=find_packages(),  # Automatically discover all packages
    include_package_data=True,  # Include other files like static, templates, etc.
    install_requires=[
        "Django==5.1",  # Add any Django version you prefer
        "django-mongodb-backend==5.1.0b1",  # If you're planning to use Gunicorn in production
        # Add any other dependencies your project needs
    ],
    extras_require={
        "dev": [
            "pytest",  # If you want to add testing dependencies
            "flake8",  # If you want to add linter dependencies
        ],
    },
    package_data={
        "app": [
           # "static/*",
            "templates/*",
            "app/migrations/*",
        ],
    },
    entry_points={
        "console_scripts": [
            "manage.py = my_project.manage:main",  # If you need to specify a custom entry point
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.13.1",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",  # Adjust this as needed
    ],
    long_description=open("README.md").read(),  # Include long description from README
    long_description_content_type="text/markdown",  # Ensure it's treated as markdown
    python_requires=">=3.13.1", 
)
