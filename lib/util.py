# A simple dictionary extension that maps dot-notation access to public keys (do not start with '_')
# while maintaining normal attribute behavior for private ('_...') keys.
import yaml


class DotDict(dict):
    def __getattr__(self, k):
        if k[0] == '_':
            return object.__getattribute__(self, k)
        else:
            return self.__getitem__(k)

    def __setattr__(self, k, v):
        if k[0] == '_':
            object.__setattr__(self, k, v)
        else:
            self.__setitem__(k, v)


yaml.add_representer(DotDict, yaml.Dumper.yaml_representers[dict], yaml.Dumper)
