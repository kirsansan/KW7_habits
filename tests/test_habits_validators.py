import copy

import pytest
from tests.factories import HabitFactory


@pytest.mark.django_db
def test_validation_habit(authenticated_user, user, base_habit):
    auth_client = authenticated_user.get('client')
    auth_user = authenticated_user.get('user')

    # easy base create
    response = auth_client.post('/habit/create/', base_habit, format='json')
    assert response.status_code == 201

    # associated and reward exists checker
    tmp_habit = copy.deepcopy(base_habit)
    second_habit = HabitFactory(creator=auth_user)
    tmp_habit['associated_habit'] = second_habit.pk
    tmp_habit['reward'] = "fridge Rosenlew"
    response = auth_client.post('/habit/create/', tmp_habit, format='json')
    assert response.status_code == 400
    assert str(response.data['non_field_errors']) == "[ErrorDetail(string='You must " \
                                                     "specify associated habit or reward. " \
                                                     "Not both at the same time', code='invalid')]"
    #
    # associated exist and useful checker
    tmp_habit = copy.deepcopy(base_habit)
    second_habit = HabitFactory(creator=auth_user)
    second_habit.is_useful = False
    second_habit.save()
    tmp_habit['associated_habit'] = second_habit.pk
    response = auth_client.post('/habit/create/', tmp_habit, format='json')
    assert response.status_code == 400
    assert str(response.data['non_field_errors']) == "[ErrorDetail(string='Associated " \
                                                     "habit must have is_useful flag as True', " \
                                                     "code='invalid')]"

    # is_useful and reward
    tmp_habit = copy.deepcopy(base_habit)
    tmp_habit['is_useful'] = True
    tmp_habit['reward'] = "travel to Siberia"
    response = auth_client.post('/habit/create/', tmp_habit, format='json')
    assert response.status_code == 400
    assert str(response.data['non_field_errors']) == "[ErrorDetail(string='Useful " \
                                                     "habit must not have reward', " \
                                                     "code='invalid')]"

    # freq > 7
    tmp_habit = copy.deepcopy(base_habit)
    tmp_habit['frequency'] = 100500
    response = auth_client.post('/habit/create/', tmp_habit, format='json')
    assert response.status_code == 400
    assert str(response.data['non_field_errors']) == "[ErrorDetail(string='frequency " \
                                                     "of habit must be less 7 days', " \
                                                     "code='invalid')]"

    # time > 2:00
    tmp_habit = copy.deepcopy(base_habit)
    tmp_habit['time_for_action'] = "02:01"
    response = auth_client.post('/habit/create/', tmp_habit, format='json')
    assert response.status_code == 400
    assert str(response.data['non_field_errors']) == "[ErrorDetail(string='time_for_action " \
                                                     "must be less 2 minutes ', " \
                                                     "code='invalid')]"
