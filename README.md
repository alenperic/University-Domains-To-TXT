# University Domains and Names Data List & API with Domain Extraction Script

This repository is a fork of the original University Domains and Names Data List & API, extended to include a Python script for extracting university domain data into a `.txt` file. It utilizes the comprehensive JSON dataset of university domains, names, and countries from around the world, which may be used as an allowlist or blocklist, depending on the specific consumer needs.

## Features

- A JSON file containing a detailed list of universities and their associated domain names, based on [University Domains and Names Data List & API by Hipo](https://github.com/Hipo/university-domains-list).
- A Python script that allows for the extraction of these domains to a `.txt` file, which can be used for various purposes such as domain validation or data analysis.
- A finished extract from November 2023, if running the Python script is not an option.

## Example Use Cases:

- Validate email domains efficiently by cross-referencing with the university domain list.
- Derive a user's university and country based on their email domain automatically.

### Using the Python Script

To extract university domains to a `.txt` file, use the provided Python script `extract_domains_to_txt.py` with the following usage:

```bash
python extract_domains_to_txt.py [-L local_file_path]
```

If the `-L` option is not specified, the script will by default download the latest data from the Hipo GitHub repository.

### Using the Original JSON Data

The original dataset is located in the `world_universities_and_domains.json` file and is structured as follows:

```json
[
    ...
    {
        "alpha_two_code": "TR",
        "country": "Turkey",
        "state-province": null,
        "domains": [
            "sabanciuniv.edu",
            "sabanciuniv.edu.tr"
        ],
        "name": "Sabanci University",
        "web_pages": [
            "http://www.sabanciuniv.edu/",
            "http://www.sabanciuniv.edu.tr/"
        ],
    },
    ...
]
```

### Original Hosted API

For small projects or exploratory purposes, you can use the free hosted API sponsored by [Hipo](http://www.hipolabs.com). For larger projects, consider hosting the data on your own server.

Example API requests:

- `http://universities.hipolabs.com`
- `http://universities.hipolabs.com/search?name=middle`
- `http://universities.hipolabs.com/search?name=middle&country=turkey`

## Contribution

Contributions to this project are welcome. If you find any data inaccuracies or have updates, please open a pull request or create an issue.

## Contributors

This project exists thanks to all the people who contribute. A list of original contributors can be found [here](https://github.com/Hipo/university-domains-list/graphs/contributors).

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Credit goes to the original creators and contributors of the [University Domains and Names Data List & API](https://github.com/Hipo/university-domains-list).

### Created and maintained by Alen Peric
