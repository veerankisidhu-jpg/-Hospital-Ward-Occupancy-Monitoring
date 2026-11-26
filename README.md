# -Hospital-Ward-Occupancy-Monitoring
Name:V.Siva Sambhavi
Roll number:N26V01A0389  
section:05 
# Hospital Ward Occupancy Monitoring

## Project Description

The Hospital Ward Occupancy Monitoring System is a Python-based program designed to analyse hospital bed occupancy across different wards over a period of days.

The program uses a nested list to store daily occupied bed counts for each ward. It calculates bed utilization percentages, identifies capacity violations, and determines peak-demand periods.

This project helps understand hospital resource utilization and supports basic bed management analysis.

## Objectives

- Store ward-wise bed occupancy using nested lists.
- Calculate total occupied beds for each ward.
- Determine average daily occupancy.
- Calculate bed utilization percentages.
- Detect capacity violations.
- Identify peak-demand days for each ward.
- Calculate overall hospital occupancy statistics.
- Identify the day with the highest hospital demand.

## Concepts Used

- Variables and data types
- Lists and nested lists
- List indexing
- List operations
- Arithmetic operators
- Conditional statements
- For loops
- Built-in functions such as `len()`, `sum()`, `max()`, and `round()`

## Input

The program uses sample data for four hospital wards:

1. General Ward
2. ICU
3. Emergency Ward
4. Maternity Ward

Each ward contains seven daily occupancy values representing Monday to Sunday.

The bed capacities are:

| Ward | Capacity |
|---|---:|
| General Ward | 30 |
| ICU | 15 |
| Emergency Ward | 35 |
| Maternity Ward | 25 |

## Algorithm

1. Start the program.
2. Initialize ward occupancy data using a nested list.
3. Initialize ward capacities and ward names.
4. Set the number of wards and days.
5. For each ward:
   - Calculate total occupied beds.
   - Calculate daily utilization percentages.
   - Check whether occupancy exceeds capacity.
   - Identify the peak occupancy and peak-demand day.
   - Calculate average occupancy and average utilization.
6. Calculate overall hospital occupancy.
7. Identify the day with maximum hospital demand.
8. Display the results.
9. Stop the program.

## Formula

### Daily Utilization

Daily utilization is calculated as:

Utilization (%) = (Occupied Beds / Ward Capacity) × 100

### Average Daily Occupancy

Average daily occupancy is calculated as:

Average Occupancy = Total Occupied Bed-Days / Number of Days

### Average Ward Utilization

Average ward utilization is calculated as:

Average Utilization (%) = (Average Occupancy / Ward Capacity) × 100

### Overall Hospital Utilization

Overall utilization is calculated as:

Overall Utilization (%) = (Total Occupied Bed-Days / Total Available Bed-Days) × 100

## Capacity Violation

A capacity violation occurs when:

Occupied Beds > Ward Capacity

The program displays a warning and calculates the number of excess beds.

## Peak Demand

Peak demand is the maximum number of occupied beds recorded during the observation period.

The program identifies:

- Peak-demand day for each ward.
- Peak-demand day for the entire hospital.

## How to Run

1. Install Python 3.
2. Save the program as `hospital_occupancy.py`.
3. Open a terminal or command prompt.
4. Navigate to the folder containing the program.
5. Execute the following command:

```bash
python hospital_occupancy.py
```

## Expected Output

The program displays:

- Daily occupancy for each ward.
- Daily utilization percentages.
- Capacity violation warnings.
- Total occupied bed-days.
- Average daily occupancy.
- Average utilization.
- Peak occupancy and peak-demand day.
- Overall hospital utilization.
- Daily hospital occupancy summary.

## Conclusion

The Hospital Ward Occupancy Monitoring System demonstrates how Python nested lists can be used to analyse hospital bed occupancy.

It calculates utilization percentages, detects capacity violations, and identifies peak-demand periods. The project provides a simple example of using computational thinking and basic programming concepts to solve a real-world hospital management problem.

## Future Enhancements

- Accept occupancy data from the user.
- Read occupancy records from a file.
- Display graphical occupancy charts.
- Generate automatic alerts for high utilization.
- Analyse occupancy over longer periods.
- Store historical occupancy records.
