# photobook-generation
Repository for creating fake data and utterances for an experiment where two agents talk about a photo book.

## Install packages

You need to install the EMISSOR package in order to run the code. You can download it by going to the command line and running:

    python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple emissor

Alternatively you can run the following three lines in the command line:

    git clone https://github.com/cltl/EMISSOR --branch issue-53-processing
    cd EMISSOR
    python install.py install

You will also need the following packages:
* `random`
* `os`

## Running the code
The main code to run for creating a scenario is in `scenario_creation.py`. You will need to specify the name of a folder where the scenario is stored, inside 'data'. Create the folder and put the name as a variable when running `create_sequence`. 

## Input triples
The information that serves as the input for the scenarios is triples from the television show *Friends* extracted from [WikiData](https://www.wikidata.org/) using the [Wikidata Query Service](https://query.wikidata.org/). Afterwards it was formatted so that it could be turned into a dictionary using the code in `read_triples.py`. More triples and new fake entities were also added. When adding new entities or new triples for an entity, be sure to adhere to the formatting structure, otherwise the triples will be read wrong and the dictionary output will be incorrect. 
Below is an example of triples for one entity:

    Paul name "Paul";
    full_name "Paul Stevens";
    sex_or_gender "male";
    unmarried_partner "Rachel Green";
    child "Elizabeth Stevens".

The first triple for an entity consists of three parts: `subject predicate object`.
In each subsequent triple the subject is omitted and only the predicate and object are put.
Objects are denoted with `" "` Each triple ends with a `;` except for the final triple 
for an entity, which ends with `.`. 