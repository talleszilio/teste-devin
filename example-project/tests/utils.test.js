/**
 * Testes para utilitários
 * Simula testes unitários em JavaScript
 */

const {
    toTitleCase,
    validateEmail,
    generateId,
    formatDateBR
} = require('../src/utils');

describe('Utils', () => {
    describe('toTitleCase', () => {
        test('deve converter primeira letra para maiúscula', () => {
            expect(toTitleCase('talles')).toBe('Talles');
        });
        
        test('deve manter demais letras minúsculas', () => {
            expect(toTitleCase('TALLES')).toBe('Talles');
        });
        
        test('deve retornar string vazia para input vazio', () => {
            expect(toTitleCase('')).toBe('');
        });
    });
    
    describe('validateEmail', () => {
        test('deve validar email correto', () => {
            expect(validateEmail('talleszilio@gmail.com')).toBe(true);
        });
        
        test('deve rejeitar email sem @', () => {
            expect(validateEmail('tallesziliogmail.com')).toBe(false);
        });
        
        test('deve rejeitar email sem domínio', () => {
            expect(validateEmail('talleszilio@')).toBe(false);
        });
        
        test('deve validar email com subdomínio', () => {
            expect(validateEmail('user@sub.domain.com')).toBe(true);
        });
        
        test('deve validar email com múltiplos subdomínios', () => {
            expect(validateEmail('user@mail.sub.domain.com')).toBe(true);
        });
    });
    
    describe('generateId', () => {
        test('deve gerar ID único', () => {
            const id1 = generateId();
            const id2 = generateId();
            expect(id1).not.toBe(id2);
        });
        
        test('deve retornar string', () => {
            expect(typeof generateId()).toBe('string');
        });
    });
    
    describe('formatDateBR', () => {
        test('deve formatar data corretamente', () => {
            const date = new Date('2026-08-07');
            expect(formatDateBR(date)).toBe('07/08/2026');
        });
    });
});