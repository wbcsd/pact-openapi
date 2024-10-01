OUTDIR := upload

all: build

clean: 
	rm -rf $(OUTDIR)

build:
	mkdir -p $(OUTDIR)
	python3 tools/generate-excel.py pact-openapi-2.2.0.yaml
	python3 tools/generate-excel.py pact-openapi-2.3.0.yaml 
	echo '<html><body>' > index.html
	echo '<a href='pact-openapi-2.2.0.yaml'>PACT OpenAPI 2.2.0</a>' >> index.html
	echo '<a href='pact-simplified-model-2.2.0.xlsx'>PACT Simplified Model 2.2.0</a>' >> index.html
	echo '<a href='pact-openapi-2.3.0.yaml'>PACT OpenAPI 2.3.0</a>' >> index.html
	echo '<a href='pact-simplified-model-2.3.0.xlsx'>PACT Simplified Model 2.3.0</a>' >> index.html
	echo '</body></html>' >> index.html
	cp *.yaml $(OUTDIR)
	mv *.xlsx $(OUTDIR)
	mv index.html $(OUTDIR)
