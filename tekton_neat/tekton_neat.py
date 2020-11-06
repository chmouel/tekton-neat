"""Main module."""
import yaml

CLEANIT = [
    'metadata->generation',
    'metadata->annotations->kubectl.kubernetes.io/last-applied-configuration',
    'metadata->pipeline.tekton.dev/release',
    'creationTimestamp',
    'generation',
    'metadata->managedFields',
    'metadata->selfLink',
    'metadata->uid',
    'metadata->creationTimestamp',
    'metadata->resourceVersion',
    'status',
]


def process(yamls):
    """Process yamls document single or multiple."""
    jeez = yaml.safe_load(yamls)
    ret = []

    if 'items' in jeez:
        items = jeez['items']
    else:
        items = [jeez]

    for document in items:
        for key in CLEANIT:
            key_list = key.split('->')
            sub = document
            for i in key_list[:-1]:
                if i in sub:
                    sub = sub[i]
            if key_list[-1] in sub:
                del sub[key_list[-1]]
        ret.append("--- ")
        ret.append(yaml.dump(document))
    return ret
