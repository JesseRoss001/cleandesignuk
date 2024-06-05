from django.shortcuts import render

def index(request):
    # Add your logic here, e.g., fetching products or data to display in the store
    return render(request, 'developer_store/index.html', {})




def templates_list(request):
    # Logic to fetch and display templates
    return render(request, 'developer_store/templates_list.html', {
        'templates': []  # Assume you might have some data to pass
    })


def components_list(request):
    # Logic to fetch and display templates
    return render(request, 'developer_store/components_list.html', {
        'components_list': []  # Assume you might have some data to pass
    })

