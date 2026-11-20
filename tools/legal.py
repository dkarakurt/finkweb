# Yasal sayfaları üretir: python3 tools/legal.py  (kökten çalıştır)
# Tek kaynak: aşağıdaki metinler. Değişiklikten sonra yeniden çalıştır ve SURUM'u güncelle.
import html, os, re

SURUM = "20 Kasım 2026"
SORUMLU = "Deniz Karakurt"
SEHIR = "İstanbul"
EPOSTA = "deniz.karakurt@hotmail.com"
SITE = "https://fink.denizkarakurt.com"

def md(text):
    """Çok basit biçim: '## ' başlık, '- ' madde, boş satır paragraf, **kalın**, [metin](adres)."""
    out, items = [], []
    def flush():
        if items:
            out.append("<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>")
            items.clear()
    def inline(s):
        s = html.escape(s, quote=False)
        s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
        s = re.sub(r"\[(.+?)\]\((.+?)\)", r'<a href="\2">\1</a>', s)
        return s
    for raw in text.strip().split("\n"):
        line = raw.rstrip()
        if line.startswith("## "):
            flush(); out.append(f"<h2>{inline(line[3:])}</h2>")
        elif line.startswith("- "):
            items.append(inline(line[2:]))
        elif not line:
            flush()
        else:
            flush(); out.append(f"<p>{inline(line)}</p>")
    flush()
    return "\n".join(out)

LOGO = '<svg viewBox="0 0 512 512" aria-hidden="true"><g fill="currentColor" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M214 250 L196 70" stroke-width="80" fill="none"/><path d="M296 250 L314 140 Q326 84 376 110 L424 152" stroke-width="80" fill="none"/><circle cx="256" cy="336" r="140" stroke="none"/></g><g stroke="#14122B" stroke-width="18" fill="none" stroke-linecap="round"><path d="M182 342 Q206 368 230 342"/><path d="M282 342 Q306 368 330 342"/></g></svg>'

PAGES = [
  ("gizlilik", "Gizlilik Politikası", "Fink'in hangi verileri neden topladığı, kimlerle paylaştığı, ne kadar sakladığı ve haklarını nasıl kullanacağın."),
  ("hesap-silme", "Hesabını ve verilerini silme", "Fink hesabını ve ona bağlı verileri nasıl sildirebileceğin."),
  ("cocuk-guvenligi", "Çocuk güvenliği standartları", "Fink'in çocukların cinsel istismarına ve sömürüsüne karşı standartları."),
  ("kosullar", "Kullanım Koşulları", "Fink'i kullanırken geçerli kurallar."),
]

BODY = {}

