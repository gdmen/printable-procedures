build:
	npm install --prefix static
	static/node_modules/less/bin/lessc styles.less static/css/styles.css

run:
	python3 server.py
