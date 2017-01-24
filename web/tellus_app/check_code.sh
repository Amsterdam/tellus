# flake code check including mccabe
# flake8 --config=./flake.conf .

# Show pylint code review
pylint --rcfile=.pylintrc --load-plugins pylint_django ../tellus_app
