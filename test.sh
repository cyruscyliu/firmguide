py.test tests --junit-xml log/test.xml --cov-report html:log/cov_html --cov-report xml:log/cov.xml --cov-report annotate:log/cov_annotate --cov=.
./salamander.py -g tests/files/2b38a3.yaml -a arm -wd build/ -p simple
./salamander.py -g tests/files/ec5859.yaml -a arm -wd build/ -p simple
