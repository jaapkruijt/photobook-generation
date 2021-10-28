def parse_friends_to_dict():
    with open('friends-triples.txt') as triple_file:
        data = triple_file.read().split('.')
    data = [entity.replace('\n', '') for entity in data]
    data = [entity.split(';') for entity in data]
    data = [[triple.split('"') for triple in entity] for entity in data]
    data = [[[triple[0].split(), triple[1:]] for triple in entity] for entity in data]
    data.pop(-1)
    for entity in data:
        subj = entity[0][0][0]
        entity.append(subj)
        entity[0][0].remove(subj)
    entities = {}
    for entity in data:
        subj = entity[-1]
        triples = {}
        for trip in entity[:-1]:
            pred = trip[0][0]
            objs = list(set(trip[1]))
            objs = [value for value in objs if value not in ['', ', ', ',']]
            triples[pred] = objs
        entities[subj] = triples
    return entities



if __name__ == "__main__":
    ents = parse_friends_to_dict()
    print(ents)
