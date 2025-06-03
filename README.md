# ```scrape-x```

1. Install
  ```
  pip install curate-x-posts
  ```

2. Create a ```json``` file that contains your login credentials for the X social platform

3. Change below ```88``` and ```99``` to the appropriate values for the latitude and longitude of the location you would like to query and run the command:
 
  ```
  python -m curate-x-posts --lat 88 --lon 99 --radius-km 10 -q "foodpoison,stomachbug" --start-date 2025-04-01 --days 7 -e my_x@gmail.com -u my_x_username -p my_x_password -c my_cookies.json
  ```
  Above will save the cookie data into a file my_cookies.json

  Once created, you could refer to the cookie file and drop the credential data
  ```
  python -m curate-x-posts --lat 88 --lon 99 --radius-km 10 -q "foodpoison,stomachbug" --start-date 2025-04-01 --days 7 -c my_cookies.json
  ```

## ```json``` file

[See example](tests/example_x_login.json)