BODY["gizlilik"] = f"""
Bu politika, **Fink** mobil uygulamasının (Google Play'de "Fink.", paket adı `com.finkapp.android`) kişisel verileri nasıl işlediğini anlatır. Aynı zamanda 6698 sayılı Kişisel Verilerin Korunması Kanunu (KVKK) kapsamındaki aydınlatma metnidir.

## Veri sorumlusu
{SORUMLU}, {SEHIR}. İletişim: [{EPOSTA}](mailto:{EPOSTA})

## Kısaca
- Fink'te adın, yaşın, telefon numaran, e-postan ya da profil fotoğrafın yoktur. Sana rastgele bir hayvan ismi verilir.
- Konumun yalnızca uygulama açıkken kullanılır; kimse kesin konumunu görmez.
- Verilerini satmayız, reklam için kullanmayız, reklam ve analiz şirketleriyle paylaşmayız.
- Hesabını uygulamanın içinden istediğin an silebilirsin.

## Topladığımız veriler
**Hesap verileri:** Rastgele oluşturulan kullanıcı kimliği, sana atanan hayvan ismi, seçtiğin cinsiyet, 18 yaşından büyük olduğuna dair beyanın, kabul ettiğin koşulların sürümü ve tarihi. Oturumun için telefonuna rastgele bir anahtar verilir; sunucuda bu anahtarın kendisi değil, geri çevrilemeyen özeti saklanır.

**Konum:** Uygulama açıkken telefonunun konumu. Yakınındaki kişileri bulmak, aranızdaki yaklaşık mesafeyi göstermek ve ikinize de yakın buluşma noktaları önermek için kullanılır. Uygulama arka planda konum almaz.

**Mesajlar ve fotoğraflar:** Eşleştiğin kişiyle yazdığın mesajlar ve isteğe bağlı olarak gönderdiğin anlık fotoğraf. Fotoğraf yalnızca uygulamanın kamerasıyla o an çekilebilir; galerine erişilmez.

**Güvenlik kayıtları:** Engellediğin kişiler, gönderdiğin şikayetler (seçtiğin neden ve yazdığın not) ve hakkında yapılan şikayetler.

**Teknik ve teşhis verileri:** Uygulama çökerse hata mesajı, telefonunun işletim sistemi ve sürümü ile uygulama sürümü. Ayrıca hataları bulmak için uygulamanın adım kayıtları: hangi ekranın açıldığı, sunucuya hangi isteğin gittiği ve sonucu (konum, mesaj içeriği ve fotoğraf bu kayıtlara girmez). Sunucuya bağlanırken IP adresin, hizmeti sunmak ve kötüye kullanımı önlemek için altyapı sağlayıcımız tarafından işlenir.

## Verileri neden işliyoruz
- Hizmeti sunmak: yakındaki kişileri göstermek, eşleştirmek, sohbet ve buluşma önerisi (KVKK m.5/2-c, sözleşmenin kurulması ve ifası).
- Güvenlik: şikayetleri incelemek, kuralları ihlal eden hesapları kapatmak, kötüye kullanımı önlemek (KVKK m.5/2-f, meşru menfaat; m.5/2-ç, hukuki yükümlülük).
- Uygulamanın düzgün çalışması: hataları bulmak ve düzeltmek (KVKK m.5/2-f, meşru menfaat).

## Kimin neyi görebildiği
- Diğer kullanıcılar yalnızca hayvan ismini ve aranızdaki yuvarlanmış yaklaşık mesafeyi görür; yön ve kesin konum gösterilmez.
- Mesajlarını yalnızca eşleştiğin kişi görür. Anlık fotoğrafı alıcı bir kez, 5 saniye görür.
- Buluşma önerisinde iki tarafa da yalnızca önerilen kafeler ve yürüme süreleri gösterilir; kimsenin konumu paylaşılmaz.

## Paylaştığımız taraflar
- **Cloudflare, Inc.:** Sunucularımız ve veritabanımız Cloudflare'de, Avrupa Birliği'ndeki veri merkezlerinde çalışır (hesap kayıtları Batı Avrupa'da). Cloudflare verileri yalnızca bizim adımıza, hizmeti sunmak için işler.
- **OpenStreetMap / Overpass:** Kafe önerileri kendi veritabanımızdan gelir. Yalnızca o bölge için veritabanında kafe yoksa, iki kişinin orta noktasının koordinatı (kimlik bilgisi olmadan) kafe aramak için Overpass hizmetine gönderilir.
- **Google Play:** Uygulamayı Google Play üzerinden indirirsin; Google'ın kendi gizlilik politikası geçerlidir.
- **Yetkili makamlar:** Kanunen zorunlu olduğunda ya da bir çocuğun güvenliği söz konusu olduğunda yetkili makamlarla paylaşılabilir.

Verilerin, sunucuların Avrupa Birliği'nde bulunması nedeniyle yurt dışına aktarılır. Aktarım KVKK m.9'a uygun olarak gerçekleştirilir.

## Saklama süreleri
- **Konum:** En fazla 15 dakika. Uygulamayı kapattığında ya da arka plana aldığında hemen silinir.
- **Anlık fotoğraf:** Açıldığı an silinir; açılmazsa 24 saat sonra silinir.
- **Mesajlar:** Sohbet kapandıktan 30 gün sonra silinir.
- **Hata raporları:** 14 gün. **Adım kayıtları:** 3 gün.
- **Şikayet kayıtları:** İncelemenin ve olası hukuki süreçlerin gerektirdiği süre boyunca.
- **Hesap verileri:** Hesabını silene kadar.

## Hesabını silmek
Uygulamada profil ekranından **Hesabımı sil** ile hesabını ve kişisel verilerini hemen silebilirsin. Uygulamaya erişemiyorsan [hesap silme sayfasına](../hesap-silme/) bak.

## Güvenlik
Uygulama ile sunucu arasındaki tüm bağlantılar şifrelidir (HTTPS). Oturum anahtarın telefonunun güvenli deposunda tutulur. Android'de anlık fotoğraf ekranında ekran görüntüsü engellenir.

## 18 yaş sınırı
Fink yalnızca 18 yaşını doldurmuş kişiler içindir. 18 yaşından küçük olduğu anlaşılan hesaplar kapatılır ve verileri silinir. Ayrıntılar için [çocuk güvenliği standartlarımıza](../cocuk-guvenligi/) bak.

## Hakların
KVKK m.11 uyarınca verilerinin işlenip işlenmediğini öğrenme, bilgi isteme, işlenme amacını öğrenme, aktarıldığı tarafları bilme, düzeltilmesini ya da silinmesini isteme, itiraz etme ve zararının giderilmesini talep etme hakkın vardır. Başvurunu [{EPOSTA}](mailto:{EPOSTA}) adresine gönderebilirsin; en geç 30 gün içinde yanıtlanır. Hesabın anonim olduğu için başvurunda uygulamadaki hayvan ismini belirtmen, seni bulmamızı kolaylaştırır.

## Değişiklikler
Bu politika güncellenebilir. Önemli değişikliklerde uygulama içinde bilgilendirilirsin. Bu sayfanın sürümü: {SURUM}.
"""

