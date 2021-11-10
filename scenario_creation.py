from read_triples import create_list_and_dicts
import driver_util as util
from create_context import select_speaker, create_context

speaker_list = ["Chandler", "Joey", "Monica", "Phoebe", "Rachel", "Ross"]


def create_sequence(entity_list, entity_dict, speakers, scenario_id, num_pictures=10):
    speaker, speaker_info = select_speaker(speakers, entity_dict)

    for num in range(1, num_pictures+1):
        context = create_context(entity_list, entity_dict, speaker, speaker_info)

        scenario_timestamp = f'picture_{num}'

        # Specify the path to an existing data folder where your scenario is created and saved as a sub-folder
        scenario_path = f"./data/{scenario_id}"

        # Define the folder where the images are saved
        imagefolder = scenario_path + "/" + scenario_timestamp + "/" + "image"

        # Create the scenario folder, the json files and a scenarioStorage and scenario in memory
        scenarioStorage = util.create_scenario(scenario_path, scenario_timestamp)
        scenario = scenarioStorage.create_scenario(scenario_timestamp, num,
                                                   num, context)


if __name__ == "__main__":
    entities, entlist = create_list_and_dicts()
    create_sequence(entlist, entities, speaker_list, 'scenario_1')