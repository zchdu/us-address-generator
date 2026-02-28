# US Address Generator

A command-line tool that generates realistic US addresses for testing and form-filling purposes.

**Single-file Python 3 script with zero dependencies** — only uses the standard library.

## Features

- Generates complete US address profiles: name, street, apartment, city, state, ZIP, phone, email
- Built-in real data for all 50 states + DC (cities, ZIP code ranges, area codes)
- **Defaults to tax-free states** (OR, MT, NH, DE, AK) when no state is specified
- Supports text and JSON output formats
- Batch generation with `--count`

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/us-address-generator.git
cd us-address-generator
```

No dependencies to install — just Python 3.

## Usage

```bash
# Generate 1 address (random tax-free state)
python3 us_address_generator.py

# Generate 5 addresses
python3 us_address_generator.py -n 5

# Specify a state
python3 us_address_generator.py -s CA

# JSON output
python3 us_address_generator.py -n 3 -f json

# Combine options
python3 us_address_generator.py -n 2 -s NY -f json
```

### CLI Options

| Option | Description |
|--------|-------------|
| `-n`, `--count` | Number of addresses to generate (default: 1) |
| `-s`, `--state` | State abbreviation (e.g., `CA`, `NY`). Defaults to tax-free states |
| `-f`, `--format` | Output format: `text` (default) or `json` |
| `-h`, `--help` | Show help message |

## Output Examples

### Text Format (default)

```
John Smith
1234 Oak Avenue, Apt 5B
Los Angeles, CA 90012
Phone: (213) 555-1234
Email: john.smith@gmail.com
```

### JSON Format (`-f json`)

```json
{
  "first_name": "John",
  "last_name": "Smith",
  "street": "1234 Oak Avenue",
  "apt": "Apt 5B",
  "city": "Los Angeles",
  "state": "CA",
  "zip": "90012",
  "phone": "(213) 555-1234",
  "email": "john.smith@gmail.com"
}
```

When generating multiple addresses with `-f json`, results are returned as a JSON array.

## Generated Fields

| Field | Generation Method |
|-------|-------------------|
| Name | Random first + last from common US name pools |
| Street | Random house number + street name + type (St/Ave/Blvd/Dr/...), optional direction prefix |
| Apartment | 25% chance of appearing, with random format (Apt/Suite/Unit/#) |
| City | Real cities matched to the selected state |
| State | Full 50 states + DC support with abbreviations |
| ZIP Code | Generated within the state's real ZIP code range |
| Phone | Uses real area codes for the selected state |
| Email | Derived from the generated name with random domain |

## Tax-Free States

When no `--state` is specified, the generator randomly picks from states with no sales tax:

- **Oregon (OR)**
- **Montana (MT)**
- **New Hampshire (NH)**
- **Delaware (DE)**
- **Alaska (AK)**

## License

MIT
