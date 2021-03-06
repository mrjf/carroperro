#!/usr/bin/env python
"""Makes and models of automobiles, and helpers to create and recognize
hashtags for them"""
	
from carroperro import util


class Cars:

    makes_models = [
        ('Acura', 'MDX'),
        ('Acura', 'RDX'),
        ('Acura', 'TLX'),
        ('Acura', 'ILX'),
        ('Acura', 'RLX'),
        ('Acura', 'NSX'),
        ('Alfa Romeo', 'Giulia'),
        ('Alfa Romeo', 'Stelvio'),
        ('Audi', 'Q5'),
        ('Audi', 'Q7'),
        ('Audi', 'A4'),
        ('Audi', 'A5'),
        ('Audi', 'Q3'),
        ('Audi', 'A6'),
        ('Audi', 'A3'),
        ('Audi', 'A7'),
        ('Audi', 'A8'),
        ('Audi', 'TT'),
        ('Audi', 'R8'),
        ('Bentley', 'Bentayga'),
        ('Bentley', 'Continental GT'),
        ('Bentley', 'Flying Spur'),
        ('Bentley', 'Mulsanne'),
        ('BMW', '3-Series'),
        ('BMW', 'X5'),
        ('BMW', '5-Series'),
        ('BMW', 'X3'),
        ('BMW', 'X1'),
        ('BMW', '4-Series'),
        ('BMW', '2-Series'),
        ('BMW', 'X6'),
        ('BMW', '7-Series'),
        ('BMW', 'X4'),
        ('BMW', '6-Series'),
        ('BMW', 'i3'),
        ('BMW', 'i8'),
        ('BMW', 'Z4'),
        ('Buick', 'Enclave'),
        ('Buick', 'Encore'),
        ('Buick', 'Envision'),
        ('Buick', 'LaCrosse'),
        ('Buick', 'Regal'),
        ('Buick', 'Cascada'),
        ('Buick', 'Verano'),
        ('Cadillac', 'XT5'),
        ('Cadillac', 'Escalade'),
        ('Cadillac', 'XTS'),
        ('Cadillac', 'ATS'),
        ('Cadillac', 'CT6'),
        ('Cadillac', 'CTS'),
        ('Cadillac', 'SRX'),
        ('Cadillac', 'ELR'),
        ('Chevrolet', 'Silverado'),
        ('Chevrolet', 'Equinox'),
        ('Chevrolet', 'Malibu'),
        ('Chevrolet', 'Traverse'),
        ('Chevrolet', 'Cruze'),
        ('Chevrolet', 'Colorado'),
        ('Chevrolet', 'Tahoe'),
        ('Chevrolet', 'Impala'),
        ('Chevrolet', 'Trax'),
        ('Chevrolet', 'Suburban'),
        ('Chevrolet', 'Camaro'),
        ('Chevrolet', 'Express'),
        ('Chevrolet', 'Spark'),
        ('Chevrolet', 'Bolt'),
        ('Chevrolet', 'Sonic'),
        ('Chevrolet', 'Corvette'),
        ('Chevrolet', 'Volt'),
        ('Chevrolet', 'SS'),
        ('Chevrolet', 'City Express'),
        ('Chevrolet', 'Caprice PPV'),
        ('Chrysler', 'Pacifica'),
        ('Chrysler', '300'),
        ('Chrysler', '200'),
        ('Chrysler', 'Town & Country'),
        ('Dodge', 'Ram'),
        ('Dodge', 'Grand Caravan'),
        ('Dodge', 'Charger'),
        ('Dodge', 'Durango'),
        ('Dodge', 'Journey'),
        ('Dodge', 'Challenger'),
        ('Dodge', 'Dart'),
        ('Dodge', 'Viper'),
        ('Dodge', 'Avenger'),
        ('Fiat', '500'),
        ('Fiat', '500X'),
        ('Fiat', '124 Spider'),
        ('Fiat', '500L'),
        ('Ford', 'F-Series'),
        ('Ford', 'Escape'),
        ('Ford', 'Explorer'),
        ('Ford', 'Fusion'),
        ('Ford', 'Focus'),
        ('Ford', 'Edge'),
        ('Ford', 'Transit'),
        ('Ford', 'Mustang'),
        ('Ford', 'E-Series'),
        ('Ford', 'Expedition'),
        ('Ford', 'Fiesta'),
        ('Ford', 'Transit Connect'),
        ('Ford', 'Taurus'),
        ('Ford', 'Flex'),
        ('Ford', 'C-Max'),
        ('Ford', 'GT'),
        ('Genesis', 'G80'),
        ('Genesis', 'G90'),
        ('GMC', 'Sierra'),
        ('GMC', 'Acadia'),
        ('GMC', 'Terrain'),
        ('GMC', 'Yukon'),
        ('GMC', 'Yukon XL'),
        ('GMC', 'Canyon'),
        ('GMC', 'Savana'),
        ('Honda', 'CR-V'),
        ('Honda', 'Civic'),
        ('Honda', 'Accord'),
        ('Honda', 'Pilot'),
        ('Honda', 'Odyssey'),
        ('Honda', 'HR-V'),
        ('Honda', 'Fit'),
        ('Honda', 'Ridgeline'),
        ('Honda', 'Clarity FCV'),
        ('Honda', 'CR-Z'),
        ('Honda', 'Crosstour'),
        ('Honda', 'Insight'),
        ('Hyundai', 'Elantra'),
        ('Hyundai', 'Tucson'),
        ('Hyundai', 'Santa Fe'),
        ('Hyundai', 'Sonata'),
        ('Hyundai', 'Accent'),
        ('Hyundai', 'Ioniq'),
        ('Hyundai', 'Veloster'),
        ('Hyundai', 'Azera'),
        ('Hyundai', 'Genesis'),
        ('Hyundai', 'Equus'),
        ('Infiniti', 'Q50'),
        ('Infiniti', 'QX60'),
        ('Infiniti', 'QX50'),
        ('Infiniti', 'QX80'),
        ('Infiniti', 'Q60'),
        ('Infiniti', 'QX30'),
        ('Infiniti', 'Q70'),
        ('Infiniti', 'QX70'),
        ('Jaguar', 'F-Pace'),
        ('Jaguar', 'XE'),
        ('Jaguar', 'XF'),
        ('Jaguar', 'F-Type'),
        ('Jaguar', 'XJ'),
        ('Jeep', 'Grand Cherokee'),
        ('Jeep', 'Cherokee'),
        ('Jeep', 'Wrangler'),
        ('Jeep', 'Compass'),
        ('Jeep', 'Renegade'),
        ('Kia', 'Forte'),
        ('Kia', 'Optima'),
        ('Kia', 'Sorento'),
        ('Kia', 'Soul'),
        ('Kia', 'Sportage'),
        ('Kia', 'Niro'),
        ('Kia', 'Rio'),
        ('Kia', 'Sedona'),
        ('Kia', 'Cadenza'),
        ('Kia', 'K900'),
        ('Kia', 'Stinger'),
        ('Land Rover', 'Range Rover'),
        ('Land Rover', 'Discovery'),
        ('Lexus', 'RX'),
        ('Lexus', 'NX'),
        ('Lexus', 'ES'),
        ('Lexus', 'IS'),
        ('Lexus', 'GX'),
        ('Lexus', 'RC'),
        ('Lexus', 'GS'),
        ('Lexus', 'LX'),
        ('Lexus', 'LS'),
        ('Lexus', 'LC'),
        ('Lexus', 'CT'),
        ('Lexus', 'LFA'),
        ('Lincoln', 'MKX'),
        ('Lincoln', 'MKC'),
        ('Lincoln', 'MKZ'),
        ('Lincoln', 'Navigator'),
        ('Lincoln', 'Continental'),
        ('Lincoln', 'MKT'),
        ('Lincoln', 'MKS'),
        ('Maserati', 'Levante'),
        ('Maserati', 'Ghibli'),
        ('Maserati', 'Quattroporte'),
        ('Maserati', 'GranTurismo'),
        ('Mazda', 'CX-5'),
        ('Mazda', '3'),
        ('Mazda', 'CX-9'),
        ('Mazda', '6'),
        ('Mazda', 'CX-3'),
        ('Mazda', 'MX-5 Miata'),
        ('Mazda', '5'),
        ('Mercedes-AMG', 'GT'),
        ('Mercedes-Benz', 'C-Class'),
        ('Mercedes-Benz', 'GLC-Class'),
        ('Mercedes-Benz', 'GLE-Class'),
        ('Mercedes-Benz', 'E / CLS-Class'),
        ('Mercedes-Benz', 'GLS-Class'),
        ('Mercedes-Benz', 'GLA-Class'),
        ('Mercedes-Benz', 'Sprinter'),
        ('Mercedes-Benz', 'CLA-Class'),
        ('Mercedes-Benz', 'S-Class'),
        ('Mercedes-Benz', 'Metris'),
        ('Mercedes-Benz', 'SL-Class'),
        ('Mercedes-Benz', 'SLC-Class'),
        ('Mercedes-Benz', 'G-Class'),
        ('Mercedes-Benz', 'B-Class'),
        ('Mini', 'Cooper'),
        ('Mini', 'Countryman'),
        ('Mini', 'Paceman'),
        ('Mitsubishi', 'Outlander'),
        ('Mitsubishi', 'Outlander Sport'),
        ('Mitsubishi', 'Mirage'),
        ('Mitsubishi', 'Lancer'),
        ('Mitsubishi', 'i MiEV'),
        ('Nissan', 'Rogue'),
        ('Nissan', 'Altima'),
        ('Nissan', 'Sentra'),
        ('Nissan', 'Murano'),
        ('Nissan', 'Titan'),
        ('Nissan', 'Versa'),
        ('Nissan', 'Frontier'),
        ('Nissan', 'Pathfinder'),
        ('Nissan', 'Maxima'),
        ('Nissan', 'Armada'),
        ('Nissan', 'NV200'),
        ('Nissan', 'NV'),
        ('Nissan', 'Juke'),
        ('Nissan', '370Z'),
        ('Nissan', 'Leaf'),
        ('Nissan', 'GT-R'),
        ('Nissan', 'Quest'),
        ('Nissan', 'Xterra'),
        ('Porsche', 'Macan'),
        ('Porsche', 'Cayenne'),
        ('Porsche', '911'),
        ('Porsche', 'Panamera'),
        ('Porsche', 'Cayman'),
        ('Porsche', 'Boxster'),
        ('Ram', 'ProMaster'),
        ('Ram', 'ProMaster City'),
        ('Scion', 'tC'),
        ('Scion', 'xD'),
        ('Subaru', 'Forester'),
        ('Subaru', 'Outback'),
        ('Subaru', 'Crosstrek'),
        ('Subaru', 'Impreza'),
        ('Subaru', 'Legacy'),
        ('Subaru', 'BRZ'),
        ('Tesla', 'Model S'),
        ('Tesla', 'Model X'),
        ('Tesla', 'Model 3'),
        ('Toyota', 'Camry'),
        ('Toyota', 'RAV4'),
        ('Toyota', 'Corolla'),
        ('Toyota', 'Highlander'),
        ('Toyota', 'Tacoma'),
        ('Toyota', '4Runner'),
        ('Toyota', 'Tundra'),
        ('Toyota', 'Prius'),
        ('Toyota', 'Sienna'),
        ('Toyota', 'C-HR'),
        ('Toyota', 'Yaris'),
        ('Toyota', 'Avalon'),
        ('Toyota', 'Sequoia'),
        ('Toyota', 'Land Cruiser'),
        ('Toyota', 'Mirai'),
        ('Toyota', 'Venza'),
        ('Toyota', 'FJ Cruiser'),
        ('Volkswagen', 'Jetta'),
        ('Volkswagen', 'Tiguan'),
        ('Volkswagen', 'Atlas'),
        ('Volkswagen', 'Golf'),
        ('Volkswagen', 'Passat'),
        ('Volkswagen', 'Beetle'),
        ('Volkswagen', 'Touareg'),
        ('Volkswagen', 'Eos'),
        ('Volvo', 'XC90'),
        ('Volvo', 'XC60 II'),
        ('Volvo', 'S90'),
        ('Volvo', 'S60'),
        ('Volvo', 'XC60'),
        ('Volvo', 'V90'),
        ('Volvo', 'V60'),
        ('Volvo', 'S80'),
        ('Volvo', 'XC70'),
    ]

    def __init__(self):

        self.makes = sorted(
            list(set([make for make, model in self.makes_models])),
        )
        self.models = sorted(
            list(set([model for make, model in self.makes_models])),
        )

        # We want to be somewhat flexible in the hashtags we allow to match for
        # each make and model. Differences in non-alphanumeric characters
        # should be ignored.

        self.make_model_hashtags = {
            util.fold_hashtag(
                make + model,
            ): (make, model) for make, model in self.makes_models
        }
        self.model_hashtags = {
            util.fold_hashtag(model): (
                make, model,
            ) for make, model in self.makes_models
            if len(model) > 4
        }

    def name_from_hashtag(self, hashtag):
        if hashtag in self.make_model_hashtags:
            return ' '.join(self.make_model_hashtags[hashtag])
        elif hashtag in self.model_hashtags:
            return ' '.join(self.model_hashtags[hashtag])
        else:
            return None
