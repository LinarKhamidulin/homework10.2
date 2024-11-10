import re


def filter_parameters_from_the_user(parameters: dict)-> dict:
    try:
        file_to_process_ = re.findall(r"1|2|3", parameters.get("process"), flags=re.IGNORECASE)
        filter_by_status_ = re.findall(r"EXECUTED|CANCELED|PENDING", parameters.get("status"), flags=re.IGNORECASE)
        filter_by_data_ = re.findall(r"да|нет", parameters.get("data"), flags=re.IGNORECASE)
        sort_in_ascending_or_descending_order_ = re.findall(
            r"по возрастанию|по убыванию", parameters.get("ascending_or_descending"), flags=re.IGNORECASE
        )
        filter_by_currency_ = re.findall(r"да|нет", parameters.get("currency"), flags=re.IGNORECASE)

        parameters_from_the_user = {
            "process": file_to_process_[0],
            "status": filter_by_status_[0],
            "data": filter_by_data_[0],
            "ascending_or_descending": sort_in_ascending_or_descending_order_[0],
            "currency": filter_by_currency_[0],
        }

        return parameters_from_the_user

    except Exception:
        return f"Указаны не верные параметры для сортировки {parameters}"