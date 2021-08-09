::pytest -v -s testCases/test_login.py 
pytest -v -s -m "sanity" testCases/ --browser firefox
rem pytest -v -s -m "regression" testCases/ --browser firefox
::pytest -v -s testCases/LoginPage.py --browser firefox

