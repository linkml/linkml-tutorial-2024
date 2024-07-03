from __future__ import annotations 
from datetime import (
    datetime,
    date
)
from decimal import Decimal 
from enum import Enum 
import re
import sys
from typing import (
    Any,
    List,
    Literal,
    Dict,
    Optional,
    Union
)
from pydantic.version import VERSION  as PYDANTIC_VERSION 
if int(PYDANTIC_VERSION[0])>=2:
    from pydantic import (
        BaseModel,
        ConfigDict,
        Field,
        field_validator
    )
else:
    from pydantic import (
        BaseModel,
        Field,
        validator
    )

metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass


class BiomeTypeEnum(str, Enum):
    """
    The type of biome.
    """
    forest = "forest"
    lake = "lake"
    ocean = "ocean"
    desert = "desert"
    air = "air"


class SpeciesEnum(str):
    """
    The species of micro organisms collected in the sample.
    """
    pass


class SampleCollection(ConfiguredBaseModel):
    """
    A collection of samples.
    """
    samples: Optional[Dict[str, Union[Sample,AirSample,SoilSample]]] = Field(default_factory=dict, description="""The samples in the collection.""")


class Sample(ConfiguredBaseModel):
    """
    A sample is a limited quantity of something (e.g. an individual or set of individuals from a population,  or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration,  or trial use.
    """
    id: str = Field(..., description="""The unique identifier for the biosample.""")
    latitude: Optional[float] = Field(None, description="""Latitude is a geographic coordinate which refers to the angle from a point on the Earth's surface to the  equatorial plane.""")
    longitude: Optional[float] = Field(None, description="""Longitude is a geographic position that refers to the angle east or west of a reference meridian between the  two geographical poles to another meridian that passes through an arbitrary point.""")
    species: Optional[List[SpeciesEnum]] = Field(default_factory=list, description="""The species of micro organisms collected in the sample.""")
    sample_biome: Optional[BiomeTypeEnum] = Field(None, description="""The biome type of the biosample""")
    sample_type: Literal["Sample"] = Field("Sample", description="""The type of sample.""")


class AirSample(Sample):
    """
    A sample of air
    """
    altitude: Optional[float] = Field(None, description="""Altitude is the height of an object or point in relation to a specific reference point, such as the sea level.""")
    id: str = Field(..., description="""The unique identifier for the biosample.""")
    latitude: Optional[float] = Field(None, description="""Latitude is a geographic coordinate which refers to the angle from a point on the Earth's surface to the  equatorial plane.""")
    longitude: Optional[float] = Field(None, description="""Longitude is a geographic position that refers to the angle east or west of a reference meridian between the  two geographical poles to another meridian that passes through an arbitrary point.""")
    species: Optional[List[SpeciesEnum]] = Field(default_factory=list, description="""The species of micro organisms collected in the sample.""")
    sample_biome: Optional[BiomeTypeEnum] = Field(None, description="""The biome type of the biosample""")
    sample_type: Literal["AirSample"] = Field("AirSample", description="""The type of sample.""")

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^airsample:\d*")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid id format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid id format: {v}")
        return v


class SoilSample(Sample):
    """
    A sample of soil
    """
    depth: Optional[int] = Field(None, description="""The depth in centimeters of the biosample.""")
    id: str = Field(..., description="""The unique identifier for the biosample.""")
    latitude: Optional[float] = Field(None, description="""Latitude is a geographic coordinate which refers to the angle from a point on the Earth's surface to the  equatorial plane.""")
    longitude: Optional[float] = Field(None, description="""Longitude is a geographic position that refers to the angle east or west of a reference meridian between the  two geographical poles to another meridian that passes through an arbitrary point.""")
    species: Optional[List[SpeciesEnum]] = Field(default_factory=list, description="""The species of micro organisms collected in the sample.""")
    sample_biome: Optional[BiomeTypeEnum] = Field(None, description="""The biome type of the biosample""")
    sample_type: Literal["SoilSample"] = Field("SoilSample", description="""The type of sample.""")

    @field_validator('id')
    def pattern_id(cls, v):
        pattern=re.compile(r"^soilsample:\d*")
        if isinstance(v,list):
            for element in v:
                if not pattern.match(element):
                    raise ValueError(f"Invalid id format: {element}")
        elif isinstance(v,str):
            if not pattern.match(v):
                raise ValueError(f"Invalid id format: {v}")
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
SampleCollection.model_rebuild()
Sample.model_rebuild()
AirSample.model_rebuild()
SoilSample.model_rebuild()

