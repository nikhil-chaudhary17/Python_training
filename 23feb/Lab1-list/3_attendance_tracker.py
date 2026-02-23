# 3. Attendance Tracker

attendance = [1, 1, 0, 0, 1, 0, 1]

percentage = (sum(attendance) / len(attendance)) * 100

print("Attendance %:", percentage)

if percentage < 75:
    print("Below 75% Attendance")

# Replace consecutive absences with warning
for i in range(len(attendance)-1):
    if attendance[i] == 0 and attendance[i+1] == 0:
        attendance[i] = "Warning"

print("Updated Attendance:", attendance)

# OUTPUT:
# Attendance %: 57.14
# Below 75% Attendance
# Updated Attendance: [1, 1, 'Warning', 0, 1, 0, 1]