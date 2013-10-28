bootstrap:
	pip install -e . --use-mirrors
	pip install "file://`pwd`#egg=log4django" --use-mirrors
	pip install "file://`pwd`#egg=log4django[tests]" --use-mirrors
	pip install "file://`pwd`#egg=log4django[gearman]" --use-mirrors
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