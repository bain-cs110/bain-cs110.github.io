'''
What was the average time of someone completing
the boston marathon in 2015?
'''

import utilities

file_path = utilities.get_file_path('marathon_results_2015.csv')
f = open(file_path, 'r', encoding='utf8')


# HINT: To process the times...
#       1. Figure out which element of your "line" list the time is in
#       2. Second, you need to split the time into different components. Luckily
#          each component is separated by a colon. See the hint below on how to split
#       3. Then you'll need to convert each component to seconds! (60 minutes in an hour...
#          60 seconds in a minute, etc.)

# time_components = "50:49:48".split(":")


print('analyze file here...')


f.close()
