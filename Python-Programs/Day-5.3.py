row1 = ['😊', '😊', '😊']
row2 = ['😊', '😊', '😊']
row3 = ['😊', '😊', '😊']

matrix =[row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position= input("Enter the position where to hide money...")

row_count = int(position[0])
column_count = int(position[1])

row_selected = matrix[row_count-1]
row_selected[column_count-1] = 'X'

print(f"\n{row1}\n{row2}\n{row3}")
