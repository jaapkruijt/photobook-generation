from read_triples import parse_friends_to_dict
import emissor
from random import getrandbits
import requests
from datetime import datetime
import driver_util as util
from create_context import select_speaker, create_context

def create_sequence(entity_list, entity_dict):
    speaker, speaker_info = select_speaker(entity_list, entity_dict)
    context = create_context(entity_list, entity_dict, speaker, speaker_info)

    ### The name of your scenario
    scenarioid = "test_scenario"

    ### Specify the path to an existing data folder where your scenario is created and saved as a subfolder
    scenario_path = "./data"

    ### Define the folder where the images are saved
    imagefolder = scenario_path + "/" + scenarioid + "/" + "image"


    ### Create the scenario folder, the json files and a scenarioStorage and scenario in memory
    scenarioStorage = util.create_scenario(scenario_path, scenarioid)
    scenario = scenarioStorage.create_scenario(scenarioid, datetime.now().microsecond, datetime.now().microsecond, context)

if __name__ == "__main__":
    entities = parse_friends_to_dict()
    entlist = []
    for key in entities:
        entlist.append(key)
    create_sequence(entlist, entities)