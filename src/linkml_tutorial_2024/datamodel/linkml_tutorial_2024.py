# Auto generated from linkml_tutorial_2024.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-06-26T09:28:36
# Schema: linkml-tutorial-2024
#
# id: https://w3id.org/linkml/linkml-tutorial-2024
# description: A repostitory that walks through schema generation.
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Float, String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ENVO = CurieNamespace('ENVO', 'http://purl.obolibrary.org/obo/ENVO_')
KBASE = CurieNamespace('KBase', 'https://kbase.us/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
SIO = CurieNamespace('SIO', 'http://semanticscience.org/resource/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_TUTORIAL_2024 = CurieNamespace('linkml_tutorial_2024', 'https://w3id.org/linkml/linkml-tutorial-2024/')
NMDC = CurieNamespace('nmdc', 'https://w3id.org/nmdc/')
OBO = CurieNamespace('obo', 'http://purl.obolibrary.org/obo/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = LINKML_TUTORIAL_2024


# Types

# Class references
class SampleCollectionId(extended_str):
    pass


class SampleId(extended_str):
    pass


class AirSampleId(SampleId):
    pass


class SoilSampleId(SampleId):
    pass


@dataclass
class SampleCollection(YAMLRoot):
    """
    A collection of samples.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL_2024["SampleCollection"]
    class_class_curie: ClassVar[str] = "linkml_tutorial_2024:SampleCollection"
    class_name: ClassVar[str] = "SampleCollection"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL_2024.SampleCollection

    id: Union[str, SampleCollectionId] = None
    samples: Optional[Union[Dict[Union[str, SampleId], Union[dict, "Sample"]], List[Union[dict, "Sample"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleCollectionId):
            self.id = SampleCollectionId(self.id)

        self._normalize_inlined_as_list(slot_name="samples", slot_type=Sample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Sample(YAMLRoot):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population, or a
    portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration, or trial use.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SIO["001050"]
    class_class_curie: ClassVar[str] = "SIO:001050"
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL_2024.Sample

    id: Union[str, SampleId] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    species: Optional[Union[Union[str, "SpeciesEnum"], List[Union[str, "SpeciesEnum"]]]] = empty_list()
    sample_biome: Optional[Union[str, "BiomeTypeEnum"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self.latitude is not None and not isinstance(self.latitude, float):
            self.latitude = float(self.latitude)

        if self.longitude is not None and not isinstance(self.longitude, float):
            self.longitude = float(self.longitude)

        if self.sample_biome is not None and not isinstance(self.sample_biome, BiomeTypeEnum):
            self.sample_biome = BiomeTypeEnum(self.sample_biome)

        super().__post_init__(**kwargs)


@dataclass
class AirSample(Sample):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL_2024["AirSample"]
    class_class_curie: ClassVar[str] = "linkml_tutorial_2024:AirSample"
    class_name: ClassVar[str] = "Air Sample"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL_2024.AirSample

    id: Union[str, AirSampleId] = None
    altitude: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AirSampleId):
            self.id = AirSampleId(self.id)

        if self.altitude is not None and not isinstance(self.altitude, float):
            self.altitude = float(self.altitude)

        super().__post_init__(**kwargs)


@dataclass
class SoilSample(Sample):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_TUTORIAL_2024["SoilSample"]
    class_class_curie: ClassVar[str] = "linkml_tutorial_2024:SoilSample"
    class_name: ClassVar[str] = "Soil Sample"
    class_model_uri: ClassVar[URIRef] = LINKML_TUTORIAL_2024.SoilSample

    id: Union[str, SoilSampleId] = None
    depth: Optional[float] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SoilSampleId):
            self.id = SoilSampleId(self.id)

        if self.depth is not None and not isinstance(self.depth, float):
            self.depth = float(self.depth)

        super().__post_init__(**kwargs)


# Enumerations
class BiomeTypeEnum(EnumDefinitionImpl):
    """
    The type of biome.
    """
    forest = PermissibleValue(
        text="forest",
        meaning=ENVO["00000111"])
    lake = PermissibleValue(
        text="lake",
        meaning=ENVO["00000020"])
    ocean = PermissibleValue(
        text="ocean",
        meaning=ENVO["00000015"])
    desert = PermissibleValue(
        text="desert",
        meaning=ENVO["01001357"])
    air = PermissibleValue(
        text="air",
        meaning=ENVO["00002005"])

    _defn = EnumDefinition(
        name="BiomeTypeEnum",
        description="The type of biome.",
    )

class SpeciesEnum(EnumDefinitionImpl):
    """
    The species of micro organisms collected in the sample.
    """
    _defn = EnumDefinition(
        name="SpeciesEnum",
        description="The species of micro organisms collected in the sample.",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=LINKML_TUTORIAL_2024.id, name="id", curie=LINKML_TUTORIAL_2024.curie('id'),
                   model_uri=LINKML_TUTORIAL_2024.id, domain=None, range=URIRef)

slots.altitude = Slot(uri=LINKML_TUTORIAL_2024.altitude, name="altitude", curie=LINKML_TUTORIAL_2024.curie('altitude'),
                   model_uri=LINKML_TUTORIAL_2024.altitude, domain=None, range=Optional[float])

slots.latitude = Slot(uri=SCHEMA.latitude, name="latitude", curie=SCHEMA.curie('latitude'),
                   model_uri=LINKML_TUTORIAL_2024.latitude, domain=None, range=Optional[float])

slots.longitude = Slot(uri=SCHEMA.longitude, name="longitude", curie=SCHEMA.curie('longitude'),
                   model_uri=LINKML_TUTORIAL_2024.longitude, domain=None, range=Optional[float])

slots.species = Slot(uri=LINKML_TUTORIAL_2024.species, name="species", curie=LINKML_TUTORIAL_2024.curie('species'),
                   model_uri=LINKML_TUTORIAL_2024.species, domain=None, range=Optional[Union[Union[str, "SpeciesEnum"], List[Union[str, "SpeciesEnum"]]]])

slots.depth = Slot(uri=LINKML_TUTORIAL_2024.depth, name="depth", curie=LINKML_TUTORIAL_2024.curie('depth'),
                   model_uri=LINKML_TUTORIAL_2024.depth, domain=None, range=Optional[float])

slots.sample_biome = Slot(uri=LINKML_TUTORIAL_2024.sample_biome, name="sample biome", curie=LINKML_TUTORIAL_2024.curie('sample_biome'),
                   model_uri=LINKML_TUTORIAL_2024.sample_biome, domain=None, range=Optional[Union[str, "BiomeTypeEnum"]])

slots.samples = Slot(uri=LINKML_TUTORIAL_2024.samples, name="samples", curie=LINKML_TUTORIAL_2024.curie('samples'),
                   model_uri=LINKML_TUTORIAL_2024.samples, domain=None, range=Optional[Union[Dict[Union[str, SampleId], Union[dict, Sample]], List[Union[dict, Sample]]]])

slots.Air_Sample_id = Slot(uri=LINKML_TUTORIAL_2024.id, name="Air Sample_id", curie=LINKML_TUTORIAL_2024.curie('id'),
                   model_uri=LINKML_TUTORIAL_2024.Air_Sample_id, domain=AirSample, range=Union[str, AirSampleId],
                   pattern=re.compile(r'^airsample:\d*'))

slots.Soil_Sample_id = Slot(uri=LINKML_TUTORIAL_2024.id, name="Soil Sample_id", curie=LINKML_TUTORIAL_2024.curie('id'),
                   model_uri=LINKML_TUTORIAL_2024.Soil_Sample_id, domain=SoilSample, range=Union[str, SoilSampleId],
                   pattern=re.compile(r'^soilsample:\d*'))