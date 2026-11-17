# fink. tanıtım sitesi

Fink çöpçatan uygulamasının tanıtım sitesi. Statik bir site: derleme adımı yok, bu klasör olduğu gibi yayınlanır.

## Yayınlama

Kök klasörde `index.html` var. Herhangi bir statik barındırma yeterli:

- **Cloudflare Pages:** Workers & Pages → Create → Pages → bu repoyu bağla.
  - Framework preset: *None*
  - Build command: *(boş)*
  - Build output directory: `/`
- **Netlify / Vercel:** Build command boş, publish directory `.`.
- **GitHub Pages:** Settings → Pages → Branch: `main`, klasör `/ (root)`.

Yerelde denemek için: `npx serve .` ya da `python3 -m http.server 8080`.

> Not: `*.workers.dev` ve `*.pages.dev` adresleri Türkiye'den erişilemiyor. Siteyi kendi alan adına bağla (ör. `fink.dilakarakurt.com` ya da `www.…`).

## Dosyalar

| Dosya | Ne |
|---|---|
| `index.html` | Sayfa: anlamlı HTML, bütün metinler burada |
| `site.css`, `site.js` | Sayfaya özel stil ve davranış |
| `scrollcraft.css`, `scrollcraft.js` | Kaydırma motoru ([scroll-craft](https://github.com/nateherkai/scroll-craft), MIT). Projeye göre düzenlenmez |
| `assets/fink-logic.js` | Uygulamanın kendi kuralları (isimler, mesafe, karar, buzkıranlar, kafe seçimi, snap süresi), uygulama reposundaki `src/logic` dosyalarından paketlenir |
| `assets/fonts/` | Fredoka (Türkçe harfler eklenmiş marka sürümü) ve Inter, ikisi de OFL 1.1 |
| `docs/BRIEF.md` | Tasarım kararları: düzen, duygu eğrisi, doruk an, imza hareketi |
| `licenses/` | Motorun ve fontların lisansları |

## Sayfa ne yapıyor

Sayfa uygulamanın kendisi gibi davranır ve örnek bir senaryo üzerinde gerçek kurallarla çalışır:

1. **Açılış:** Ziyaretçiye bir hayvan ismi verilir. İsim bir kez değiştirilebilir ve sayfa boyunca onunla kalır.
2. **Radar:** Kaydırdıkça yakındakiler belirir, biri sana çarpar.
3. **Strike:** İkiniz de çarptınız.
4. **FinkRoom:** 90 saniye kaydırmanın altında akar. Sıfırda karar kartı çıkar; ikisi de Devam derse saat kırılır. Oda gerçekten çalışır: buzkıran gönderilebilir, mesaj yazılabilir.
5. **FinkSnap:** 5 saniye görünür, sonra silinir.
6. **FinkMeet ve İkinci Şans:** İkinize de 700 m içindeki kafeler; kibar veda şablonları.
7. **Kapanış:** 18+ onayı ve **APK'yı indir**.

## İndirme düğmesi

Düğme şu adrese gider:

```
https://github.com/dkarakurt/blitzdate/releases/latest/download/fink.apk
```

Uygulama reposunda `fink.apk` dosyası içeren bir GitHub Release yayınlanınca çalışır. Adresi değiştirmek için `index.html` içinde `data-download` geçen satıra bak.

## Kuralları güncellemek

Uygulamanın kuralları değişirse `assets/fink-logic.js` yeniden paketlenir. Uygulama reposunda:

```bash
cd web/builds/fink
npx esbuild src/logic-entry.ts --bundle --format=iife --global-name=FinkLogic --target=es2019 --minify --outfile=assets/fink-logic.js
```

Çıkan dosyayı bu repodaki `assets/fink-logic.js` ile değiştir.
