from read_triples import parse_friends_to_dict
from random import randint, sample
from emissor.representation.scenario import ScenarioContext
from emissor.representation.ldschema import emissor_dataclass

from typing import List


def select_speaker(entity_list, entity_dict):
    index = randint(0,len(entity_list)-1)
    speaker = entity_list[index]
    speaker_info = entity_dict[speaker]
    return speaker, speaker_info


def select_persons(entity_list, speaker, number):
    if speaker in entity_list:
        entity_list.remove(speaker)
    persons = sample(entity_list, number)
    return persons


@emissor_dataclass
class PhotobookContext(ScenarioContext):
    agent: str
    objects: List[str]
    persons: List[dict]
    speaker: dict


def create_context(entity_list, entity_dict, speaker, speaker_info):
    number = randint(1,2)
    persons = select_persons(entity_list, speaker, number)
    persons_info = []
    for person in persons:
        person_info = entity_dict[person]
        persons_info.append(person_info)
    # persons_json = json.dumps(persons_info)
    # speaker_json = json.dumps(speaker_info)
    agent = 'robot_agent'
    scenario_context = PhotobookContext(agent, [], persons_info, speaker_info)
    return scenario_context


if __name__ == "__main__":
    entities = parse_friends_to_dict()
    entity_list = []
    for key in entities:
        entity_list.append(key)
    speaker, speaker_info = select_speaker(entity_list, entities)
    cont = create_context(entity_list, entities, speaker, speaker_info)
    print(cont)
