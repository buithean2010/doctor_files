from ..models import PartSymptoms, SubCategories2


def get_parts_symptoms_by_subcategory1(cat_id):
    sub_categories_2 = SubCategories2.objects.filter(
        sub_categories_1_id=cat_id)

    symptoms = {
        -1: sub_categories_2.first().sub_categories_1.name_vn,
    }
    for sub_cat in sub_categories_2:
        symptoms[sub_cat.id] = PartSymptoms.objects.filter(
            part_id=sub_cat.id)

    return symptoms


def get_sub_cat2_by_sub_cat1(cat1_id):
    sub_categories_2 = SubCategories2.objects.filter(
        sub_categories_1_id=cat_id1)

    return sub_categories_2
