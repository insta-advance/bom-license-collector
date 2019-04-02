 [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
 
BOM License Collector
==========

BOM License Collector is a Python 3 script that generates a file containing all license texts of a BOM xml file. The script is designed to work with [CycloneDX](https://cyclonedx.org/) BOM files.

Usage
-----

Run the script with:

	$ python3 LicenseCollector.py
	
or

	$ ./LicenseCollector.py

#### Options

By default, *bom.xml* file is read as an input and the license texts are saved in *license_texts.txt* file. However, both options can be overwritten as follows:

	$ ./LicenseCollector.py -i [input_file] -o [output_file]

License
-----------------

BOM License Collector is licensed under the terms of the MIT License. See the [LICENSE] file for the full license.

[License]: https://github.com/intopalo/bom-license-collector/blob/master/LICENSE



