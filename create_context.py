from read_triples import parse_friends_to_dict
from random import randint, sample

def select_speaker(entity_list, entity_dict):
    index = randint(0,len(entity_list)-1)
    speaker = entity_list[index]
    speaker_info = entity_dict[speaker]
    return speaker, speaker_info

def select_persons(entity_list, speaker, number):
    entity_list.remove(speaker)
    persons = sample(entity_list, number)
    return persons

def create_context(entity_list, entity_dict, speaker, speaker_info):
    number = randint(1,2)
    persons = select_persons(entity_list, speaker, number)
    persons_info = []
    for person in persons:
        person_info = entity_dict[person]
        persons_info.append(person_info)
    context = '"agent": "robot_agent", "objects": [], "persons": {}, "speaker": {}'.format(persons_info, speaker_info)
    return context

if __name__ == "__main__":
    entities = parse_friends_to_dict()
    entity_list = []
    for key in entities:
        entity_list.append(key)
    scenario_context = create_context(entity_list, entities)
    print(scenario_context)
