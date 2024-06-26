-- # Class: "SampleCollection" Description: "A collection of samples."
--     * Slot: id Description: 
-- # Class: "Sample" Description: "A sample is a limited quantity of something (e.g. an individual or set of individuals from a population,  or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration,  or trial use."
--     * Slot: id Description: The unique identifier for the biosample.
--     * Slot: latitude Description: Latitude is a geographic coordinate which refers to the angle from a point on the Earth's surface to the  equatorial plane.
--     * Slot: longitude Description: Longitude is a geographic position that refers to the angle east or west of a reference meridian between the  two geographical poles to another meridian that passes through an arbitrary point.
--     * Slot: sample_biome Description: The biome type of the biosample
--     * Slot: sample_type Description: The type of sample.
--     * Slot: SampleCollection_id Description: Autocreated FK slot
-- # Class: "AirSample" Description: ""
--     * Slot: altitude Description: Altitude is the height of an object or point in relation to a specific reference point, such as the sea level.
--     * Slot: id Description: The unique identifier for the biosample.
--     * Slot: latitude Description: Latitude is a geographic coordinate which refers to the angle from a point on the Earth's surface to the  equatorial plane.
--     * Slot: longitude Description: Longitude is a geographic position that refers to the angle east or west of a reference meridian between the  two geographical poles to another meridian that passes through an arbitrary point.
--     * Slot: sample_biome Description: The biome type of the biosample
--     * Slot: sample_type Description: The type of sample.
-- # Class: "SoilSample" Description: ""
--     * Slot: depth Description: The depth in centimeters of the biosample.
--     * Slot: id Description: The unique identifier for the biosample.
--     * Slot: latitude Description: Latitude is a geographic coordinate which refers to the angle from a point on the Earth's surface to the  equatorial plane.
--     * Slot: longitude Description: Longitude is a geographic position that refers to the angle east or west of a reference meridian between the  two geographical poles to another meridian that passes through an arbitrary point.
--     * Slot: sample_biome Description: The biome type of the biosample
--     * Slot: sample_type Description: The type of sample.
-- # Class: "Sample_species" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: species Description: The species of micro organisms collected in the sample.
-- # Class: "AirSample_species" Description: ""
--     * Slot: AirSample_id Description: Autocreated FK slot
--     * Slot: species Description: The species of micro organisms collected in the sample.
-- # Class: "SoilSample_species" Description: ""
--     * Slot: SoilSample_id Description: Autocreated FK slot
--     * Slot: species Description: The species of micro organisms collected in the sample.

CREATE TABLE "SampleCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "AirSample" (
	altitude FLOAT, 
	id TEXT NOT NULL, 
	latitude FLOAT, 
	longitude FLOAT, 
	sample_biome VARCHAR(6), 
	sample_type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SoilSample" (
	depth INTEGER, 
	id TEXT NOT NULL, 
	latitude FLOAT, 
	longitude FLOAT, 
	sample_biome VARCHAR(6), 
	sample_type TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Sample" (
	id TEXT NOT NULL, 
	latitude FLOAT, 
	longitude FLOAT, 
	sample_biome VARCHAR(6), 
	sample_type TEXT, 
	"SampleCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("SampleCollection_id") REFERENCES "SampleCollection" (id)
);
CREATE TABLE "AirSample_species" (
	"AirSample_id" TEXT, 
	species VARCHAR, 
	PRIMARY KEY ("AirSample_id", species), 
	FOREIGN KEY("AirSample_id") REFERENCES "AirSample" (id)
);
CREATE TABLE "SoilSample_species" (
	"SoilSample_id" TEXT, 
	species VARCHAR, 
	PRIMARY KEY ("SoilSample_id", species), 
	FOREIGN KEY("SoilSample_id") REFERENCES "SoilSample" (id)
);
CREATE TABLE "Sample_species" (
	"Sample_id" TEXT, 
	species VARCHAR, 
	PRIMARY KEY ("Sample_id", species), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id)
);