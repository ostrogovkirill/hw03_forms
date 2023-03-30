from datetime import datetime


def year(request):
    """Добавляет переменную с текущим годом."""
    year = datetime.now()
    print(year)
    return {
        'year' : datetime.today().year
    }