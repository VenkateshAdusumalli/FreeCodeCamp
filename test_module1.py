from demographic_data_analyzer import calculate_demographic_data

def test_calculate():
    result = calculate_demographic_data(print_data=False)

    assert isinstance(result['race_count'], object), "race_count should be a Series"
    assert result['average_age_men'] > 30, "Average age of men should be realistic"
    assert result['percentage_bachelors'] > 10, "Percentage with Bachelors seems too low"
    assert result['min_work_hours'] >= 0, "Min work hours cannot be negative"

    print("✅ All basic tests passed.")
