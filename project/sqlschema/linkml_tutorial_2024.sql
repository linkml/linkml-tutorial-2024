-- # Class: "SampleCollection" Description: "A collection of samples."
--     * Slot: id Description: The unique identifier for the biosample.
-- # Class: "Sample" Description: "A sample is a limited quantity of something (e.g. an individual or set of individuals from a population,  or a portion of a substance) to be used for testing, analysis, inspection, investigation, demonstration,  or trial use."
--     * Slot: id Description: The unique identifier for the biosample.
--     * Slot: latitude Description: Latitude is a geographic coordinate which refers to the angle from a point on the Earth's surface to the  equatorial plane.
--     * Slot: longitude Description: Longitude is a geographic position that refers to the angle east or west of a reference meridian between the  two geographical poles to another meridian that passes through an arbitrary point.
--     * Slot: sample_biome Description: The biome type of the biosample
--     * Slot: SampleCollection_id Description: Autocreated FK slot
-- # Class: "Air Sample" Description: ""
--     * Slot: altitude Description: Altitude is the height of an object or point in relation to a specific reference point, such as the sea level.
--     * Slot: id Description: The unique identifier for the biosample.
--     * Slot: latitude Description: Latitude is a geographic coordinate which refers to the angle from a point on the Earth's surface to the  equatorial plane.
--     * Slot: longitude Description: Longitude is a geographic position that refers to the angle east or west of a reference meridian between the  two geographical poles to another meridian that passes through an arbitrary point.
--     * Slot: sample_biome Description: The biome type of the biosample
-- # Class: "Soil Sample" Description: ""
--     * Slot: depth Description: The depth in centimeters of the biosample.
--     * Slot: id Description: The unique identifier for the biosample.
--     * Slot: latitude Description: Latitude is a geographic coordinate which refers to the angle from a point on the Earth's surface to the  equatorial plane.
--     * Slot: longitude Description: Longitude is a geographic position that refers to the angle east or west of a reference meridian between the  two geographical poles to another meridian that passes through an arbitrary point.
--     * Slot: sample_biome Description: The biome type of the biosample
-- # Class: "Sample_species" Description: ""
--     * Slot: Sample_id Description: Autocreated FK slot
--     * Slot: species Description: The species of micro organisms collected in the sample.
-- # Class: "Air Sample_species" Description: ""
--     * Slot: Air Sample_id Description: Autocreated FK slot
--     * Slot: species Description: The species of micro organisms collected in the sample.
-- # Class: "Soil Sample_species" Description: ""
--     * Slot: Soil Sample_id Description: Autocreated FK slot
--     * Slot: species Description: The species of micro organisms collected in the sample.

CREATE TABLE "SampleCollection" (
	id TEXT NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Air Sample" (
	altitude FLOAT, 
	id TEXT NOT NULL, 
	latitude FLOAT, 
	longitude FLOAT, 
	sample_biome VARCHAR(6), 
	PRIMARY KEY (id)
);
CREATE TABLE "Soil Sample" (
	depth FLOAT, 
	id TEXT NOT NULL, 
	latitude FLOAT, 
	longitude FLOAT, 
	sample_biome VARCHAR(6), 
	PRIMARY KEY (id)
);
CREATE TABLE "Sample" (
	id TEXT NOT NULL, 
	latitude FLOAT, 
	longitude FLOAT, 
	sample_biome VARCHAR(6), 
	"SampleCollection_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("SampleCollection_id") REFERENCES "SampleCollection" (id)
);
CREATE TABLE "Air Sample_species" (
	"Air Sample_id" TEXT, 
	species VARCHAR, 
	PRIMARY KEY ("Air Sample_id", species), 
	FOREIGN KEY("Air Sample_id") REFERENCES "Air Sample" (id)
);
CREATE TABLE "Soil Sample_species" (
	"Soil Sample_id" TEXT, 
	species VARCHAR, 
	PRIMARY KEY ("Soil Sample_id", species), 
	FOREIGN KEY("Soil Sample_id") REFERENCES "Soil Sample" (id)
);
CREATE TABLE "Sample_species" (
	"Sample_id" TEXT, 
	species VARCHAR, 
	PRIMARY KEY ("Sample_id", species), 
	FOREIGN KEY("Sample_id") REFERENCES "Sample" (id)
);