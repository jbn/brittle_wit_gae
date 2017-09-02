install_requirements:
	pip install -t lib -r requirements.txt

devel:
	dev_appserver.py app.yaml
