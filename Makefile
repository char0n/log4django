bootstrap:
	pip install -e .
	pip install "file://`pwd`#egg=log4django"
	pip install "file://`pwd`#egg=log4django[tests]"
	pip install "file://`pwd`#egg=log4django[gearman]"
	./scripts/setup.sh
	python manage.py syncdb --noinput --migrate


test: bootstrap
	@echo "Running Python tests"
	python manage.py test log4django
	@echo ""

clean:
	rm -rf ./dist
	rm -rf ./log4django.egg-info
	rm -rf test.db
	rm -rf settings.py
