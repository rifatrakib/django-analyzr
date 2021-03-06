from django.contrib.auth.models import User

from io import BytesIO

import matplotlib.pyplot as plt
import seaborn as sns
import base64


def get_image():
    # create a bytes buffer for image to save
    buffer = BytesIO()
    # create the plot with the use of BytesIO object as its 'file'
    plt.savefig(buffer, format='png')
    # set the cursor to the beginning of the stream
    buffer.seek(0)
    # retriecve the entire content of the file
    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')

    # free memory of the buffer
    buffer.close()
    return graph


def get_simple_plot(chart_type, *ars, **kwargs):
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 5))
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')
    if chart_type == 'bar plot':
        title = 'total price by day (bar)'
        plt.title(title)
        plt.bar(x, y)
    elif chart_type == 'line plot':
        title = 'total price by day (line)'
        plt.title(title)
        plt.plot(x, y)
    else:
        title = 'sales per day'
        plt.title(title)
        sns.countplot('name', data=data)
    plt.xticks(rotation=45)
    plt.tight_layout()

    graph = get_image()
    return graph


def get_salesman_from_id(value):
    salesman = User.objects.get(id=value)
    return salesman
