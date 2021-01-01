from ..models import PartSymptoms, SubCategories2


def get_symptoms_by_part_id(part_id):
    return PartSymptoms.objects.filter(part_id=part_id)
