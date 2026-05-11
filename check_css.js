const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');
const styles = html.match(/<style>[\s\S]*?<\/style>/g);
if (!styles) {
  console.log("NO STYLE BLOCKS FOUND");
} else {
  console.log("Found " + styles.length + " style blocks.");
  // Basic CSS sanity check
  styles.forEach((s, i) => {
    let openBraces = (s.match(/\{/g) || []).length;
    let closeBraces = (s.match(/\}/g) || []).length;
    console.log(`Block ${i + 1}: { count=${openBraces}, } count=${closeBraces}`);
  });
}