BODY["hesap-silme"] = f"""
Bu sayfa **Fink** uygulamasının (Google Play'de "Fink.", geliştirici: {SORUMLU}) hesap ve veri silme yöntemini anlatır.

## Uygulamanın içinden (en hızlısı)
- Fink'i aç.
- Radar ekranında sağ üstteki hayvan isminle gösterilen profiline dokun.
- **Hesabımı sil**'e, ardından **Evet, hesabımı sil**'e dokun.

Hesabın ve ona bağlı veriler hemen silinir; uygulama seni başlangıç ekranına döndürür.

## Uygulamaya erişemiyorsan
Uygulamayı sildiysen ya da açamıyorsan [{EPOSTA}](mailto:{EPOSTA}) adresine "Fink hesap silme" konulu bir e-posta gönder. Hesaplar anonim olduğu için hatırlıyorsan uygulamadaki hayvan ismini (örneğin "Cesur Vaşak") ve yaklaşık kayıt tarihini yaz. Talebin en geç 30 gün içinde sonuçlandırılır.

Not: Fink'te e-posta ya da telefonla giriş olmadığı için uygulamayı silmek, oturum anahtarını da telefondan siler. Bu durumda hesabın kimseyle eşleşmez, radarda görünmez ve kapanmış sohbetleri 30 gün içinde kendiliğinden silinir.

## Neler silinir
- Hesap verileri: kullanıcı kimliği, hayvan ismi, cinsiyet, yaş beyanı, oturum anahtarının özeti.
- Konum kaydı.
- Açılmamış anlık fotoğraflar.
- Engelleme listen.

## Neler bir süre saklanabilir
- **Mesajlar:** Karşı tarafın da gördüğü sohbet mesajları, sohbet kapandıktan sonra en geç 30 gün içinde silinir.
- **Şikayet kayıtları:** Senin yaptığın ya da hakkında yapılan şikayetler, incelemenin ve olası hukuki süreçlerin gerektirdiği süre boyunca saklanabilir.
- **Teknik kayıtlar:** Hata raporları en fazla 14 gün, adım kayıtları en fazla 3 gün tutulur.
"""

BODY["cocuk-guvenligi"] = f"""
**Fink** (Google Play'de "Fink.", geliştirici: {SORUMLU}) çocukların cinsel istismarına ve sömürüsüne (CSAE) ve çocuk istismarı içeriğine (CSAM) karşı sıfır tolerans uygular.

## Yaş sınırı
Fink yalnızca 18 yaşını doldurmuş kişiler içindir. Kayıtta 18 yaşından büyük olduğunu onaylaman istenir. 18 yaşından küçük olduğu anlaşılan hesaplar derhal kapatılır.

## Kesinlikle yasak olanlar
- Çocukları cinselleştiren, istismar eden ya da tehlikeye atan her türlü içerik ve davranış.
- Çocuk istismarı içeriği (CSAM) paylaşmak, istemek ya da bu tür içeriğe yönlendirmek.
- Bir çocukla cinsel amaçla iletişim kurmaya çalışmak (grooming), cinsel şantaj ve çocuk ticareti.
- 18 yaşından küçük birinin uygulamayı kullanmasına aracılık etmek.

## Nasıl bildirirsin
- **Uygulamanın içinden:** Sohbet ekranının üst kısmındaki kalkan simgesine dokun, nedeni seç, istersen not ekle ve **Şikayet et ve engelle**'ye dokun. Kişi engellenir, şikayetin incelemeye gönderilir.
- **E-postayla:** [{EPOSTA}](mailto:{EPOSTA}). Konu satırına "Çocuk güvenliği" yaz.
- Bir çocuk tehlikedeyse önce **112**'yi ara. İnternetteki çocuk istismarı içeriğini [ihbarweb.org.tr](https://www.ihbarweb.org.tr) üzerinden de bildirebilirsin.

## Bildirimlere ne yapıyoruz
- Çocuk güvenliğiyle ilgili şikayetler öncelikli olarak incelenir.
- İhlal tespit edilen hesap kalıcı olarak kapatılır ve ilgili içerik kaldırılır.
- Çocuk istismarı içeriği tespit edildiğinde yürürlükteki mevzuat uyarınca yetkili makamlara (Türkiye'de kolluk kuvvetleri ve Cumhuriyet savcılığı) bildirilir; yasal soruşturmalar için gereken kayıtlar saklanır.
- Yetkili makamların taleplerine mevzuat çerçevesinde iş birliği yapılır.

## Çocuk güvenliği iletişim kişisi
{SORUMLU}. E-posta: [{EPOSTA}](mailto:{EPOSTA})

Sürüm: {SURUM}
"""

