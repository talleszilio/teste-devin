# Awesome Text Processor

![npm version](https://img.shields.io/npm/v/awesome-text-processor)
![License](https://img.shields.io/npm/l/awesome-text-processor)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen)

## Description

A powerful text processing utility library for Node.js that provides comprehensive text manipulation capabilities including word counting, unique word extraction, text statistics, and flexible text processing options.

## Features

- **Flexible Text Processing**: Configure case sensitivity and whitespace trimming
- **Word Counting**: Accurately count words in any text
- **Unique Word Extraction**: Extract and deduplicate words from text
- **Text Statistics**: Get comprehensive statistics including character counts
- **Simple API**: Easy-to-use interface with sensible defaults
- **Well Tested**: Comprehensive test coverage with Jest
- **Type-Safe**: Full JSDoc documentation for better IDE support

## Installation

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn package manager

### Steps

```bash
# Clone the repository
git clone <repository-url>
cd awesome-text-processor

# Install dependencies
npm install
```

Or install via npm:

```bash
npm install awesome-text-processor
```

## Usage

### Basic Usage

```javascript
const TextProcessor = require('awesome-text-processor');

// Create a processor with default options
const processor = new TextProcessor();

const text = "  Hello World! This is a TEST.  ";
console.log(processor.process(text)); // "hello world! this is a test."
console.log(processor.countWords(text)); // 5
console.log(processor.extractUniqueWords(text)); // ['hello', 'world!', 'this', 'is', 'a', 'test.']
console.log(processor.getStats(text)); // Statistics object
```

### Advanced Usage

```javascript
// Custom configuration
const customProcessor = new TextProcessor({
  caseSensitive: true,
  trimWhitespace: true
});

const text = "  Mixed CASE Text  ";
console.log(customProcessor.process(text)); // "Mixed CASE Text"

// Get detailed statistics
const stats = processor.getStats("Hello World Test");
console.log(stats);
// {
//   wordCount: 3,
//   uniqueWords: 3,
//   charCount: 16,
//   charCountNoSpaces: 13
// }
```

### API Reference

#### `TextProcessor(options)`

Creates a new TextProcessor instance.

**Options:**
- `caseSensitive` (boolean): Whether to preserve case (default: false)
- `trimWhitespace` (boolean): Whether to trim whitespace (default: true)

#### `process(text)`

Process text according to configured options.

**Parameters:**
- `text` (string): Input text to process

**Returns:** Processed string

#### `countWords(text)`

Count the number of words in text.

**Parameters:**
- `text` (string): Input text

**Returns:** Number of words

#### `extractUniqueWords(text)`

Extract unique words from text.

**Parameters:**
- `text` (string): Input text

**Returns:** Array of unique words

#### `getStats(text)`

Get comprehensive text statistics.

**Parameters:**
- `text` (string): Input text

**Returns:** Object with wordCount, uniqueWords, charCount, and charCountNoSpaces

## Configuration

The library accepts configuration options when creating a new TextProcessor instance:

```javascript
const processor = new TextProcessor({
  caseSensitive: true,    // Preserve original case
  trimWhitespace: false   // Don't trim whitespace
});
```

## Development

### Setup

```bash
# Clone the repository
git clone <repository-url>
cd awesome-text-processor

# Install dependencies
npm install
```

### Running Tests

```bash
# Run all tests
npm test

# Run tests in watch mode
npm test -- --watch

# Run tests with coverage
npm test -- --coverage
```

### Linting

```bash
# Run ESLint
npm run lint
```

### Running the Example

```bash
# Run the example file
node example.js
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes and add tests
4. Ensure all tests pass (`npm test`)
5. Ensure linting passes (`npm run lint`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

### Development Guidelines

- Write clean, readable code
- Add tests for new features
- Update documentation as needed
- Follow existing code style
- Ensure all tests pass before submitting

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Node.js](https://nodejs.org/)
- Uses [Lodash](https://lodash.com/) for utility functions
- Tested with [Jest](https://jestjs.io/)
- Linted with [ESLint](https://eslint.org/)

## Roadmap

Future enhancements planned:
- [ ] Add support for multiple languages
- [ ] Add text normalization features
- [ ] Add sentiment analysis capabilities
- [ ] Add text pattern matching
- [ ] Performance optimizations for large texts
