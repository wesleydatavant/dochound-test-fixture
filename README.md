# widget-factory

A Python toolkit for building widgets, currently at version 3.1.0.

## Installation

```bash
git clone https://github.com/wesleydatavant/dochound-test-fixture.git
cd dochound-test-fixture
pip install widget-factory
```

## Getting Started

Use the `WidgetBuilder` to create widgets and `GadgetAssembler` to combine them.

The `render_widget` function converts a widget to HTML output.

See the [installation guide](docs/install.md) for detailed setup.

For architecture details, read [the design doc](docs/design.md).

Check out [the changelog](CHANGELOG.md).

Jump to the [FAQ](#frequently-asked-questions) section below.

## CLI

- `widget build`
- `widget serve`

## Usage

```bash
cd /Users/alice/projects/widget-factory
widget build --output-dir dist
```

## Features

- Fast widget rendering
- Extensible plugin system
