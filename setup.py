import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-highlightselect-model-admin",
    version="1.0.0",
    author="Laonan",
    author_email="hello@laonan.net",
    description="A Django App that highlights selected rows on the admin UI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laonan/django-highlightselect-model-admin",  # github url
    project_urls={
        "Bug Tracker": "https://github.com/laonan/django-highlightselect-model-admin/issues",
    },
    include_package_data=True,
    package_data={
        "highlightselect_model_admin": ["static/highlightselect_model_admin/js/*.js"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
            'Django>=2.0.13',
    ],
    zip_safe=True,
    python_requires=">=3.6",
)
