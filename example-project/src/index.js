const _ = require('lodash');

/**
 * Main text processor class
 */
class TextProcessor {
  constructor(options = {}) {
    this.caseSensitive = options.caseSensitive || false;
    this.trimWhitespace = options.trimWhitespace !== false;
  }

  /**
   * Process text with configured options
   * @param {string} text - Input text to process
   * @returns {string} Processed text
   */
  process(text) {
    if (!text || typeof text !== 'string') {
      return text;
    }

    let result = text;

    if (this.trimWhitespace) {
      result = result.trim();
    }

    if (!this.caseSensitive) {
      result = result.toLowerCase();
    }

    return result;
  }

  /**
   * Count words in text
   * @param {string} text - Input text
   * @returns {number} Word count
   */
  countWords(text) {
    if (!text) return 0;
    const words = text.split(/\s+/).filter(word => word.length > 0);
    return words.length;
  }

  /**
   * Extract unique words from text
   * @param {string} text - Input text
   * @returns {Array<string>} Unique words
   */
  extractUniqueWords(text) {
    if (!text) return [];
    const words = this.process(text).split(/\s+/);
    return _.uniq(words.filter(word => word.length > 0));
  }

  /**
   * Get text statistics
   * @param {string} text - Input text
   * @returns {Object} Statistics object
   */
  getStats(text) {
    return {
      wordCount: this.countWords(text),
      uniqueWords: this.extractUniqueWords(text).length,
      charCount: text ? text.length : 0,
      charCountNoSpaces: text ? text.replace(/\s/g, '').length : 0
    };
  }
}

module.exports = TextProcessor;
