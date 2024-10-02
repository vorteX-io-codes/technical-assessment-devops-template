FROM public.ecr.aws/lambda/python:3.12

# Write Docker commands to package your Python application with its dependencies
# TIPS: a python 'requirements.txt' file to insall the Python dependencies with pip
# can be generated using 'poetry export --without-hashes > lambda_app/requirements.txt'
# before building the image with 'docker build ...'
RUN ...

CMD ["app.lambda_handler"]
