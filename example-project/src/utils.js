/**
 * Utilitários de exemplo para o projeto
 * Simula funções comuns em um ambiente de trabalho real
 */

/**
 * Formata uma string para título (primeira letra maiúscula)
 * @param {string} str - String para formatar
 * @returns {string} String formatada
 */
function toTitleCase(str) {
    if (!str) return '';
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

/**
 * Valida se um email está em formato válido
 * @param {string} email - Email para validar
 * @returns {boolean} True se válido, false caso contrário
 */
function validateEmail(email) {
    // Regex melhorado para aceitar subdomínios
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+(\.[^\s@]+)*$/;
    return regex.test(email);
}

/**
 * Gera um ID único
 * @returns {string} ID único
 */
function generateId() {
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
}

/**
 * Formata data para formato brasileiro
 * @param {Date} date - Data para formatar
 * @returns {string} Data formatada
 */
function formatDateBR(date) {
    const d = new Date(date);
    const day = String(d.getDate()).padStart(2, '0');
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const year = d.getFullYear();
    return `${day}/${month}/${year}`;
}

module.exports = {
    toTitleCase,
    validateEmail,
    generateId,
    formatDateBR
};