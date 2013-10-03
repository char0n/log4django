bootstrap:
	pip install -e . --use-mirrors
	pip install "file://`pwd`#egg=log4django" --use-mirrors
	pip install "file://`pwd`#egg=log4django[tests]" --use-mirrors
	pip install "file://`pwd`#egg=log4django[gearman]" --use-mirrors

test: bootstrap
	@echo "Running Python tests"
	python manage.py test log4django
	@echo ""

clean:
	rm -rf ./dist
	rm -rf ./log4django.egg-info