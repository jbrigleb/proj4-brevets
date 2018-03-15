# Project 4:  Brevet time calculator with Ajax

Reimplementation the RUSA ACP controle time calculator with flask and ajax.

Credits to Michal Young for original project and code

## Repo Author

Jack Brigleb 

jbrigleb@uoregon.edu

## ACP controle times

Open and close times for controle points are calculated based on the distance of the controle
and the minimum and maximum speeds in each brevet distance. Calculations are implemented using tables.

The algorithm for calculating controle times is described at
https://rusa.org/octime_alg.html .  Additional background information
is in https://rusa.org/pages/rulesForRiders . 

Expected speeds are as follows

For controle locations in the 0-200km range,     the minimum speed is 15km and the maximum speed is 34km.

For controle locations in the 200-400km range,   the minimum speed is 15km and the maximum speed is 32km.

For controle locations in the 400-600km range,   the minimum speed is 15km and the maximum speed is 30km.

For controle locations in the 600-1000km range,  the minimum speed is 11.428km and the maximum speed is 28km.

For controle locations in the 1000-1300km range, the minimum speed is 13.333km and the maximum speed is 26km.


Opening time is calculated based on max speed, closing time is based on minimum speed.

You iterate through the above listed distance categories, and divide the distance by the speed to get at time difference.

Consider a 350km controle.

the calculation for opening time would look like 200km/34kph = 5.882 = 5 hours and .882*60 = 53 minutes*
                                                 150km/32kph = 4.687 = 4 hours and .687*60 = 41 minutes*
                                                 5+4 = 9 Hours and 53 + 41 = 94 minutes
                                                 So the opening time would be 10 Hours and 34 minutes from the start time.
*minutes are rounded to nearest minute.



controle distances which are further than the overall brevet distance, but no greater than 1.2 times further than the brevet distance are allowed, 
but have opening and closing times as if the controle distance was exactly the brevet distance.

For example, in 200km brevet, a 240km controle is allowed, but will have the same opening and close times as a 200km controle.
A 250km controle, however, would be disallowed.



There are addition rules which can be found in the above link.


We are essentially replacing the calculator at
https://rusa.org/octime_acp.html .


## Testing

A nose test suite is included.

Tests are included for:

A 0km controle case.

A negative distance input controle case.

A distance category border case.

A case where a controle is further than the brevet distance, but within 1.2 times the brevet distance.

A case where the controle is out of bounds; over 1.2 times the brevet distance.


