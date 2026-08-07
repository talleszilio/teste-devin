const TextProcessor = require('../src/index');

describe('TextProcessor', () => {
  let processor;

  beforeEach(() => {
    processor = new TextProcessor();
  });

  describe('process', () => {
    test('should trim whitespace by default', () => {
      expect(processor.process('  hello  ')).toBe('hello');
    });

    test('should convert to lowercase by default', () => {
      expect(processor.process('HELLO')).toBe('hello');
    });

    test('should handle empty input', () => {
      expect(processor.process('')).toBe('');
      expect(processor.process(null)).toBe(null);
    });
  });

  describe('countWords', () => {
    test('should count words correctly', () => {
      expect(processor.countWords('hello world test')).toBe(3);
    });

    test('should handle empty input', () => {
      expect(processor.countWords('')).toBe(0);
    });
  });

  describe('extractUniqueWords', () => {
    test('should extract unique words', () => {
      const words = processor.extractUniqueWords('hello world hello test world');
      expect(words).toEqual(expect.arrayContaining(['hello', 'world', 'test']));
      expect(words.length).toBe(3);
    });
  });

  describe('getStats', () => {
    test('should return text statistics', () => {
      const stats = processor.getStats('hello world');
      expect(stats.wordCount).toBe(2);
      expect(stats.charCount).toBe(11);
    });
  });
});
