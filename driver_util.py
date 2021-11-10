import os
from emissor.persistence import ScenarioStorage


def create_scenario(scenarioPath: str, scenarioid: str):
    myscenariopath = scenarioPath+"/"+scenarioid
    if not os.path.exists(myscenariopath):
        os.mkdir(myscenariopath)
        print("Directory ", myscenariopath, " Created ")
    else:
        print("Directory ", myscenariopath, " already exists")
    imagefolder =  myscenariopath+"/"+"image"
    if not os.path.exists(imagefolder):
        os.mkdir(imagefolder)
        print("Directory ", imagefolder, " Created ")
    else:
        print("Directory ", imagefolder, " already exists")

    # so far not needed
    # textfolder = myscenariopath+"/"+"text"

    scenarioStorage = ScenarioStorage(scenarioPath)
    return scenarioStorage