const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const styles = html.match(/<style>([\s\S]*?)<\/style>/g);
if (styles) {
  styles.forEach((s, i) => {
    let singleQuotes = (s.match(/'/g) || []).length;
    let doubleQuotes = (s.match(/"/g) || []).length;
    console.log(`Block ${i + 1}: ' count=${singleQuotes}, " count=${doubleQuotes}`);
  });
}
