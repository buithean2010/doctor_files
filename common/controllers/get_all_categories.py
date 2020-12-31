from ..models import MainCategories, SubCategories1


def get_all_categories():
    categories = {}
    for item in SubCategories1.objects.all():
        if item.main_cat.name_vn not in categories:
            categories[item.main_cat.name_vn] = [item]
        else:
            categories[item.main_cat.name_vn].append(item)

    return categories
