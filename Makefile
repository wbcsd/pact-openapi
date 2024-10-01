OUTDIR := upload

all: build

clean: 
	rm -rf $(OUTDIR)

build:
	mkdir -p $(OUTDIR)
	python3 tools/generate-excel.py pact-openapi-2.2.0.yaml
	python3 tools/generate-excel.py pact-openapi-2.3.0.yaml 
	echo '<html>' > index.html
	echo '<head><style>body { font-family: sans-serif; color: black; margin: 2em; } h1,h2,h3,a { color: rgb(0, 90, 156); } a:not([href]) { color: darkgray; }] </style></head><body>' >> index.html
	echo '<h1>PACT OpenAPI Schema</h1>' >> index.html
	echo '<p>This page contains the OpenAPI schemas and the Simplified Data Model in Excel format for recent and upcoming versions of the PACT Data Model.</p>' >> index.html
	echo '<p>For more information, please visit the <a href="https://carbon-transparency.org/">PACT website</a> and the <a href="https://github.com/wbcsd/pact-openapi">WBCSD GitHub repository</a>.</p>' >> index.html
	echo '<h2>2.0.0</h2>' >> index.html
	echo '<a>PACT OpenAPI 2.0.0</a><br/>' >> index.html
	echo '<a>PACT Simplified Model 2.0.0 (Excel)</a>' >> index.html
	echo '<h2>2.1.0</h2>' >> index.html
	echo '<a>PACT OpenAPI 2.1.0</a><br/>' >> index.html
	echo '<a>PACT Simplified Model 2.1.0 (Excel)</a>' >> index.html
	echo '<h2>2.2.0</h2>' >> index.html
	echo '<a href='pact-openapi-2.2.0.yaml'>PACT OpenAPI 2.2.0</a><br/>' >> index.html
	echo '<a href='pact-simplified-model-2.2.0.xlsx'>PACT Simplified Model 2.2.0 (Excel)</a>' >> index.html
	echo '<h2>2.3.0</h2>' >> index.html
	echo '<a href='pact-openapi-2.3.0.yaml'>PACT OpenAPI 2.3.0</a><br/>' >> index.html
	echo '<a href='pact-simplified-model-2.3.0.xlsx'>PACT Simplified Model 2.3.0 (Excel)</a>' >> index.html
	echo '</body></html>' >> index.html
	cp *.yaml $(OUTDIR)
	mv *.xlsx $(OUTDIR)
	mv index.html $(OUTDIR)
