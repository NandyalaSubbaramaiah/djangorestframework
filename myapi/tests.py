from django.test import TestCase
import matplotlib.pyplot as plt

# Hypothetical data for different Django frameworks
frameworks = ['Django REST framework', 'Django Channels', 'Django Oscar', 'Django CMS', 'Django Haystack']
usage_percentage = [50, 20, 10, 10, 10]  # Hypothetical usage percentages

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(usage_percentage, labels=frameworks, autopct='%1.1f%%', startangle=140)
plt.title('Usage of Different Django Frameworks')
plt.axis('equal')  # Equal aspect ratio ensures the pie is drawn as a circle.

# Show the pie chart
plt.show()
# Create your tests here.
