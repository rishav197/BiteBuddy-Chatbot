import re



def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""


def get_str_from_food_dict(food_dict: dict):
    return ", ".join([f"{value} {key}" for key, value in food_dict.items()])


if __name__ == "__main__":
    # print(extract_session_id("projects/bitebuddy-chatbot-for-foo-qosr/agent/sessions/96458169-4c2e-5a97-cd39-aa71960872a9/contexts/ongoing-order"))
    print(get_str_from_food_dict({"somsa":2, "chhole":5}))