BODY["kosullar"] = f"""
## 1. Taraflar ve kapsam
Bu koşullar, {SORUMLU} ("Fink") tarafından sunulan Fink mobil uygulamasının kullanımını düzenler. Uygulamaya kaydolarak bu koşulları ve [Gizlilik Politikası](../gizlilik/)'nı kabul etmiş olursun.

## 2. Yaş sınırı
Fink yalnızca 18 yaşını doldurmuş kişiler içindir. 18 yaşından küçük olduğu anlaşılan hesaplar kapatılır. 18 yaşından küçük birini fark edersen lütfen sohbet ekranındaki kalkan simgesinden şikayet et.

## 3. Anonimlik
Fink'te adın, yaşın ya da fotoğrafın yoktur; sana rastgele bir hayvan ismi verilir. Sohbette kendi isteğinle paylaştığın bilgilerden sen sorumlusun.

## 4. Davranış kuralları
Şunlar yasaktır: taciz, tehdit, nefret söylemi; istenmeyen cinsel içerik; başkasının kişisel bilgilerini paylaşmak; dolandırıcılık, reklam ve spam; anlık fotoğrafla çıplaklık ya da müstehcen görüntü göndermek; başka birinin yerine geçmek; uygulamanın güvenlik önlemlerini aşmaya çalışmak. Çocuk güvenliğine ilişkin kurallar için [çocuk güvenliği standartlarımıza](../cocuk-guvenligi/) bak.

## 5. Anlık fotoğraf
Anlık fotoğraf yalnızca o an kamerayla çekilir, alıcı tarafından 5 saniye görüntülenir ve ardından silinir. Ekran görüntüsü almaya ya da başka bir cihazla kaydetmeye çalışmak yasaktır.

## 6. Buluşma güvenliği
Uygulama yalnızca halka açık kafeleri önerir. İlk buluşmayı her zaman kalabalık, halka açık bir yerde yap; bir yakınına nerede olduğunu haber ver; kendini güvende hissetmezsen ayrıl. Fink kullanıcıların kimliğini doğrulamaz ve buluşmalarda yaşanan olaylardan sorumlu değildir.

## 7. Şikayet ve engelleme
Rahatsız olduğun herkesi engelleyebilir ve şikayet edebilirsin. Şikayetler incelenir; kuralları ihlal eden hesaplar uyarı yapılmaksızın kapatılabilir.

## 8. Hesabın silinmesi
Profil ekranındaki **Hesabımı sil** ile hesabını ve kişisel verilerini dilediğin an silebilirsin. Ayrıntılar: [hesap silme](../hesap-silme/).

## 9. Değişiklikler
Bu koşullar güncellenebilir; önemli değişikliklerde uygulama içinde yeniden onayın istenir.

## 10. İletişim
[{EPOSTA}](mailto:{EPOSTA})

Sürüm: {SURUM}
"""

NAV = "".join(f'<a href="../{slug}/">{title}</a>' for slug, title, _ in PAGES)

TEMPLATE = """<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · fink.</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{site}/{slug}/">
<meta name="theme-color" content="#0F0D22">
<link rel="stylesheet" href="../assets/fonts.css">
<link rel="stylesheet" href="../assets/legal.css">
</head>
<body>
<header class="lg-bar">
  <a class="lg-brand" href="../">{logo}<span>fink.</span></a>
</header>
<main class="lg-main">
  <h1>{title}</h1>
  <p class="lg-meta">Son güncelleme: {surum}</p>
  {body}
</main>
<footer class="lg-foot">
  <nav aria-label="Yasal sayfalar">{nav}</nav>
  <p>© 2026 fink. · {sorumlu} · <a href="mailto:{eposta}">{eposta}</a></p>
</footer>
</body>
</html>
"""

for slug, title, desc in PAGES:
    os.makedirs(slug, exist_ok=True)
    page = TEMPLATE.format(title=html.escape(title), desc=html.escape(desc), site=SITE, slug=slug, logo=LOGO,
                           surum=SURUM, body=md(BODY[slug]), nav=NAV, sorumlu=SORUMLU, eposta=EPOSTA)
    with open(os.path.join(slug, "index.html"), "w", encoding="utf-8") as f:
        f.write(page)
    print("yazıldı:", slug + "/index.html")
