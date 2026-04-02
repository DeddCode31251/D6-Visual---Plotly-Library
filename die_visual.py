from plotly.graph_objs import Bar,Layout
from plotly import offline

from random import choice,randint

from die import Die

#Create a D6.
die = Die()

#Make some rolls, and store results in a list.
results = []
#Times
times = 0
for roll_num in range(1000):
    times += 1
    result = die.roll()
    results.append(result)


#Analyze the results.
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

#Random File name
letters = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
random_letters = choice(letters) * 5
random_number = randint(1, 1001023050)
file_name = f'{random_letters}-{random_number}'
#Visualize the results.
x_values = list(range(1,die.num_sides+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':"Result"}
y_axis_config = {"title":"Frequency Result"}
my_layout = Layout(title=f"Results of rolling one D6 {times} times",
                   xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename=f'html/d6{file_name}.html')
