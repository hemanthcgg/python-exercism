def transform(legacy_data):
    final_result = {}
    for key,value in legacy_data.items():
        for i in list(value):
            final_result[i.lower()]=key
    return final_result