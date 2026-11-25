// Turn design.html into entry.png (1024x1024) with headless Chrome.
// Run by hand: node render.mjs. The grader never runs this file;
// it only runs main.py, which ships the PNG this script produces.
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { createRequire } from 'node:module';

const dir = dirname(fileURLToPath(import.meta.url));
const tools = new URL('../token-radar-tools/package.json', import.meta.url);
const need = createRequire(tools);
const puppeteer = need('puppeteer-core');

const chrome = join(
  process.env.HOME,
  'workspace/makefun/token-radar-tools/chrome/linux-157.0.8103.78/chrome-linux64/chrome',
);

const browser = await puppeteer.launch({
  executablePath: chrome,
  headless: 'new',
  args: ['--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--force-device-scale-factor=1'],
});
try {
  const page = await browser.newPage();
  await page.setViewport({ width: 1024, height: 1024 });
  await page.goto('file://' + join(dir, 'design.html'), { waitUntil: 'networkidle0', timeout: 30000 });
  await new Promise((r) => setTimeout(r, 400));
  await page.screenshot({ path: join(dir, 'entry.png'), type: 'png' });
  console.log('rendered ' + join(dir, 'entry.png'));
} finally {
  await browser.close();
}
