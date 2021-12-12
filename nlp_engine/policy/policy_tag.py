from nlp_engine.policy_code.policy_code_tag import policy_code_tag
from pathlib import Path
import os
import pandas as pd

def policy_tag(body: str):
    """

    :param body: str
    :return: str

    This function returns the tag of policy from the body of a webpage.
    In practice, this tag is the definition of the policy code
    """

    policy_code = policy_code_tag(body)

    policy_code_array = policy_code.split(";")

    dir_path = Path(os.path.dirname(os.path.realpath(__file__)))

    path_to_policy_code_taxonomy = str(dir_path.parent.absolute()).replace("\\","/") + "/doc/policy_codes_last_layer.csv"

    policy_code_last_layer = pd.read_csv(filepath_or_buffer=path_to_policy_code_taxonomy,  header=0, sep=",")

    tag=[]
    for i in policy_code_array:
        for index_policy_code, row_policy_code in policy_code_last_layer.iterrows():
            if i == row_policy_code["Policy code"]:
                tag.append(row_policy_code["information or procedure"])

    return ";".join(tag)