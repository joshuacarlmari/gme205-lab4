# Algorithm
## i. START
## ii. Load parcel from JSON file
## iii. Convert each record into a Parcel object
## iv. If no parcels are loaded:
### • Display error message
### • Stop program
## v. Initialize total active area to 0.
## vi. For each parcel:
### • If parcel is active:
###     • Add parcel area to total active area.
## vii. SInitialize empty list for parcels above threshold.
## viii. For each parcel:
### • If zone not in dictionary, increment zone count to 0
### • Increment zone count.
## ix. Initialize empty dictionary for zone counts.
## x. Initialize empty list for development-suitable parcels.
## xi. For each parcel:
### • If parcel zone matches selected development zone, add parcel to result list
## xii. Display results
## xiii. Save summary results to output file
## xiv. END
#
#
#
#
# Pseudocode
## BEGIN

## LOAD parcel_data from JSON file

## CONVERT parcel_data into Parcel objects
## STORE in parcel_list

## IF parcel_list is empty THEN
###  PRINT "No parcels found."
###  STOP
## END IF

## SET total_active_area = 0

## FOR each parcel IN parcel_list DO
###  IF parcel is active THEN
###      total_active_area = total_active_area + parcel.area()
###  END IF
## END FOR

## SET threshold = 5000
## CREATE empty list large_parcels

## FOR each parcel IN parcel_list DO
###  IF parcel.area() > threshold THEN
###      ADD parcel to large_parcels
###  END IF
### END FOR

## CREATE empty dictionary zone_counts

## FOR each parcel IN parcel_list DO
###  IF parcel.zone NOT IN zone_counts THEN
###      zone_counts[parcel.zone] = 0
##   END IF

###      zone_counts[parcel.zone] = zone_counts[parcel.zone] + 1
## END FOR

## SET development_zone = "Residential"
## CREATE empty list development_parcels

## FOR each parcel IN parcel_list DO
###  IF parcel.zone == development_zone THEN
###      ADD parcel to development_parcels
###  END IF
### END FOR

## PRINT total_active_area
## PRINT large_parcels
## PRINT zone_counts
## PRINT development_parcels

## SAVE results to summary.json

## END