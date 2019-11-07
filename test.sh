python3.7 -m unittest tests.test_generation.TestGeneration.test_nas7820
python3.7 -m unittest tests.test_generation.TestGeneration.test_wrt320n_n1
python3.7 -m unittest tests.test_generation.TestGeneration.test_wrt350n_v2
python3.7 main.py -dbt firmadyne -p dt -u 13882 -r -wd ./build
python3.7 main.py -dbt firmadyne -p dt -u 14292 -r -wd ./build
python3.7 main.py -dbt firmadyne -p dt -u 15007 -r -wd ./build
python3.7 main.py -dbt firmadyne -p dt -f all -wd ./build
python3.7 -m unittest tests.supervisor_test.SupervisorTest.test_trace_collection
