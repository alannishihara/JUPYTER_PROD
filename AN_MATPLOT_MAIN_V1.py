# AN_MATPLOT_MAIN_V1.py

import random
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

counter = 0
counter2 = 0
counter3 = 0
counter4 = 0
counter5 = 0
counter6 = 0
counter7 = 0
counter8 = 0
counter9 = 0
counter10 = 0
counter11 = 0
counter12 = 0

counter_init = input("\nEnter number of dice rolls: ")
                     
while counter < int(counter_init):
	x = (random.randint(1, 6))
	y = (random.randint(1, 6))
	z = x + y
	counter = counter + 1
	print('Total for throw number', counter, '=', z)
	if z == 2:
		counter2 = counter2 + 1
	elif z == 3:
		counter3 = counter3 + 1
	elif z == 4:
		counter4 = counter4 + 1
	elif z == 5:
		counter5 = counter5 + 1
	elif z == 6:
		counter6 = counter6 + 1
	elif z == 7:
		counter7 = counter7 + 1
	elif z == 8:
		counter8 = counter8 + 1
	elif z == 9:
		counter9 = counter9 + 1
	elif z == 10:
		counter10 = counter10 + 1
	elif z == 11:
		counter11 = counter11 + 1
	elif z == 12:
		counter12 = counter12 + 1

result2 = (counter2/counter)
result3 = (counter3/counter)
result4 = (counter4/counter)
result5 = (counter5/counter)
result6 = (counter6/counter)
result7 = (counter7/counter)
result8 = (counter8/counter)
result9 = (counter9/counter)
result10 = (counter10/counter)
result11 = (counter11/counter)
result12 = (counter12/counter)

print('\nNO. OF 2s THROWN =', counter2, '(',f'{result2:.2%}',')')
print('NO. OF 3s THROWN =', counter3, '(',f'{result3:.2%}',')')
print('NO. OF 4s THROWN =', counter4, '(',f'{result4:.2%}',')')
print('NO. OF 5s THROWN =', counter5, '(',f'{result5:.2%}',')')
print('NO. OF 6s THROWN =', counter6, '(',f'{result6:.2%}',')')
print('NO. OF 7s THROWN =', counter7, '(',f'{result7:.2%}',')')
print('NO. OF 8s THROWN =', counter8, '(',f'{result8:.2%}',')')
print('NO. OF 9s THROWN =', counter9, '(',f'{result9:.2%}',')')
print('NO. OF 10s THROWN =', counter10, '(',f'{result10:.2%}',')')
print('NO. OF 11s THROWN =', counter11, '(',f'{result11:.2%}',')')
print('NO. OF 12s THROWN =', counter12, '(',f'{result12:.2%}',')\n')

x = [2,3,4,5,6,7,8,9,10,11,12]
y = [counter2,counter3,counter4,counter5,counter6,counter7,counter8,counter9,counter10,counter11,counter12]

plt.title('DICE ROLL SIMULATION\n' + 'Number of Rolls: ' + str(counter_init), fontweight='bold', fontsize=12, color='black')
plt.xlabel('Sum of Dice Roll', fontstyle='italic', fontweight='bold', fontsize=10, color='black')
plt.ylabel('Frequency of Dice Roll', fontstyle='italic', fontweight='bold', fontsize=10, color='black')
plt.grid(axis='y', color='gray', linewidth=0.75, alpha=0.25)

p = plt.bar(x, y, color = 'darkblue')
plt.bar_label(p, label_type='edge', color='red', fontweight='bold', fontsize=8)
plt.xticks(x,x)
fmt = '%.0f%%'
yticks = mtick.PercentFormatter(xmax=int(counter_init), decimals=0, symbol='%')
plt.gca().yaxis.set_major_formatter(yticks)

plt.show()