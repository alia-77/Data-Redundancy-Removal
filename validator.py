from difflib import SequenceMatcher

def similarity(a, b):

    return SequenceMatcher(
        None,
        a.lower(),
        b.lower()
    ).ratio()


def classify_record(new_record, existing_records):

    for record in existing_records:

        # Definite duplicate
        if (
            record.email.lower() == new_record["email"].lower()
            or record.phone == new_record["phone"]
        ):

            return (
                "Duplicate",
                "A record with the same email or phone number already exists."
            )

        # Possible duplicate (false positive)
        same_name = similarity(
            record.name,
            new_record["name"]
        ) > 0.90

        same_address = similarity(
            record.address,
            new_record["address"]
        ) > 0.90

        if same_name and same_address:

            return (
                "Possible Duplicate",
                "A very similar record already exists. Please verify that this is a different person."
            )

    return (
        "Unique",
        "Record is unique."
    )