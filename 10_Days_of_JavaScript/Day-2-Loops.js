/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    const vowels = 'aeiou';
    var consonants = '';
    
    'var i = 0; i < s.length; i++ ... '
    'left boundry =0, right = length of s and increment = 1'
    for(var i = 0; i < s.length; i++) {
        'if character from s is in substring'
        'then output the character'
        if (vowels.includes(s[i])) {
            console.log(s[i]);
        }
        else {
            'else, build a string of consonants'
            consonants += s[i] + '\n';
        }
    }
    'output consonants and trim to display'
    'only the character (no white space etc)'
    console.log(consonants.trim());
}
