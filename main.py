
# Hospital Ward Occupancy Monitoring
# Analyse bed occupancy across hospital wards and days.

# Nested list: Each inner list contains daily occupied beds
# for one ward.
occupancy = [
    [18, 20, 22, 25, 24, 21, 19],  # General Ward
    [10, 12, 15, 14, 16, 18, 13],  # ICU
    [25, 28, 30, 32, 35, 31, 29],  # Emergency Ward
    [15, 17, 19, 20, 18, 16, 14]   # Maternity Ward
]

# Bed capacity of each ward
capacities = [30, 15, 35, 25]

# Ward names
ward_names = [
    "General Ward",
    "ICU",
    "Emergency Ward",
    "Maternity Ward"
]

days = [
    "Monday", "Tuesday", "Wednesday",
    "Thursday", "Friday", "Saturday", "Sunday"
]

# Number of wards and days
ward_count = len(occupancy)
day_count = len(days)

# Variables for overall hospital statistics
total_hospital_beds = sum(capacities)
total_occupied_beds = 0
total_capacity = 0

# Store daily hospital occupancy
daily_hospital_occupancy = [0] * day_count

print("=" * 65)
print("       HOSPITAL WARD OCCUPANCY MONITORING SYSTEM")
print("=" * 65)

# Analyse each ward
for i in range(ward_count):

    ward_total = 0
    ward_peak = 0
    peak_day = ""

    print("\nWard:", ward_names[i])
    print("Capacity:", capacities[i], "beds")

    # Calculate occupancy for each day
    for j in range(day_count):

        occupied = occupancy[i][j]
        capacity = capacities[i]

        ward_total += occupied
        daily_hospital_occupancy[j] += occupied

        # Calculate daily utilization
        utilization = (occupied / capacity) * 100

        print(
            days[j],
            "- Occupied:", occupied,
            "| Utilization:", round(utilization, 2), "%"
        )

        # Check capacity violation
        if occupied > capacity:
            excess = occupied - capacity

            print(
                "  WARNING: Capacity exceeded by",
                excess, "beds!"
            )

        # Identify peak demand for this ward
        if occupied > ward_peak:
            ward_peak = occupied
            peak_day = days[j]

    # Calculate average occupancy and utilization
    average_occupancy = ward_total / day_count

    average_utilization = (
        average_occupancy / capacities[i]
    ) * 100

    total_occupied_beds += ward_total
    total_capacity += capacities[i] * day_count

    print("\nWard Summary:")
    print("Total occupied bed-days:", ward_total)
    print("Average daily occupancy:", round(average_occupancy, 2))
    print("Average utilization:", round(average_utilization, 2), "%")
    print("Peak occupancy:", ward_peak, "beds")
    print("Peak demand day:", peak_day)

# Overall hospital utilization
overall_utilization = (
    total_occupied_beds / total_capacity
) * 100

print("\n" + "=" * 65)
print("             OVERALL HOSPITAL SUMMARY")
print("=" * 65)

print("Total hospital bed capacity:", total_hospital_beds)
print("Total occupied bed-days:", total_occupied_beds)

print(
    "Average daily occupied beds:",
    round(total_occupied_beds / day_count, 2)
)

print(
    "Overall bed utilization:",
    round(overall_utilization, 2), "%"
)

# Find the day with maximum hospital demand
peak_hospital_occupancy = max(daily_hospital_occupancy)

peak_hospital_day = daily_hospital_occupancy.index(
    peak_hospital_occupancy
)

print(
    "Peak hospital demand:",
    peak_hospital_occupancy, "beds"
)

print(
    "Peak hospital demand day:",
    days[peak_hospital_day]
)

# Display daily hospital occupancy
print("\nDaily Hospital Occupancy:")

for i in range(day_count):

    daily_utilization = (
        daily_hospital_occupancy[i] / total_hospital_beds
    ) * 100

    print(
        days[i],
        ":",
        daily_hospital_occupancy[i],
        "beds occupied |",
        round(daily_utilization, 2), "%"
    )

print("\nMonitoring completed successfully.")
