# wingz-exam
# Setup:
```
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
```

## Running server
`python manage.py runserver`


## Setup Postman APIs
1. Using postman, import the `Local.postman_environment.json` environment file and `Wingz.postman_collection.json` API file
2. Replace the `username` and `password` fields with your user account


# Documentation
Once you've setup the postman APIs, you can see all the API endpoints.


# Bonus SQL
```
SELECT 
    strftime('%Y-%m', rar.pickup_time) AS month, 
    rau.first_name || ' ' || substr(rau.last_name, 1, 1) AS Driver, 
    count(*) AS 'Count of Trips > 1'
FROM ride_app_rideevent rre
INNER JOIN ride_app_rideevent rre2 ON rre.id != rre2.id
INNER JOIN ride_app_ride rar ON rre.id_ride_id = rar.id
INNER JOIN ride_app_user rau ON rau.id = rar.id_driver_id
WHERE rre.description = 'Status changed to pickup' AND rre2.description = 'Status changed to dropoff' 
    AND rre.id_ride_id = rre2.id_ride_id AND ((julianday(rre2.created_at) - julianday(rre.created_at)) * 24) > 1
GROUP BY month, Driver
```

