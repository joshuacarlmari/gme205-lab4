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


# Reflection
## 1. Where in your system do Sequence, Selection, and Repetition explicitly appear?

### The system clearly conducted the concepts of Sequence, Selection, and Repetition. Sequence is demonstrated in run_lab4.py, where the program follows an order which is loading the data, creating Parcel objects, performing analysis, displaying results, and saving the output. Selection is implemented using if statements to make decisions, such as verifying that parcels were loaded and filtering parcels based on conditions like active status, area threshold, or zone classification. Repetition appears through for loops used during data loading and within the analysis functions to iterate over all parcels for calculations and filtering.

## 2. If you removed your algorithm planning step, how would your implementation likely change?

### It would make the planning stage not in order and messy. Without a clear outline of the steps beforehand, the code might be developed in an disprganized way, increasing the chances of duplicated logic, poorly placed conditionals, or overly complex nested structures. As a result, the program would be harder to read, maintain, and expand. Overall, eliminating the planning phase would sacrifice the structure and clarity of the system.

## 3. Where does spatial behavior live in your system, and why is that important?
### All spatial behavior is contained within the SpatialObject class in spatial.py. This includes storing the geometry using Shapely and computing the area through the area() method. Keeping spatial logic inside the object is important because it centralizes all geometry-related operations, making them reusable and self-contained. This design prevents analysis functions and the main program from dealing directly with geometry details, reducing code repetition, improving clarity, and making the system easier to maintain and scale.

## 4. Why does analysis.py contain structured logic instead of demo.py?

### To maintain separation of concerns and ensure modular, reusable code. By placing loops, conditionals, and processing functions in analysis.py, all the data analysis is centralized and independent of the program’s execution flow. This keeps run_lab4.py organized, focusing only on sequencing such as loading data, creating objects, calling analysis functions, printing results, and saving outputs. If the structured logic were in the demo file, it would mix computation with program control, making the code harder to read, maintain, and scale.

## 5. What would happen if all filtering logic were placed inside the Parcel class?

### If all filtering logic were put inside the Parcel class, the class would take on too many responsibilities, combining data storage, spatial behavior, and analysis in one place. This would break the separation of concerns and make the class harder to maintain. Each Parcel would need to handle thresholds, zones, and other filtering rules, tightly coupling it to specific analysis. Adding new analysis or changing filtering criteria would require modifying the class itself, increasing the chance of errors.

## 6. If a new rule is added (e.g., “exclude inactive industrial parcels”), how easily can your current design adapt?

### The current design can adapt easily because filtering is handled in analysis.py and Parcel objects provide the needed attributes. To implement a rule like “exclude inactive industrial parcels,” you can add a condition in the analysis function without changing the Parcel class or main program. This keeps the system organized and maintainable, allowing new rules to be added with minimal changes.

## 7. How does separating structured logic from object behavior prevent “God classes”?

### Keeping structured logic separate from object behavior stops a class from doing too much. Parcel and SpatialObject only handle data and geometry, while analysis.py does the calculations and filtering. This makes the code simpler, easier to maintain, and avoids one class becoming too complicated.
