// Фото продуктов FitLine: ищет на странице картинку /cdnip/products/*.png, качает width=1200,
// обрезает по альфе > 200 (без отражения). Запуск: node olga_products.js SP
const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const SP = process.argv[2].replace(/\/$/, '') + '/';
const PRODUCTS = { '0702037': 'product.png', '0712062': 'product_lutein.png' };
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [id, name] of Object.entries(PRODUCTS)) {
    const urls = [];
    p.removeAllListeners('request');
    p.on('request', r => { const u = r.url(); if (/\/cdnip\/products\/[^?]+\.png\?width=640/.test(u)) urls.push(u); });
    await p.goto(`https://www.fitline.com/de/de-de/products/${id}`, { waitUntil: 'domcontentloaded', timeout: 90000 });
    await p.waitForTimeout(8000);
    if (!urls.length) { console.log('не найдено фото', id); continue; }
    const raw = SP + 'raw_' + name;
    execFileSync('curl', ['-sSfL', '-o', raw, urls[0].replace('width=640&quality=85', 'width=1200')]);
    execFileSync('python3', ['-I', '-c',
      'import sys;from PIL import Image;im=Image.open(sys.argv[1]).convert("RGBA");' +
      'bb=im.getchannel("A").point(lambda v:255 if v>200 else 0).getbbox();im.crop(bb).save(sys.argv[2])', raw, SP + name]);
    console.log(id, '->', SP + name);
  }
  await b.close();
})();
