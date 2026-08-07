const TextProcessor = require('./src/index');

// Create a processor with default options
const processor = new TextProcessor();

// Example usage
const text = "  Hello World! This is a TEST.  ";
console.log('Original:', text);
console.log('Processed:', processor.process(text));
console.log('Word count:', processor.countWords(text));
console.log('Unique words:', processor.extractUniqueWords(text));
console.log('Stats:', processor.getStats(text));

// Custom options
const customProcessor = new TextProcessor({
  caseSensitive: true,
  trimWhitespace: true
});

#VOU ADICIONAR ESSA LINHA AQUI, IMAGINE QUE ISSO É UM BLOCO DE CÓDIGO QUE REALMENTE PRESTA PARA ALGO
console.log('\nCustom processor:', customProcessor.process('  Mixed CASE Text  '));
