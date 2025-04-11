# ScrapeX

1. Install
  ```
  pip install scrapex
  ```

2. Create a ```json``` file

3. Change below ```77``` and ```99``` to the appropriate values for the latitude and longitude of the location you would like to query and run the command:
  ```
  python scrapex.py --lat 88 --lon 99 --query "foodpoison,stomachbug" 
  ```

  Note: explore with other attributes, e.g.: 
  ```
  python scrapex.py --lat 88 --lon 99 --radius-km 10 --start-date 2025-04-01 --days 7 --query "foodpoison,stomachbug" 
  ```
